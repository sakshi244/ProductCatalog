from ..Model.ProductDetails import ProductDetails
from ..Model.ProductCategories import ProductCategories
from ..Model.ProductImages import ProductImages


class ProductController:

    @staticmethod
    def get_products(brands, categories):
        if len(brands) > 0:
            temp_result = ProductDetails.objects.filter(product_brand__in=brands)
        else:
            temp_result = ProductDetails.objects.all()
        product_ids_containing_brands = list(map(lambda x: x.product_id, temp_result))

        if len(categories) > 0:
            temp_result = ProductCategories.objects.values('product_id').filter(category__in=categories).distinct()
        else:
            temp_result = ProductCategories.objects.values('product_id').all().distinct()

        product_ids_containing_categories = list(map(lambda x: x['product_id'], temp_result))

        product_ids = list(set(product_ids_containing_brands) & set(product_ids_containing_categories))

        product_details = ProductDetails.objects.filter(product_id__in=product_ids)
        product_categories = ProductCategories.objects.filter(product_id__in=product_ids)
        product_images = ProductImages.objects.filter(product_id__in=product_ids)

        result = {}
        for ind in range(len(product_details)):
            result[product_details[ind].product_id] = {
                'name': product_details[ind].product_name,
                'brand': product_details[ind].product_brand,
                'categories': [],
                'images': []
            }
        for ind in range(len(product_categories)):
            result[product_categories[ind].product_id]['categories'].append(product_categories[ind].category)
        for ind in range(len(product_images)):
            result[product_images[ind].product_id]['images'].append(product_images[ind].image_url)

        return result


    @staticmethod
    def add_new_product_categories(product_id, categories):
        for ind in range(len(categories)):
            ProductCategories.create(product_id, categories[ind])

    @staticmethod
    def add_new_product_images(product_id, images):
        for ind in range(len(images)):
            ProductImages.create(product_id, images[ind])

    @staticmethod
    def insert_new_product(name, brand, categories, images):
        product_id = ProductDetails.create(name, brand)
        ProductController.add_new_product_categories(product_id, categories)
        ProductController.add_new_product_images(product_id, images)
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

    @staticmethod
    def update_product(product_id, name, brand, categories, images):

        product_details = ProductDetails.objects.filter(product_id=product_id)[:1]
        if len(product_details) == 0:
            return False

        if categories:
            ProductController.delete_from_product_categories(product_id)
            ProductController.add_new_product_categories(product_id, categories)
        if images:
            ProductController.delete_from_product_images(product_id)
            ProductController.add_new_product_images(product_id, images)

        if name:
            product_details[0].product_name = name
        if brand:
            product_details[0].product_brand = brand
        product_details[0].save()
        return True
