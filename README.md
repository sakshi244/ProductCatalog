# Product Catalog

###Project setup

Install MySql on your local machine. Keep user name as `root` and password as `password`. If different username or password has been setup for MySql then change it in ProductCatalog/settings.py file.

Run all the commands present in Database_Tables.sql file to setup the database

Install python3 for this project.

Create virtual environment `python3 -m venv  ProductCatalogEnv`

Enter into virtual environment `. ProductCatalogEnv/bin/activate`

Do all the stuff inside this virtual environment only.

Install all the pip packages using command `pip install -r requirements.txt`

If you install new pip package then do run the command `pip freeze > requirements.txt` to add that package to requirements.txt file

To start the server on PORT 5000 run command `python manage.py runserver 0.0.0.0:5000`

#### Sample cURLs for all the APIs

**Insert new product**

```buildoutcfg
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "name": "Printed man Hooded Sweatshirt",
  "brand": "Puma",
  "categories": ["Hoody", "Sweatshirt"],
  "images": ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq7aFUlrCycNsNjJ1915r_amWp5sJVTR5RHRdpRsB4RCZQiSHZeQ&s]
}' \
 'http://127.0.0.1:5000/insert_new_product/'
```

Insert product requires name, brand, categories and images as compulsory parameters. On successful creation of product it will return a product_id.


**Delete product**

```buildoutcfg
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "product_id": 3
}' \
 'http://127.0.0.1:5000/delete_product/'
```

Delete product requires the id of product that needs to be deleted

**Update product**

```buildoutcfg
curl -i -X POST \
   -H "Content-Type:application/json" \
   -d \
'{
  "product_id": 1,
  "name": "2",
  "brand": "b2",
  "categories": ["c1", "c2", "c3"],
  "images": ["i1", "i2"]
}' \
 'http://127.0.0.1:5000/update_product/'
```

Update product requires product id whose content needs to be updated along with parameters that needs to be updated. If we only pass name along with the product_id then only name corresponding to that product will get updated and all the other fields will remain unchanged.


***Get product details***

```buildoutcfg
curl -i -X GET \
 'http://127.0.0.1:5000/get_products/'
```

Above API will return all the products present in database without applying any filters

```buildoutcfg
curl -i -X GET \
 'http://127.0.0.1:5000/get_products/?category=c1&category=c3'
```

Above API will return all the products that lies in either category c1 or category c3. We can pass any number of categories in query params and it will return all the products that lie in one of the categories.

```buildoutcfg
curl -i -X GET \
 'http://127.0.0.1:5000/get_products/?brand=b1&brand=b2'
```

Above API will return all the products that lies in either brand b1 or brand b2. We can pass any number of brands in query params and it will return all the products that lie in one of the brand.

```buildoutcfg
curl -i -X GET \
 'http://127.0.0.1:5000/get_products/?category=c1&category=c2&brand=b1&brand=b2'
```

Above API will return all the products that are either of brand b1 or brand b2 and have atleast one category of c1 or c2. In this case also we can pass any number of brands and categories in query params and it will return all the products that are from one of the mentioned brand and also lie in atleast one of the mentioned category. 