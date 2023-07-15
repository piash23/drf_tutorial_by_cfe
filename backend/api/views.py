from django.http import HttpResponse, JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['title', 'content', 'price'])

    print(data)
    return JsonResponse(data)
    # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'Content-Type': 'application/json'})
