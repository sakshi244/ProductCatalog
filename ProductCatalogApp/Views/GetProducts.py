from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ..Controller.ProductController import ProductController

@csrf_exempt
@require_http_methods(["GET"])
def get_products(request):
    try:

        categories = request.GET.getlist('category')
        brands = request.GET.getlist('brand')

        result = ProductController.get_products(brands, categories)

        result = list(map(lambda key: {**result[key], **{'product_id': key}}, result))

        return JsonResponse({
            'result': result
        }, status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
