from django.urls import path
from hello import views

urlpatterns = [
    path("getPaymentMethods", views.getPaymentMethodList, name="payment_methods"),
    path("createPayment", views.createPayment, name="create_payment"),
     path("createPayment3D", views.createPayment3D, name="create_payment_3D"),
]

