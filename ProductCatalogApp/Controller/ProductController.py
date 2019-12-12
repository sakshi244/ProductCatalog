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

    @staticmethod
    def delete_from_product_categories(product_id):
        ProductCategories.objects.filter(product_id=product_id).delete()

    @staticmethod
    def delete_from_product_images(product_id):
        ProductImages.objects.filter(product_id=product_id).delete()

    @staticmethod
    def delete_from_product_details(product_id):
        ProductDetails.objects.filter(product_id=product_id).delete()

    @staticmethod
    def delete_product(product_id):
        ProductController.delete_from_product_categories(product_id)
        ProductController.delete_from_product_images(product_id)
        ProductController.delete_from_product_details(product_id)
