from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.main, name="index"),
    path("<int:pk>/hotlist", views.hotlist, name="hotlist"),
    path("<int:pk>", views.hotdetail, name="hotdetail"),
    path("<int:pk>/hotcreate", views.hotcreate, name="hotcreate"),
    path("<int:pk>/reviewcreate", views.reviewcreate, name="reviewcreate"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("<int:pk>/reviewcreate", views.reviewcreate, name="reviewcreate"),
    path("<int:pk>/hotupdate", views.hotupdate, name="hotupdate"),
    path("<int:review_pk>/likes", views.likes, name="likes"),
]
