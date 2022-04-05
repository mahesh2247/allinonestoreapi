# allinonestoreapi

AllinOneStoreAPI is an API developed to calculate total payable price of input of grocery items in JSON format simulating a store counter machine which is deployed on the heroku cloud.
The API computational logic for the input is as follows :
-	5% on medicines and Food
-	5% on clothes below 1000 INR and 12% above 1000INR purchase
-	3% on music cds/dvds
-	Flat 18% on the imported commodities.
-	Books are exempted from tax.
-	On every purchase I get a receipt that has the below information :
-	Date and Time of purchase
-	List of commodities, each with their final price, tax amount with the applicable rate
-	Total amount payable
-	Additionally, a 5% discount is applied by the store if the bill exceeds 2000INR. 
-	The bill is sorted in the ascending order of the commodity names.

In order to run the API remotely, go to https://reqbin.com/curl and run the following test case with respect to API deployed on heroku - 

curl --location --request POST 'https://allinonestoreapi.herokuapp.com/processjson' \
--header 'Content-Type: application/json' \
--data-raw '[{
       "item": "Headache pills",
       "itemCategory": "Medicine",
       "quantity": 5,
       "price": 50
   },
   {
       "item": "Sandwich",
       "itemCategory": "Food",
       "quantity": 2,
       "price": 200
   },
   {
       "item": "Perfume",
       "itemCategory": "Imported",
       "quantity": 1,
       "price": 4000
   },
   {
       "item": "Black Swan",
       "itemCategory": "Book",
       "quantity": 1,
       "price": 300
   }
]
'

On the right side of the screen check HTML output from the HTML tab.


This API can also be run on Postman Locally. Clone the entire repository and run from localhost. Open postman select body>raw>JSON and provide the input in JSON format and run from Postman using POST request.


