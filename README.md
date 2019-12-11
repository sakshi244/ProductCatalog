# Product Catalog

Create virtual environment `python3 -m venv  ProductCatalogEnv`

Enter into virtual environment `. ProductCatalogEnv/bin/activate`

Do all the stuff inside this virtual environment only.

Install all the pip packages using command `pip install -r requirements.txt`

If you install new pip package then do run the command `pip freeze > requirements.txt` to add that package to requirements.txt file

To start the server on PORT 5000 run command `python ProductCatalog/manage.py runserver 0.0.0.0:5000`