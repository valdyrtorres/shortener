from django.contrib import admin
from django.urls import path, re_path

from django.conf.urls import url

from shortener.views import HomeView, URLRedirectView
# DO NOT DO
#from shortener import views
#from another_app.views import views

# Caso os padroes abaixo nao respondam como desejado, mude para re_path
# Siga o link abaixo para melhor entendimento e exemplos
#https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('exemplo/', HomeView.as_view()),
    re_path(r'^$', HomeView.as_view()),
    re_path(r'(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),

]
