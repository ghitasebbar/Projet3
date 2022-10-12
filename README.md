# Projet3: Base de données

### Objectifs
Ce repository contient les rendus du projet 3. L'objectif étant de créer une API qui requête des données depuis ue base de données préalablement peuplée.
Les données utilisées concernent une publication de produits de Amazon. Le schéma des données est le suivant: 
1. uniq_id
2. product_name,
3. manufacturer
4. price
5. number_available_in_stock
6. number_of_reviews
7. number_of_answered_questions
8. average_review_rating
9. amazon_category_and_sub_category
10. customers_who_bought_this_item_also_bought
11. description
12. product_information
13. product_description
14. items_customers_buy_after_viewing_this_item
15. customer_questions_and_answers
16. customer_reviews
17. sellers  
La descrition des colonnes est disponibles sur le site data.world. 

Nous avons travaillé avec MongoDB pour sauvegarder les données.

### Choix de la base de données
Les données que nous avons considérées sont des données descriptives de produits vendus sur Amazon. Tous les produits sont censés posséder les mêmes éléments. Vue la nature de l'activité qui génère ces données, certains lignes de données peuvent ne pas être renseignées telles les commentaires utilisateurs, les questions des utilisateurs ainsi que les notes données aux produits par les utilisateurs. Les produits peuvent donc ne pas contenir les mêmes élements dans la base. Nous avons donc choisi de passer sur une SGBD NoSQL.

### Requêtage de base de données
Nous avons utilisé FastAPI, la librairie PyMongo ainsi que la librairie AsyncIO de MongoDB.
FastAPI nous permet de créer les routes d'api à utiliser par les utilisateurs pour interagir avec la base de données.
PyMongo a été utilisé pour gérer le peuplement de la base de données.
Nous avons exploré l'utilisation de AsyncIO pour gérer les requêtes avec la base de données. Cette librairie est cencée gérer les requêtes avec la base de données d'une manière non bloquante.

### Fichiers
1. Le fichier setup.sh contient les commandes de création des images et conteneurs de peuplement de la base de données, de l'image et du conteneur de création de la base de données ainsi que l'API de requêtage de la base de données
2. Le ficher test_api_projet2.py contient les tests des différentes routes disponibles sur l'API
3. Le fichier server.py contient le code de définition des différentes routes de l'API
4. Le fichier my-api-deployement.yml pour le deploiment des pods
5. Les fihchier my-api-exposition.yml et my-api-exposition-ingress.yml pour l'exposition de l'api

### Utilisation de l'application
Lancer l'API:
>> chmod +x setup.sh    
>> sh setup.sh  

Vous pouvez tester et consulter la documentation de l'API sur http://0.0.0.0:8000/docs après lancement.  
Sur kubernetes il faudra au préalable créer un tunel ssh entre l'API et le port 8000 de votre machine.  

>> ssh -i "data_enginering_machine.pem" ubuntu@3.251.80.227 -fNL 8000:192.168.49.2:80

Et donc par la suite l'api s'ouvre sur le navigateur sur l'adresse  localhost:8000/docs.  
`Nota`: L'utilisation de l'API se fait par corps de requête

#### Routes

###### Lire `n`documents de la collection
>> curl -X 'GET' \
  'http://localhost:8000/read/document?n=2' \
  -H 'accept: application/json'

Réponse de l'api :

{
  "data": [
    [
      {
        "id": "6341f586bae80733eb130a20",
        "product_name": "Hornby 2014 Catalogue",
        "manufacturer": "Hornby",
        "price": "£3.42",
        "number_available_in_stock": "5 new",
        "number_of_reviews": "15",
        "number_of_answered_questions": 1,
        "average_review_rating": "4.9 out of 5 stars",
        "amazon_category_and_sub_category": "Hobbies > Model Trains & Railway Sets > Rail Vehicles > Trains",
        "customers_who_bought_this_item_also_bought": "http://www.amazon.co.uk/Hornby-R8150-Catalogue-2015/dp/B00S9SUUBE | http://www.amazon.co.uk/Hornby-Book-Model-Railways-Edition/dp/1844860957 | http://www.amazon.co.uk/Hornby-Book-Scenic-Railway-Modelling/dp/1844861120 | http://www.amazon.co.uk/Peco-60-Plans-Book/dp/B002QVL16I | http://www.amazon.co.uk/Hornby-Gloucester | http://www.amazon.co.uk/Airfix-5014429781902",
        "description": "Product Description Hornby 2014 Catalogue Box Contains 1 x one catalogue",
        "product_information": "Technical Details Item Weight640 g Product Dimensions29.6 x 20.8 x 1 cm Manufacturer recommended age:6 years and up Item model numberR8148 Main Language(s)English manual, English Number of Game Players1 Number of Puzzle Pieces1 Assembly RequiredNo Scale1:72 Engine Typeelectric Track Width/GaugeHO Batteries Required?No Batteries Included?No Material Type(s)Paper Material Care InstructionsNo Remote Control Included?No Radio Control Suitabilityindoor Colorwhite    Additional Information ASINB00HJ208KO Best Sellers Rank 52,854 in Toys & Games (See top 100) #69 in Toys & Games > Model Trains & Railway Sets > Rail Vehicles > Trains Shipping Weight640 g Delivery Destinations:Visit the Delivery Destinations Help page to see where this item can be delivered. Date First Available24 Dec. 2013    Feedback  Would you like to update product info or give feedback on images?",
        "product_description": "Product Description Hornby 2014 Catalogue Box Contains 1 x one catalogue",
        "items_customers_buy_after_viewing_this_item": "http://www.amazon.co.uk/Hornby-R8150-Catalogue-2015/dp/B00S9SUUBE | http://www.amazon.co.uk/Hornby-Book-Model-Railways-Edition/dp/1844860957 | http://www.amazon.co.uk/Peco-60-Plans-Book/dp/B002QVL16I | http://www.amazon.co.uk/Newcomers-Guide-Model-Railways-Step/dp/1857943295",
        "customer_questions_and_answers": "Does this catalogue detail all the previous Hornby products please? // HiThe 2014 catalogue does indeed detail previous models but also includes new releases for 2014.You would be advised to purchase models as you need them to avoid them being discontinued in subsequent years…\n    \n      see more\n    \n  \n  \n    HiThe 2014 catalogue does indeed detail previous models but also includes new releases for 2014.You would be advised to purchase models as you need them to avoid them being discontinued in subsequent yearsHope this helps\n    \n      see less",
        "customer_reviews": "Worth Buying For The Pictures Alone (As Ever) // 4.0 // 6 April 2014 // By\n    \n    Copnovelist\n  \n on 6 April 2014 // Part of the magic for me growing up as a boy was to buy (or be given) the new Hornby catalogue every year, even if it included 90% of the same products as the previous year.  I've still got my old ones dating back to the 70s and 80s somewhere.  These days the catalogue is especially informative in that it tells you the vintage of the rolling stock which is useful if you are dedicating your railway to one particular era and train company. | Amazing detail fabulous photography. // 5.0 // 11 April 2015 // By\n    \n    richard\n  \n on 11 April 2015 // Amazing detail, every credit to the photographer in this book, a worthy reference manual, as well as a sales brochure. even if you only have a passing interest in the hobby you will be transported to another time when we were all younger and in awe of the big trains. | 'Great Purchase' // 5.0 // 23 April 2014 // By\n    \n    Pinkhandbag\n  \n on 23 April 2014 // This was purchased on behalf of my Dad. He is always asking me to look up 00 gauge engines online, so this has been a good buy as he can look at it anytime. Would definitely buy the next one 2015!It arrived quickly and in perfect condition :-) | Great Catalogue // 5.0 // 11 Jun. 2014 // By\n    \n    Gary John Mapson\n  \n on 11 Jun. 2014 // Everything I really needed to see what was on offer from Hornby in the way of trains.  Would not have minded it included an RRP as well though | I collect them all as the glossy pictures are great and it is nice that you can still get ... // 5.0 // 7 Dec. 2014 // By\n    \n    David Baker\n  \n on 7 Dec. 2014 // I collect them all as the glossy pictures are great and it is nice that you can still get catalogs to collect. | Great catalogue // 5.0 // 20 Mar. 2015 // By\n    \n    John A. Day\n  \n on 20 Mar. 2015 // What a great book.  Extremely useful insight to all future christmas presents. | Useful // 5.0 // 7 Oct. 2014 // By\n    \n    T. Davies\n  \n on 7 Oct. 2014 // Useful info for someonelike me starting back into the hobby after many years | hornbys latest catalogue. // 5.0 // 1 Dec. 2014 // By\n    \n    John Butlin\n  \n on 1 Dec. 2014 // A well produced very good quality catalogue.Super quality pictures.",
        "sellers": "{\"seller\"=>[{\"Seller_name_1\"=>\"Amazon.co.uk\", \"Seller_price_1\"=>\"£3.42\"}, {\"Seller_name_2\"=>\"**stop-&-shop-uk**\", \"Seller_price_2\"=>\"£0.19\"}, {\"Seller_name_3\"=>\"World Wide Shopping Mall Ltd\", \"Seller_price_3\"=>\"£9.99\"}, {\"Seller_name_4\"=>\"MyHobbyStore Retail\", \"Seller_price_4\"=>\"£8.00\"}, {\"Seller_name_5\"=>\"francejouet\", \"Seller_price_5\"=>\"£37.62\"}]}"
      },
      {
        "id": "6341f586bae80733eb130a21",
        "product_name": "FunkyBuys® Large Christmas Holiday Express Festive Train Set (SI-TY1017) Toy Light / Sounds / Battery Operated & Smoke",
        "manufacturer": "FunkyBuys",
        "price": "£16.99",
        "number_available_in_stock": "N/A",
        "number_of_reviews": "2",
        "number_of_answered_questions": 1,
        "average_review_rating": "4.5 out of 5 stars",
        "amazon_category_and_sub_category": "Hobbies > Model Trains & Railway Sets > Rail Vehicles > Trains",
        "customers_who_bought_this_item_also_bought": "http://www.amazon.co.uk/Christmas-Holiday-Express-Festive-Train-Set-Toy/dp/B009R8S8AA | http://www.amazon.co.uk/Goldlok-Holiday-Express-Operated-Multi-Colour/dp/B009R8PAO2 | http://www.amazon.co.uk/FunkyBuys%C2%AE-Christmas-SI-TY1017-Ornaments-Operated/dp/B01437QMHA | http://www.amazon.co.uk/Holiday-Express-Christmas-Ornament-Decoration | http://www.amazon.co.uk/Seasonal-Vision-Christmas-Tree-Train/dp/B0044ZC1W2 | http://www.amazon.co.uk/Coca-Cola-Santa-Express-Train-Set/dp/B004BYSNU0",
        "description": "Size Name:Large FunkyBuys® Large Christmas Holiday Express Festive Train Set (SI-TY1017) Toy Light / Sounds / Battery Operated & Smoke",
        "product_information": "Technical Details Manufacturer recommended age:3 years and up Item model numberSI-TY1017-B    Additional Information ASINB01434AIRS Best Sellers Rank 169,625 in Toys & Games (See top 100) #261 in Toys & Games > Model Trains & Railway Sets > Rail Vehicles > Trains Delivery Destinations:Visit the Delivery Destinations Help page to see where this item can be delivered. Date First Available18 Aug. 2015   ",
        "product_description": "Size Name:Large FunkyBuys® Large Christmas Holiday Express Festive Train Set (SI-TY1017) Toy Light / Sounds / Battery Operated & Smoke",
        "items_customers_buy_after_viewing_this_item": "http://www.amazon.co.uk/Christmas-Holiday-Express-Festive-Train-Set-Toy/dp/B009R8S8AA | http://www.amazon.co.uk/Goldlok-Holiday-Express-Operated-Multi-Colour/dp/B009R8PAO2 | http://www.amazon.co.uk/FunkyBuys%C2%AE-Christmas-SI-TY1017-Ornaments-Operated/dp/B01437QMHA | http://www.amazon.co.uk/Holiday-Express-Christmas-Ornament-Decoration",
        "customer_questions_and_answers": "can you turn off sounds // hi no you cant turn sound off",
        "customer_reviews": "Four Stars // 4.0 // 18 Dec. 2015 // By\n    \n    kenneth bell\n  \n on 18 Dec. 2015 // Very happy with the communication with funkybuys | Five Stars // 5.0 // 14 Jan. 2016 // By\n    \n    moosixty\n  \n on 14 Jan. 2016 // Great buy.",
        "sellers": "{\"seller\"=>{\"Seller_name_1\"=>\"UHD WHOLESALE\", \"Seller_price_1\"=>\"£16.99\"}}"
      }
    ]
  ],
  "code": 200,
  "message": "Products retrieved successfully"
}

###### Ajouter un produit dans la collection 

>> curl -X 'POST' \
  'http://localhost:8000/add/document' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "uniq_id": "anewlyaddedproduct123456",
  "product_name": "Fashionista'\''s shoes",
  "manufacturer": "Fashionista",
  "price": "£13.4",
  "number_available_in_stock": "20 new",
  "number_of_reviews": 10,
  "number_of_answered_questions": 0,
  "average_review_rating": "3.2 out of 5 stars",
  "amazon_category_and_sub_category": "Women > Fashion > Shoes > High Heel",
  "customers_who_bought_this_item_also_bought": "N/A",
  "description": "A pair of high heels red shoes",
  "product_information": "N/A",
  "product_description": "N/A",
  "items_customers_buy_after_viewing_this_item": "N/A",
  "customer_questions_and_answers": "N/A",
  "customer_reviews": "N/A",
  "sellers": "N/A"
}'

Réponse de l'api : 

{
  "data": [
    {
      "id": "6341f74792acf7742fa3cfb3",
      "product_name": "Fashionista's shoes",
      "manufacturer": "Fashionista",
      "price": "£13.4",
      "number_available_in_stock": "20 new",
      "number_of_reviews": 10,
      "number_of_answered_questions": 0,
      "average_review_rating": "3.2 out of 5 stars",
      "amazon_category_and_sub_category": "Women > Fashion > Shoes > High Heel",
      "customers_who_bought_this_item_also_bought": "N/A",
      "description": "A pair of high heels red shoes",
      "product_information": "N/A",
      "product_description": "N/A",
      "items_customers_buy_after_viewing_this_item": "N/A",
      "customer_questions_and_answers": "N/A",
      "customer_reviews": "N/A",
      "sellers": "N/A"
    }
  ],
  "code": 200,
  "message": "Product add success."
}


