from fastapi import FastAPI, Form, Request, HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
from typing import Optional
import os
from bson import ObjectId
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Load environment variables
load_dotenv()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_CLUSTER = os.getenv("DB_CLUSTER")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

# MongoDB connection setup
MONGO_URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_CLUSTER}/?retryWrites=true&w=majority&appName=Cluster0"
try:
    client = MongoClient(MONGO_URI)
    client.admin.command("ping")
    db = client["tenantbuddy"]
    landlords = db["landlords"]
    tenants = db["tenants"]
    properties = db["properties"]
    contractors = db["contractors"]
    issues = db["issues"]
except Exception as e:
    raise Exception(f"Failed to connect to MongoDB: {e}")

# Twilio client initialization
twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

# FastAPI application with CORS
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Utility function for issue categorization
def categorize_issue(description: str) -> str:
    description = description.lower()
    if "leak" in description or "pipe" in description:
        return "plumbing"
    if "light" in description or "electric" in description:
        return "electrical"
    return "general"


# Tenant endpoints
@app.post("/tenants")
async def create_tenant(name: str = Form(...), phone: str = Form(...)):
    tenant_data = {"name": name, "phone": phone}
    result = tenants.insert_one(tenant_data)
    return {
        "inserted_id": str(result.inserted_id),
        "message": "Tenant created successfully",
    }


@app.get("/tenants")
async def get_tenants():
    tenant_list = list(tenants.find())
    for tenant in tenant_list:
        tenant["_id"] = str(tenant["_id"])
    return {"tenants": tenant_list}


# Contractor endpoints
@app.post("/contractors")
async def create_contractor(
    name: str = Form(...), phone: str = Form(...), specialty: str = Form(...)
):
    contractor_data = {"name": name, "phone": phone, "specialty": specialty}
    result = contractors.insert_one(contractor_data)
    return {
        "inserted_id": str(result.inserted_id),
        "message": "Contractor created successfully",
    }


@app.get("/contractors")
async def get_contractors():
    contractor_list = list(contractors.find())
    for contractor in contractor_list:
        contractor["_id"] = str(contractor["_id"])
    return {"contractors": contractor_list}


# Property endpoints
@app.post("/properties")
async def create_property(address: str = Form(...)):
    property_data = {"address": address}
    result = properties.insert_one(property_data)
    return {
        "inserted_id": str(result.inserted_id),
        "message": "Property created successfully",
    }


@app.get("/properties")
async def get_properties():
    property_list = list(properties.find())
    for property in property_list:
        property["_id"] = str(property["_id"])
    return {"properties": property_list}


# Issue endpoints
@app.post("/issues")
async def create_issue(
    description: str = Form(...),
    tenant_id: Optional[str] = Form(None),
    tenantPhone: Optional[str] = Form(None),
):
    # Validate that we have at least one tenant identifier
    if not tenant_id and not tenantPhone:
        raise HTTPException(
            status_code=400, detail="Either tenant_id or tenantPhone must be provided"
        )

    # Find tenant by ID first (preferred method)
    if tenant_id:
        try:
            tenant = tenants.find_one({"_id": ObjectId(tenant_id)})
            if not tenant:
                raise HTTPException(
                    status_code=404, detail="Tenant not found with provided ID"
                )
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Invalid tenant ID format: {str(e)}"
            )
    # Fallback to phone lookup only if ID is not provided
    else:
        tenant = tenants.find_one({"phone": tenantPhone})
        if not tenant:
            raise HTTPException(
                status_code=404, detail="Tenant not found with provided phone number"
            )

    category = categorize_issue(description)
    issue_data = {
        "description": description,
        "tenant_id": str(tenant["_id"]),
        "category": category,
        "resolved": False,
    }
    result = issues.insert_one(issue_data)
    return {
        "inserted_id": str(result.inserted_id),
        "message": "Issue created successfully",
    }


@app.get("/issues")
async def get_issues():
    issue_list = list(issues.find())
    for issue in issue_list:
        issue["_id"] = str(issue["_id"])
        issue["tenant_id"] = str(issue["tenant_id"])
    return {"issues": issue_list}


# Twilio SMS endpoint
@app.post("/sms")
async def receive_sms(request: Request):
    form_data = await request.form()
    phone = form_data["From"]
    message = form_data["Body"]
    tenant = tenants.find_one({"phone": phone})
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    category = categorize_issue(message)
    issue_data = {
        "description": message,
        "tenant_id": str(tenant["_id"]),
        "category": category,
        "resolved": False,
    }
    issues.insert_one(issue_data)
    response = MessagingResponse()
    response.message("Issue received. The landlord has been notified.")
    return str(response)


# Issue approval endpoint
@app.post("/issues/{issue_id}/approve")
async def approve_issue(issue_id: str, contractor_id: str = Form(...)):
    issue = issues.find_one({"_id": ObjectId(issue_id)})
    contractor = contractors.find_one({"_id": ObjectId(contractor_id)})
    tenant = tenants.find_one({"_id": ObjectId(issue["tenant_id"])}) if issue else None

    if not all([issue, contractor, tenant]):
        raise HTTPException(
            status_code=404, detail="Issue, contractor, or tenant not found"
        )

    issues.update_one(
        {"_id": ObjectId(issue_id)},
        {"$set": {"resolved": True, "contractor_id": contractor_id}},
    )

    # Send notifications
    twilio_client.messages.create(
        body=f"Your {issue['category']} issue is being handled by {contractor['name']}.",
        from_=TWILIO_PHONE,
        to=tenant["phone"],
    )
    twilio_client.messages.create(
        body=f"New job: {issue['description']} for tenant {tenant['phone']}.",
        from_=TWILIO_PHONE,
        to=contractor["phone"],
    )
    twilio_client.messages.create(
        body=f"Issue {issue_id} assigned to {contractor['name']}.",
        from_=TWILIO_PHONE,
        to="+1234567890",  # TODO: Replace with dynamic landlord phone
    )

    return {"message": "Issue approved and notifications sent"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
