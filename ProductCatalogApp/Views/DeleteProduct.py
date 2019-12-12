from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ..Controller.ProductController import ProductController

import json

@csrf_exempt
@require_http_methods(["POST"])
def delete_product(request):
    try:
        json_data = json.loads(str(request.body, encoding='utf-8'))

        if not 'product_id' in json_data:
            return HttpResponse("Required data not found", status=400)

        product_id = json_data['product_id']

        if not isinstance(product_id, int):
            return HttpResponse("Invalid data format", status=400)

        ProductController.delete_product(product_id)

        return JsonResponse({}, status=200)
    except Exception as e:
        return HttpResponse(status=500)
