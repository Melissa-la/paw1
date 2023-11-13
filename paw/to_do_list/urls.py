from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("login" , views.login_view , name="login"),
    path("logout" , views.logout_view , name="logout"),
    path("signin" , views.signin , name="signin"),
    path("add" ,views.add  , name="add"),
    path("delete/<int:id>" ,views.delete , name="delete"),

]