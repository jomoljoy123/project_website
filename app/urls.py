from django.urls import path
from . import views
urlpatterns=[
#     path("home/",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("registration/",views.registration,name="registration"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("course_new/", views.course_new, name="course_new")

    ]
