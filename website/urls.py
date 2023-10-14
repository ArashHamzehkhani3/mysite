
from django.urls import path
from website.views import index,about

urlpatterns = [
    path('',index),
    path('About',about)
    
]
