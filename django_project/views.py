from django.http import response
from django.shortcuts import render
import requests

def index(request):
  response1 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London,uk&')
  data = response1.json()
  Weathermessage = data['message']

  # response2 = requests.get('https://random.responsiveimages.io/')
  # data2 = response2.json()
  # Image1 = data2['image']
  return render(request, 'template/index.html', {'Weathermessage': Weathermessage})