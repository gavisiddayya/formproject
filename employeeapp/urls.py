from django.conf.urls import url
from employeeapp  import views

urlpatterns=[
    url(r'^employee$',views.employee_view),
    url(r'^st$',views.staticExample),
]