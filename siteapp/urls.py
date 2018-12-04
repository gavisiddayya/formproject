from django.conf.urls import url
from siteapp import views

urlpatterns=[
    url(r'^registration$',views.userRegistration),
    url(r'^login$',views.userLogin),
    url(r'^dashboard',views.dashboard),
    url(r'^logout$',views.userLogout)
]