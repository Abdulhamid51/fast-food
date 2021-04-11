from django.shortcuts import render
from .models import *
from django.contrib import messages
import telepot
# Create your views here.

TOKEN_1='1624445233:AAHfqXF9fU9VpdRQBlLzSzJWaznrJYcrpNQ'
TOKEN_2='1605950313:AAGco0_-QtSgDIdOVJqXr8UxjrLv4r7P_bs'

my_id = 1257603816

def index(request):
	foods = Foods.objects.all()
	if request.method == 'POST':
		name = request.POST['first_name']
		surname = request.POST['last_name']
		number = request.POST['phone']
		date = request.POST['reserv_date']
		guest = request.POST['numb_guests']
		time_from = request.POST['time_from']
		time_to = request.POST['time_to']
		PlaceOrder.objects.create(
			name=name, 
			surname=surname, 
			number=number, 
			date=date,
			guest=guest,
			time_from=time_from,
			time_to=time_to,
			)
		bot=telepot.Bot(TOKEN_1)
		bot.sendMessage(my_id, f'Ismi: {name}\nFamilyasi: {surname}\nTel raqami: {number}\nSanasi: {date}\nMehmonlar soni: {guest}\n{time_from}dan-{time_to}gacha.')

	chefs = Chefs.objects.all()
	return render(request, 'index.html',{'foods':foods,'chefs':chefs})

def order(request):
	if request.method == 'POST':
		name = request.POST['first_name']
		surname = request.POST['last_name']
		number = request.POST['phone']
		OrderFood.objects.create(
			name=name, 
			surname=surname, 
			number=number,
			)
		bot=telepot.Bot(TOKEN_2)
		bot.sendMessage(my_id, f'Ismi: {name}\nFamilyasi: {surname}\nTel raqami: {number}')
	return render(request, 'order.html')