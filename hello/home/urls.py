from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path('login',views.login,name="login"),
    path('logout_user',views.logout_user,name="logout_user"),
    path("new",views.new,name='new'),
    path("edit",views.edit,name='edit'),
    path("edit_internal",views.edit_internal,name='edit_internal'),
    path("update",views.update,name='update'),
    path("update_internal",views.update_internal,name='update_internal'),
    path("expired_edit",views.expired_edit,name='expired_edit'),
    path("expired_edit_internal",views.expired_edit_internal,name='expired_edit_internal'),
    path("expired_view_all",views.expired_view_all,name='expired_view_all'),
    path("billing",views.billing,name='billing'),
    path("PM",views.PM,name='PM'),
    path("view_all",views.view_all,name='view_all'),
]