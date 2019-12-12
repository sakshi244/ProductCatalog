from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ..Controller.ProductController import ProductController

import json

@csrf_exempt
@require_http_methods(["POST"])
def insert_new_product(request):
    try:
        json_data = json.loads(str(request.body, encoding='utf-8'))

        if not 'name' in json_data or not 'brand' in json_data or 'categories' not in json_data or 'images' not in json_data:
            return HttpResponse("Required data not found", status=400)

        name = json_data['name']
        brand = json_data['brand']
        categories = json_data['categories']
        images = json_data['images']

        if not isinstance(name, str) or not isinstance(brand, str) or not isinstance(categories, list) or not isinstance(images, list):
            return HttpResponse("Invalid data format", status=400)

        product_id = ProductController.insert_new_product(name, brand, categories, images)

        return JsonResponse({
            'product_id': product_id
        }, status=200)
    except Exception as e:
        return HttpResponse(status=500)
