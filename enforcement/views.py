from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def book(request):
    data = dict()
    if request.method == 'POST':
        if request.POST:
            payload = request.POST
        else:
            payload = json.loads(request.body) 
        print(payload)
        data['status'] = True
        data['message'] = "{0} was booked successfully".format(payload['rrr'])
    else:
        data['status'] = False
        data[''] = "Method Not Allowed"
    return JsonResponse(data)


@csrf_exempt
def payment(request):
    data = dict()
    if request.method == 'POST':
        if request.POST:
            payload = request.POST
        else:
            payload = json.loads(request.body)
        print(payload)
        data['status'] = True
        data['message'] = "{0} was paid successfully".format(payload['rrr'])
    else:
        data['status'] = False
        data['message'] = "Method Not Allowed"
    return JsonResponse(data)
