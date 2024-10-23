from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

# Define a root endpoint that returns a simple message
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a GET endpoint with a path parameter
# GET /items/5?q=test
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Define a POST endpoint that accepts data in JSON format
# POST /create-item
@app.post("/create-item")
def create_item(item: dict):
    return {"message": "Item created", "item": item}

# Define a PUT endpoint for updating an item
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: dict):
    return {"message": "Item updated", "item_id": item_id, "updated_data": item}
