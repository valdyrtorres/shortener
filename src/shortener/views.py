from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import KirrURL

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)

	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "shortener/home.html", {})

	def post(self, request, *args, **kwargs):
		#some_dict = {}
		#some_dict["url"] #error
		#some_dict.get("url", "http://spring.io") #None
		print(request.POST)
		print(request.POST["url"])
		print(request.POST.get("url"))
		return render(request, "shortener/home.html", {})

class KirrCBView(View): #class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
