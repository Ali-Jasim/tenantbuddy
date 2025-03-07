from fastapi import FastAPI, Form
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from bson import ObjectId

# Load environment variables
load_dotenv()

# Get MongoDB connection details from environment variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_CLUSTER = os.getenv("DB_CLUSTER")

# Create MongoDB connection URI
uri = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@{DB_CLUSTER}/?retryWrites=true&w=majority&appName=Cluster0"


# Create a MongoDB client and connect to the server
try:
    client = MongoClient(uri)
    # Send a ping to confirm a successful connection
    client.admin.command("ping")

    print("Successfully connected to MongoDB!")

    # Connect to the database
    db = client["tenantbuddy"]
    print(db.list_collections().to_list())

    landlords_collection = db["landlords"]
    tenants_collection = db["tenants"]
    properties_collection = db["properties"]
    contractors_collection = db["contractors"]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# ===============================
# API Endpoints
# ===============================
app = FastAPI()


@app.get("/hello")
def hello_world():
    return {"Hello": "World"}


# ----------------------------------- #


## landlord methods
@app.post("/create_landlord")
def create_landlord(name: str, email: str, properties: list[str] = None):
    try:
        # Create a new user document
        user = {
            "name": name,
            "email": email,
            "properties": (
                properties if properties else []
            ),  # Initialize as empty list if not provided
        }

        # Insert the user document into the "users" collection
        result = landlords_collection.insert_one(user)

        # Return the inserted ID
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        return {"error": f"Failed to create landlord: {str(e)}"}


@app.get("/get_landlords")
def get_landlords():
    try:
        # Retrieve all users from the "users" collection
        users = landlords_collection.find()

        # Create a list to store the landlords
        landlord_list = []

        # Iterate over the cursor and add each landlord to the list
        for user in users:
            user["_id"] = str(user["_id"])  # Convert ObjectId to string
            landlord_list.append(user)

        # Return the list of landlords
        return {"landlords": landlord_list}
    except Exception as e:
        return {"error": f"Failed to fetch landlords: {str(e)}"}


@app.get("/get_landlord/{id}")
def get_landlord(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Find one landlord with the given ID
        landlord = landlords_collection.find_one({"_id": object_id})

        if not landlord:
            return {"error": "Landlord not found"}

        # Convert ObjectId to string for JSON serialization
        landlord["_id"] = str(landlord["_id"])

        return {"landlord": landlord}
    except Exception as e:
        return {"error": f"Failed to fetch landlord: {str(e)}"}


@app.put("/update_landlord/{id}")
def update_landlord(
    id: str, name: str = None, email: str = None, properties: list[str] = None
):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Get current landlord data
        current_landlord = landlords_collection.find_one({"_id": object_id})
        if not current_landlord:
            return {"error": "Landlord not found"}

        # Create update document with only provided fields
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if email is not None:
            update_data["email"] = email
        if properties is not None:
            update_data["properties"] = properties

        # Only update if there are fields to update
        if update_data:
            result = landlords_collection.update_one(
                {"_id": object_id}, {"$set": update_data}
            )

            return {"message": "Landlord updated successfully"}
        else:
            return {"message": "No fields to update were provided"}

    except Exception as e:
        return {"error": f"Failed to update landlord: {str(e)}"}


@app.delete("/delete_landlord/{id}")
def delete_landlord(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Delete the landlord with the given ID
        result = landlords_collection.delete_one({"_id": object_id})

        if result.deleted_count == 1:
            return {"message": "Landlord deleted successfully"}
        else:
            return {"error": "Landlord not found"}

    except Exception as e:
        return {"error": f"Failed to delete landlord: {str(e)}"}


@app.get("/get_landlord_by_name/{name}")
def get_landlord_by_name(name: str):
    try:
        # Find landlords with the given name
        landlords = landlords_collection.find({"name": name})

        # Create a list to store the landlords
        landlord_list = []

        # Iterate over the cursor and add each landlord to the list
        for landlord in landlords:
            landlord["_id"] = str(landlord["_id"])
            landlord_list.append(landlord)

        if not landlord_list:
            return {"error": "No landlords found with that name"}

        return {"landlords": landlord_list}
    except Exception as e:
        return {"error": f"Failed to fetch landlord: {str(e)}"}


@app.get("/get_landlord_by_email/{email}")
def get_landlord_by_email(email: str):
    try:
        # Find landlord with the given email
        landlord = landlords_collection.find_one({"email": email})

        if not landlord:
            return {"error": "Landlord not found"}

        # Convert ObjectId to string for JSON serialization
        landlord["_id"] = str(landlord["_id"])

        return {"landlord": landlord}
    except Exception as e:
        return {"error": f"Failed to fetch landlord: {str(e)}"}


@app.get("/get_landlord_properties/{id}")
def get_landlord_properties(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Find landlord with the given ID
        landlord = landlords_collection.find_one({"_id": object_id})

        if not landlord:
            return {"error": "Landlord not found"}

        # Get the list of properties
        properties = landlord.get("properties", [])

        return {"properties": properties}
    except Exception as e:
        return {"error": f"Failed to fetch properties: {str(e)}"}


# ----------------------------------- #


## tenant methods


@app.post("/create_tenant")
def create_tenant(name: str, email: str, phone: str, address: str):
    try:
        # Create a new user document
        user = {"name": name, "email": email, "phone": phone, "address": address}

        # Insert the user document into the "users" collection
        result = tenants_collection.insert_one(user)

        # Return the inserted ID
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        return {"error": f"Failed to create tenant: {str(e)}"}


@app.get("/get_tenants")
def get_tenants():

    try:
        # Retrieve all users from the "users" collection
        users = tenants_collection.find()

        # Create a list to store the tenants
        tenant_list = []

        # Iterate over the cursor and add each tenant to the list
        for user in users:
            user["_id"] = str(user["_id"])  # Convert ObjectId to string
            tenant_list.append(user)

        # Return the list of tenants
        return {"tenants": tenant_list}
    except Exception as e:
        return {"error": f"Failed to fetch tenants: {str(e)}"}


@app.get("/get_tenant/{id}")
def get_tenant(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Find one tenant with the given ID
        tenant = tenants_collection.find_one({"_id": object_id})

        if not tenant:
            return {"error": "Tenant not found"}

        # Convert ObjectId to string for JSON serialization
        tenant["_id"] = str(tenant["_id"])

        return {"tenant": tenant}
    except Exception as e:
        return {"error": f"Failed to fetch tenant: {str(e)}"}


@app.put("/update_tenant/{id}")
def update_tenant(
    id: str, name: str = None, email: str = None, phone: str = None, address: str = None
):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Get current tenant data
        current_tenant = tenants_collection.find_one({"_id": object_id})
        if not current_tenant:
            return {"error": "Tenant not found"}

        # Create update document with only provided fields
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if email is not None:
            update_data["email"] = email
        if phone is not None:
            update_data["phone"] = phone
        if address is not None:
            update_data["address"] = address

        # Only update if there are fields to update
        if update_data:
            result = tenants_collection.update_one(
                {"_id": object_id}, {"$set": update_data}
            )

            return {"message": "Tenant updated successfully"}
        else:
            return {"message": "No fields to update were provided"}

    except Exception as e:
        return {"error": f"Failed to update tenant: {str(e)}"}


@app.delete("/delete_tenant/{id}")
def delete_tenant(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Delete the tenant with the given ID
        result = tenants_collection.delete_one({"_id": object_id})

        if result.deleted_count == 1:
            return {"message": "Tenant deleted successfully"}
        else:
            return {"error": "Tenant not found"}

    except Exception as e:
        return {"error": f"Failed to delete tenant: {str(e)}"}


@app.get("/get_tenant_by_name/{name}")
def get_tenant_by_name(name: str):
    try:
        # Find tenants with the given name
        tenants = tenants_collection.find({"name": name})

        # Create a list to store the tenants
        tenant_list = []

        # Iterate over the cursor and add each tenant to the list
        for tenant in tenants:
            tenant["_id"] = str(tenant["_id"])
            tenant_list.append(tenant)

        if not tenant_list:
            return {"error": "No tenants found with that name"}

        return {"tenants": tenant_list}
    except Exception as e:
        return {"error": f"Failed to fetch tenant: {str(e)}"}


# ----------------------------------- #


## contractor methods
@app.post("/create_contractor")
def create_contractor(name: str, email: str, phone: str, skills: list[str] = None):
    try:
        # Create a new user document
        user = {
            "name": name,
            "email": email,
            "phone": phone,
            "skills": (
                skills if skills else []
            ),  # Initialize as empty list if not provided
        }

        # Insert the user document into the "users" collection
        result = contractors_collection.insert_one(user)

        # Return the inserted ID
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        return {"error": f"Failed to create contractor: {str(e)}"}


@app.get("/get_contractors")
def get_contractors():
    try:
        # Retrieve all users from the "users" collection
        users = contractors_collection.find()

        # Create a list to store the contractors
        contractor_list = []

        # Iterate over the cursor and add each contractor to the list
        for user in users:
            user["_id"] = str(user["_id"])  # Convert ObjectId to string
            contractor_list.append(user)

        # Return the list of contractors
        return {"contractors": contractor_list}
    except Exception as e:
        return {"error": f"Failed to fetch contractors: {str(e)}"}


@app.get("/get_contractor/{id}")
def get_contractor(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Find one contractor with the given ID
        contractor = contractors_collection.find_one({"_id": object_id})

        if not contractor:
            return {"error": "Contractor not found"}

        # Convert ObjectId to string for JSON serialization
        contractor["_id"] = str(contractor["_id"])

        return {"contractor": contractor}
    except Exception as e:
        return {"error": f"Failed to fetch contractor: {str(e)}"}


@app.put("/update_contractor/{id}")
def update_contractor(
    id: str,
    name: str = None,
    email: str = None,
    phone: str = None,
    skills: list[str] = None,
):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Get current contractor data
        current_contractor = contractors_collection.find_one({"_id": object_id})
        if not current_contractor:
            return {"error": "Contractor not found"}

        # Create update document with only provided fields
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if email is not None:
            update_data["email"] = email
        if phone is not None:
            update_data["phone"] = phone
        if skills is not None:
            update_data["skills"] = skills

        # Only update if there are fields to update
        if update_data:
            result = contractors_collection.update_one(
                {"_id": object_id}, {"$set": update_data}
            )

            return {"message": "Contractor updated successfully"}
        else:
            return {"message": "No fields to update were provided"}

    except Exception as e:
        return {"error": f"Failed to update contractor: {str(e)}"}


@app.delete("/delete_contractor/{id}")
def delete_contractor(id: str):
    try:
        # Convert string ID to ObjectId
        object_id = ObjectId(id)

        # Delete the contractor with the given ID
        result = contractors_collection.delete_one({"_id": object_id})

        if result.deleted_count == 1:
            return {"message": "Contractor deleted successfully"}
        else:
            return {"error": "Contractor not found"}

    except Exception as e:
        return {"error": f"Failed to delete contractor: {str(e)}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # Enable auto-reload for development
