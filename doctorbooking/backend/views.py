from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from twilio.rest import Client

from doctorbooking import settings
from backend.utils import generate_otp

# class Index(APIView):
#     def get(self, request):
#         return Response({"Hello":"World"})
    
#     def post(self, request):
#         client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#         phone_number = request.POST.get("phone")
#         otp_code = "9875766"

#         message = client.messages.create(
#         to=phone_number,
#         from_=settings.TWILIO_FROM_NUMBER,
#         body=f"Your OTP for verification is: {otp_code}"
#     )
#         print("message.sid", message.sid, "\n")
#         return Response({"OTP" : "OTP sended successfully"})
    

# # Example function to send OTP

# def send_otp_sms(phone_number, otp_code):
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         to=phone_number,
#         from_=settings.TWILIO_FROM_NUMBER,
#         body=f"Your OTP for verification is: {otp_code}"
#     )
#     return message.sid

class Index(APIView):
    def get(self, request):
        return Response({"success":"Success"})
    