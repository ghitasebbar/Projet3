description = """ This API helps you query data from a mongodb database.
This database holds a table with 180 000 products information from Amazon.
The data are available for download at https://data.world/promptcloud/fashion-products-on-amazon-com

## Queries
* Get products from the table
* Save a new product in the table

"""

from fastapi import FastAPI, Request
from pydantic import BaseModel
import motor.motor_asyncio
from fastapi.encoders import jsonable_encoder

app = FastAPI(
        title='Projet 3 API',
        description=description,
        version="0.0.1",
        contact={
        }
    )

class ProductSchema(BaseModel):
    uniq_id: str
    product_name: str
    manufacturer: str
    price: str
    number_available_in_stock: str
    number_of_reviews: int)
    number_of_answered_questions: float
    average_review_rating: str
    amazon_category_and_sub_category: str
    customers_who_bought_this_item_also_bought: str
    description: str
    product_information: str
    product_description: str
    items_customers_buy_after_viewing_this_item: str
    customer_questions_and_answers: str
    customer_reviews: str
    sellers: str

######
    ## Database info
    ########

MONGO_INFO = "mongodb://root:root@mongodb:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_INFO)

database = client.projet3

products = database.get_collection("produits")

######
    ## Helpers
    ########

def ResponseModel(data, message):
    return {
        "data":[data],
        "code":200,
        "message":message
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "product_name": str(product["product_name"]),
        "manufacturer": str(product["manufacturer"]),
        "price": str(product["price"]),
        "number_available_in_stock": str(product["number_available_in_stock"]),
        "number_of_reviews": int(product["number_of_reviews"]),
        "number_of_answered_questions": float(product["number_of_answered_questions"]),
        "average_review_rating": str(product["average_review_rating"]),
        "amazon_category_and_sub_category": str(product["amazon_category_and_sub_category"]),
        "customers_who_bought_this_item_also_bought": str(product["customers_who_bought_this_item_also_bought"]),
        "description": str(product["description"]),
        "product_information": str(product["product_information"]),
        "product_description": str(product["product_description"]),
        "items_customers_buy_after_viewing_this_item": str(product["items_customers_buy_after_viewing_this_item"]),
        "customer_questions_and_answers": str(product["customer_questions_and_answers"]),
        "customer_reviews": str(product["customer_reviews"]),
        "sellers": str(product["sellers"])

    }

# Retrieve products from the collection
async def get_products(n):
    prods = []
    async for product in products.find().limit(n):
        prods.append(product_helper(product))
    return prods

# Add a new product to the collection
async def add_product(prod_data: dict) -> dict:
    product = await products.insert_one(prod_data)
    new_product = await products.find_one({"_id": product.inserted_id})
    return product_helper(new_product)

######
    ## Routes
    ########

@app.get("/", tags=["Root"])
async def welcome():
    return {"message": "Welcome !"}

@app.get("/read/document", tags=["Read"])
async def get_n_document(n: int, request: Request):
    products = await get_products(n)
    if products:
        return ResponseModel(products, "Products retrieved successfully")
    return ResponseModel(products, "No product returned")

@app.post("/add/document", tags=["Create"])
async def add_document(product: ProductSchema, request: Request):
    prod = jsonable_encoder(product)
    new_prod = await add_product(prod)
    return ResponseModel(new_prod, "Product add success.")


