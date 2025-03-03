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
def create_landlord(name: str, email: str, properties: list[str]):
    try:
        # Create a new user document
        user = {"name": name, "email": email, "properties": properties}

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


# ----------------------------------- #


## tenant methods
@app.post("/create_tenant")
def create_tenant(name: str, email: str, phone: str, address: str, property_id: str):
    try:
        # Create a new user document
        user = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "property_id": ObjectId(property_id),
        }

        # Insert the user document into the "users" collection
        result = db.users.insert_one(user)

        # Return the inserted ID
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        return {"error": f"Failed to create tenant: {str(e)}"}


@app.get("/get_tenants")
def get_tenants():
    try:
        # Retrieve all users from the "users" collection
        users = db.users.find()

        # Create a list to store the users
        user_list = []

        # Iterate over the cursor and add each user to the list
        for user in users:
            user["_id"] = str(user["_id"])
            user_list.append(user)

        # Return the list of users
        return user_list
    except Exception as e:
        return {"error": f"Failed to fetch tenants: {str(e)}"}


# ----------------------------------- #


## property methods
@app.post("/create_property")
def create_property(location: str, landlord_id: str, tenants: list[str]):
    try:
        # Create a new property document
        property_doc = {
            "_id": ObjectId,
            "location": location,
            "landlord_id": ObjectId(landlord_id),
            "tenants": [ObjectId(tenant_id) for tenant_id in tenants],
        }

        # Insert the property document into the "properties" collection
        result = properties_collection.insert_one(property_doc)

        # Return the inserted ID
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        return {"error": f"Failed to create property: {str(e)}"}


@app.get("/get_properties")
def get_properties():
    try:
        # Retrieve all users from the "users" collection
        users = db.users.find()

        # Create a list to store the users
        user_list = []

        # Iterate over the cursor and add each user to the list
        for user in users:
            user["_id"] = str(user["_id"])
            user_list.append(user)

        # Return the list of users
        return user_list
    except Exception as e:
        return {"error": f"Failed to fetch properties: {str(e)}"}


# ----------------------------------- #


## contractor methods
@app.post("/create_contractor")
def create_landlord(name: str, work: list[str], phone: str, email: str, location: str):
    try:
        # Create a new user document
        user = {
            "_id": ObjectId,
            "name": name,
            "work": work,
            "phone": phone,
            "email": email,
            "location": location,
        }

        # Insert the user document into the "users" collection
        result = db.users.insert_one(user)

        # Return the inserted ID
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        return {"error": f"Failed to create contractor: {str(e)}"}


@app.get("/get_contractors")
def get_contractors():
    try:
        # Retrieve all users from the "users" collection
        users = db.users.find()

        # Create a list to store the users
        user_list = []

        # Iterate over the cursor and add each user to the list
        for user in users:
            user["_id"] = str(user["_id"])
            user_list.append(user)

        # Return the list of users
        return user_list
    except Exception as e:
        return {"error": f"Failed to fetch contractors: {str(e)}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)  # Enable auto-reload for development
