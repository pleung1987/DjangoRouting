from django.conf.urls import url, include
from . import views

print "got to apps.articles.urls file"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^articles/(?P<number>\d+)$', views.show),
    url(r'^articles/(?P<word>\w+)$', views.show_word),
    url(r'^articles/2003', views.special_case_2003),
    url(r'^articles/year/(?P<year>[0-9]{4})$', views.year_archive),
    url(r'^articles/year/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', views.month_archive)
]
