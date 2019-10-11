"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    Para resolver mais duvidas entre a versao atual e as antigas veja
    https://stackoverflow.com/questions/47947673/is-it-better-to-use-path-or-url-in-urls-py-for-django-2-0
"""
from django.contrib import admin
from django.urls import path, re_path

from shortener.views import kirr_redirect_view, KirrCBView

# DO NOT DO
#from shortener import views
#from another_app.views import views

# Caso os padroes abaixo nao respondam como desejado, mude para re_path
# Siga o link abaixo para melhor entendimento e exemplos
#https://www.codingforentrepreneurs.com/blog/common-regular-expressions-for-django-urls

urlpatterns = [
    path('new_admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls), #old versions
    #path('view-1/', kirr_redirect_view),
    #path('view-2/', KirrCBView.as_view()),

    # DO NOT DO
    #url(r'^abc/$', 'shortener.views.kirr_redirect_view')
    #path('abc/', 'shortener.views.kirr_redirect_view')
    #path('abc/', 'views.kirr_redirect_view')

    re_path(r'^a/(?P<shortcode>[\w-]+)/$', kirr_redirect_view),
    re_path(r'^b/(?P<shortcode>[\w-]+)/$', KirrCBView.as_view()),
]
