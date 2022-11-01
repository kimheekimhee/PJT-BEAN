from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.main, name='index'),
    path('hotlist', views.hotlist, name='hotlist'),
    path('<int:pk>', views.hotdetail, name='hotdetail'),
    path('hotcreate', views.hotcreate, name='hotcreate'),
    path('<int:pk>/reviewcreate', views.reviewcreate, name='reviewcreate'),
    path('<int:pk>/delete', views.delete, name='delete'),
]