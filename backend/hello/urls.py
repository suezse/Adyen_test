from django.urls import path
from hello import views

urlpatterns = [
    path("getPaymentMethods", views.getPaymentMethodList, name="payment_methods"),
    path("createPayment", views.createPayment, name="create_payment"),
    path("createPayment2", views.createPayment2, name="create_payment2"),
    path("paymentDetails", views.paymentDetails, name="payment_details"),
]

