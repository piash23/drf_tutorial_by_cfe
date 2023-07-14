from django.http import HttpResponse, JsonResponse


def api_home(request):
    return JsonResponse({"message": "Hello, world. You're at the api index."})
