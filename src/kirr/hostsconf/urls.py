from django.conf.urls import url

from .views import wildcard_redirect

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^(?P<path>.*)', admin.site.urls),
]    