from django.urls import path

from .views import ContactView, CreateContact, AboutView


urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('feedback/', CreateContact.as_view(), name='feedback'),
    path('about/', AboutView.as_view(), name='about'),
]
