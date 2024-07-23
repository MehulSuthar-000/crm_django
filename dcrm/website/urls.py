from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('record/<int:pk>', views.recordDetail, name="record"),
    path('delete_record/<int:pk>', views.deleteRecord, name="delete-record"),
    path('add_record/', views.addRecord, name='add-record'),
    path('update_record/<int:pk>', views.updateRecord, name="update-record"),

]
