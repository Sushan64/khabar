from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from . import models
from . import scrapers

# Create your views here.
        
def home(request):
  scrapers.ok_news_scrap()
  return HttpResponse("Server Working")