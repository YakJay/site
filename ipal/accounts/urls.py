from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^services/$',views.services),
    url(r'^about/$',views.about),
    url(r'^contact/$',views.contact),
    url(r'^tutorials/$',views.tutorials),
    url(r'^blog/$',views.blog),
   # url(r'^base/$',views.base),
  # url('accounts/', include('django.contrib.auth.urls')),
    ]