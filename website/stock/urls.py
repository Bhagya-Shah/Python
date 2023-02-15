from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('stock/', views.stock, name='stock'),
    path('adddata/',views.adddata,name='adddata'),
    path('trades/',views.trades,name='trades'),
    path('viewcode/',views.viewcode,name='viewcode'),
    path('stock/details/<int:id>', views.details, name='details'),
    path('viewcode/codes/<str:code>', views.codes, name='codes'),
    path('viewcode/netpos/<str:code>', views.netpos, name='netpos'),
]