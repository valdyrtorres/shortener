from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)

	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "kirr.io",
			"form": the_form
		}
		return render(request, "shortener/home.html", context)
		#return render(request, "shortener/home.html", { "title": "Submit URL" })

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "Kirr.co",
			"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():			
			new_url = form.cleaned_data.get("url")
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		return render(request, template, context)

class URLRedirectView(View): #class based view
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count()!=1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
		