from django.conf.urls import url
from studentapp import views

urlpatterns=[
    url(r'^student$',views.student_view),
]