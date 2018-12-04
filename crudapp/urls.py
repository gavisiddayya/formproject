from django.conf.urls import url
from crudapp import views

urlpatterns=[
    url(r'^create$',views.create),
    url(r'^update$',views.update),
    url(r'^index$',views.index),
    url(r'^view$',views.view),
    url(r'^delete$',views.delete)
]