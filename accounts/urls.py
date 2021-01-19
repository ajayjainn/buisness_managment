from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('account/<int:id>',views.account,name='account'),
    path('account/<int:id>/update',views.update),
    path('newCustomer',views.newCustomer,name='newCustomer'),
    path('saveCustomer',views.saveCustomer,name='saveCustomer'),
    path('data',views.data,name='data')

]