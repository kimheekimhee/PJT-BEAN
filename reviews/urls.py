from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.main, name="index"),
    path("<int:pk>/hotlist", views.hotlist, name="hotlist"),
    path("<int:pk>", views.hotdetail, name="hotdetail"),
    path("<int:pk>/hotcreate", views.hotcreate, name="hotcreate"),
    path("<int:pk>/reviewcreate", views.reviewcreate, name="reviewcreate"),
    path("<int:pk>/reviewdelete", views.reviewdelete, name="reviewdelete"),
    path("<int:pk>/hotupdate", views.hotupdate, name="hotupdate"),
    path("<str:slug>/hotlist", views.hotlist_theme, name="hotlist_theme"),
    path("<int:pk>/reviewupdate", views.reviewupdate, name="reviewupdate"),
    path("<int:pk>/like", views.like, name="like"),
]
