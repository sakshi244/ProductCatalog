from ..Model.ProductDetails import ProductDetails
from ..Model.ProductCategories import ProductCategories
from ..Model.ProductImages import ProductImages

class ProductController:

    @staticmethod
    def insert_new_product(name, brand, categories, images):
        product_id = ProductDetails.create(name, brand)
        for ind in range(len(categories)):
            ProductCategories.create(product_id, categories[ind])
        for ind in range(len(images)):
            ProductImages.create(product_id, images[ind])
        return product_id
