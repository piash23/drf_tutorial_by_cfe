from django.http import HttpResponse, JsonResponse
import json
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def api_home(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):

        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def api_home_for_get(request):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    print(data)
    return Response(data)
    # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'Content-Type': 'application/json'})
