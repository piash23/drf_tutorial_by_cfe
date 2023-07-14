from django.http import HttpResponse, JsonResponse
import json


def api_home(request):
    # receive json data
    body = request.body  # byte string of json data
    data = {}
    try:
        data = json.loads(body)  # convert byte string to dictionary
    except:
        pass
    print(data)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    # url query parameters catching in django
    print(request.GET)

    data['query_params'] = dict(request.GET)
    return JsonResponse(data)
