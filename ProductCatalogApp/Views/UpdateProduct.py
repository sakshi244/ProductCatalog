from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ..Controller.ProductController import ProductController

import json

@csrf_exempt
@require_http_methods(["POST"])
def update_product(request):
    try:
        json_data = json.loads(str(request.body, encoding='utf-8'))

        if not 'product_id' in json_data:
            return HttpResponse("Required data not found", status=400)

        product_id = json_data['product_id']

        if not isinstance(product_id, int):
            return HttpResponse("Invalid data format", status=400)

        name = None
        brand = None
        categories = None
        images = None

        if 'name' in json_data:
            name = json_data['name']
            if not isinstance(name, str):
                return HttpResponse("Invalid data format", status=400)

        if 'brand' in json_data:
            brand = json_data['brand']
            if not isinstance(brand, str):
                return HttpResponse("Invalid data format", status=400)

        if 'categories' in json_data:
            categories = json_data['categories']
            if not isinstance(categories, list):
                return HttpResponse("Invalid data format", status=400)

        if 'images' in json_data:
            images = json_data['images']
            if not isinstance(images, list):
                return HttpResponse("Invalid data format", status=400)

        status = ProductController.update_product(product_id, name, brand, categories, images)

        if not status:
            return HttpResponse("Product not found", status=404)
        else:
            return HttpResponse("Updated successfully", status=200)
    except Exception as e:
        return HttpResponse(status=500)
