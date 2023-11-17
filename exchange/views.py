import os
from decimal import *

from django.shortcuts import render
import requests
from dotenv import load_dotenv



load_dotenv()


API_KEY = os.getenv("API_KEY")

API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"


def exchange(request):
	response = requests.get(API_URL).json()
	currencies = response.get("conversion_rates")
 
	if request.method == "GET":
		context = {
			"currencies": currencies
		}
		return render(request=request, template_name="app/index.html", context=context)

	if request.method == "POST":
		from_amount = float(request.POST.get("from-amount"))
		from_curr = request.POST.get("from-curr")
		to_curr = request.POST.get("to-curr")

		converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)

		context = {
			"from_amount": from_amount,
			"from_curr": from_curr,
			"to_curr": to_curr,
			"currencies":currencies,
			"converted_amount": converted_amount,
		}
		return render(request=request, template_name="app/index.html", context=context)
