from django.http import HttpResponse, JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    print(data)
    return JsonResponse(data)
