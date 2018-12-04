from django.conf.urls import url
from testapp import views

urlpatterns=[
    url(r'^c_details$',views.practice_view)
]