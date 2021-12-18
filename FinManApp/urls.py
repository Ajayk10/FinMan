from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('jointaccount/', views.jointaccount, name = 'jointaccount'),
    path('inhand/', views.inhand, name = 'inhand'),
    path('csbaccount/', views.csbaccount, name = 'csbaccount'),
    path('pensionaccount/', views.pensionaccount, name = 'pensionaccount'),
    path('myaccount/', views.myaccount, name = 'myaccount'),
    #------------------------------------------------------------------------
    path('jointaccounttransaction/', views.jointaccounttransaction, name = 'jointaccounttransaction'),
    path('pensionaccounttransaction/', views.pensionaccounttransaction, name = 'pensionaccounttransaction'),
    path('csbaccounttransaction/', views.csbaccounttransaction, name = 'csbaccounttransaction'),
    path('myaccounttransaction/', views.myaccounttransaction, name = 'myaccounttransaction'),
    path('inhandtransaction/', views.inhandtransaction, name = 'inhandtransaction'),
    #-------------------------------------------------------------------------
    path('jointaccountstatement/', views.jointaccountstatement, name = 'jointaccountstatement'),
    path('pensionaccountstatement/', views.pensionaccountstatement, name = 'pensionaccountstatement'),
    path('csbaccountstatement/', views.csbaccountstatement, name = 'csbaccountstatement'),
    path('myaccountstatement/', views.myaccountstatement, name = 'myaccountstatement'),
    path('inhandstatement/', views.inhandstatement, name = 'inhandstatement'),
    #-------------------------------------------------------------------------
    path('jointaccountdetails/<JointAccountModel_id>', views.jointaccountdetails, name = 'jointaccountdetails'),
    path('pensionaccountdetails/<PensionAccountModel_id>', views.pensionaccountdetails, name = 'pensionaccountdetails'),
    path('myaccountdetails/<MyAccountModel_id>', views.myaccountdetails, name = 'myaccountdetails'),
    path('csbaccountdetails/<CSBAccountModel_id>', views.csbaccountdetails, name = 'csbaccountdetails'),
    path('inhanddetails/<InHandModel_id>', views.inhanddetails, name = 'inhanddetails'),
    #-------------------------------------------------------------------------
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('statistics/', views.statistics, name = 'statistics'),
    #-------------------------------------------------------------------------
    path('Hike/', views.hike, name = 'hike'),
    path('Todo/', views.Todo, name = 'Todo'),
    path('addgoal/', views.addgoal, name = 'addgoal'),
    path('accomplished/<TodoList_id>', views.accomplished, name = 'accomplished'),
    path('delete/<TodoList_id>', views.delete, name = 'delete'),
]
