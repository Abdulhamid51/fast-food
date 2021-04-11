from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('',views.index, name='base'),
	path('order',views.order, name='order'),
]