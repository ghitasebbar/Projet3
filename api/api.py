description = """ This API helps you query data from a mongodb database.
This database holds a table with 180 000 products information from Amazon.
The data are available for download at https://data.world/promptcloud/fashion-products-on-amazon-com

## Queries
* Get products from the table
* Save a new product in the table

"""

from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
import motor.motor_asyncio
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder

app = FastAPI(
        title='Projet 3 API',
        description=description,
        version="0.0.1",
        contact={
        }
    )

class ProductSchema(BaseModel):
    uniq_id: str #= Field(...)
    product_name: str #= Field(...)
    manufacturer: str #= Field(...)
    price: str #=Field(...)
    number_available_in_stock: str #= Field(...)
    number_of_reviews: int #= Field(...)
    number_of_answered_questions: float #= Field(...)
    average_review_rating: str #= Field(...)
    amazon_category_and_sub_category: str #= Field(...)
    customers_who_bought_this_item_also_bought: str #= Field(...)
    description: str # = Field(...)
    product_information: str #= Field(...)
    product_description: str #= Field(...)
    items_customers_buy_after_viewing_this_item: str #= Field(...)
    customer_questions_and_answers: str #= Field(...)
    customer_reviews: str #= Field(...)
    sellers: str #= Field(...)

    #class Config:
     #   schema_extra = {
      #      "example": {
       #         "uniq_id": "A unique identifier",
        #        "product_name": "Santa's Express train",
        #        "manufacturer": "Hornby",
        #        "price": "£9.5",
        #        "number_available_in_stock":"5 new",
        #        "number_of_reviews":"12",
        #        "number_of_answered_questions":"2",
        #        "average_review_rating":"3.9 out of 5 stars",
        #        "amazon_category_and_sub_category":"Hobbies > Model Trains & Railway Sets > Rail Vehicles > Trains",
        #        "customers_who_bought_this_item_also_bought":"No data",
        #        "description":"Hornby 00 Gauge BR Hawksworth 3rd Class W 2107 W # R4410A",
        #        "product_information":"Technical Details Item Weight159 g Product Dimensions18.4 x 10.2 x 6 cm Manufacturer recommended age:4 years and up Item model numberR3211 Scale1::76 Track Width/GaugeOO Batteries Included?No    Additional Information ASINB00DCWY64Y Best Sellers Rank 84,256 in Toys & Games (See top 100) #108 in Toys & Games > Model Trains & Railway Sets > Rail Vehicles > Trains Shipping Weight159 g Delivery Destinations:Visit the Delivery Destinations Help page to see where this item can be delivered. Date First Available12 Jun. 2013    Feedback  Would you like to update product info or give feedback on images?",
        #        "product_description":"Hornby 00 Gauge BR Hawksworth 3rd Class W 2107 W # R4410A",
        #        "items_customers_buy_after_viewing_this_item":"http://www.amazon.co.uk/Train-Flash-Electric-Sound-Europe/dp/B008D7CEH4 | http://www.amazon.co.uk/13-Piece-Train-Set-Ideal/dp/B0173N6E4W",
        #        "customer_questions_and_answers":"can you turn off sounds // hi no you cant turn sound off",
        #        "customer_reviews":"Four Stars // 4.0 // 18 Dec. 2015 // By kenneth bell on 18 Dec. 2015 // Very happy with the communication with funkybuys | Five Stars // 5.0 // 14 Jan. 2016 // By moosixty",
        #        "sellers":"{'seller'=>[{'Seller_name_1'=>'Amazon.co.uk', 'Seller_price_1'=>'£3.42'}, {'Seller_name_2'=>'**stop-&-shop-uk**', 'Seller_price_2'=>'£0.19'}, {'Seller_name_3'=>'World Wide Shopping Mall Ltd', 'Seller_price_3'=>'£9.99'}, {'Seller_name_4'=>'MyHobbyStore Retail', 'Seller_price_4'=>'£8.00'}, {'Seller_name_5'=>'francejouet', 'Seller_price_5'=>'£37.62'}]}"

        #    }
       # }

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

def ErrorResponseModel(error, code, messae):
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


