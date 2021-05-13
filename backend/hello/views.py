from django.shortcuts import render
import re
import requests
import json
from django.http import HttpResponse,JsonResponse

API_KEY = "AQEyhmfxLI3MaBFLw0m/n3Q5qf3VaY9UCJ14XWZE03G/k2NFitRvbe4N1XqH1eHaH2AksaEQwV1bDb7kfNy1WIxIIkxgBw==-y3qzswmlmALhxaVPNjYf74bqPotG12HroatrKA066yE=-W+t7NF;s4}%=kUSD"
HEADER = {
    "Access-Control-Allow-Origin": "*", 
    "Content-Type": "application/json", 
    "Access-Control-Allow-Methods": "POST",
    "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
}

def getPaymentMethodList(request):
    Request_URL = "https://checkout-test.adyen.com/v66/paymentMethods"
    Request_Header = {"Content-Type": "application/json", "x-api-key": API_KEY}
    if request.method == "POST":
        Request_body = json.loads(request.body)
        DATA = {
            "countryCode": "CN",
            "shopperLocale": "zh-CN",
            **Request_body,
            "channel": "Web",
            "merchantAccount": "AdyenRecruitmentCOM"
        }
    else:
        DATA = {}
    
    Adyen_Response = requests.post(url=Request_URL, headers=Request_Header, data=json.dumps(DATA))
    # responseData = json.loads(Adyen_Response.text)
    response = HttpResponse(headers=HEADER)
    response.write(Adyen_Response.text)
    return response

def createPayment(request):
    Request_URL = "https://checkout-test.adyen.com/v66/payments"
    Request_Header = {"Content-Type": "application/json", "x-api-key": API_KEY}
    if request.method == "POST":
        Request_body = json.loads(request.body)
        DATA = {
            "reference": "1234567",
            **Request_body,
            "returnUrl": "http://localhost:8000/success.html",
            "merchantAccount": "AdyenRecruitmentCOM"
        }
    else:
        DATA = {}
    
    Adyen_Response = requests.post(url=Request_URL, headers=Request_Header, data=json.dumps(DATA))
    response = HttpResponse(headers=HEADER)
    response.write(Adyen_Response.text)
    return response


def createPayment3D(request):
    Request_URL = "https://checkout-test.adyen.com/v66/payments"
    Request_Header = {"Content-Type": "application/json", "x-api-key": API_KEY}
    if request.method == "POST":
        Request_body = json.loads(request.body)
        DATA = {
            "reference": "1234567",
            "channel": "Web",
            **Request_body,
            "origin": "http://localhost:8000",
            "returnUrl": "http://localhost:8000/success.html",
            "merchantAccount": "AdyenRecruitmentCOM"
        }
    else:
        DATA = {}
    
    Adyen_Response = requests.post(url=Request_URL, headers=Request_Header, data=json.dumps(DATA))
    response = HttpResponse(headers=HEADER)
    response.write(Adyen_Response.text)
    return response