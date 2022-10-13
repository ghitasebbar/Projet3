from pandas import read_csv
from pymongo import MongoClient

MONGO_INFO = "mongodb://root:root@mongodb:27017"

client = MongoClient(MONGO_INFO)

database = client.projet3

produits = database.get_collection("produits")

produits.create_index('uniq_id', unique = True)

# populate the database

data = read_csv('https://query.data.world/s/nhehnq4tng5e33afvgbtg32siakpac')

data[['price','manufacturer', 'number_available_in_stock', 'average_review_rating', 'amazon_category_and_sub_category', 'customers_who_bought_this_item_also_bought', 'description', 'product_information', 'product_description', 'items_customers_buy_after_viewing_this_item', 'customer_questions_and_answers', 'customer_reviews', 'sellers' ]] = data[['price','manufacturer', 'number_available_in_stock', 'average_review_rating', 'amazon_category_and_sub_category', 'customers_who_bought_this_item_also_bought', 'description', 'product_information', 'product_description', 'items_customers_buy_after_viewing_this_item', 'customer_questions_and_answers', 'customer_reviews', 'sellers' ]].fillna('N/A')

data_dict = data.to_dict("records")

produits.insert_many(data_dict)

