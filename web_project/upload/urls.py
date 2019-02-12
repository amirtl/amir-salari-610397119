from django.contrib import admin
from django.urls    import path
from .              import views

urlpatterns = [  
    path(''                               , views.upload),
    path('edit/<int:id>/'                 , views.edit) ,
    path('edit/<int:id>/resize/'          , views.resize),
    path('edit/<int:id>/crop/'            , views.crop),
    path('edit/<int:id>/rotate/'          , views.rotate),
    path('edit/<int:id>/black-and-white/' , views.black_and_white),
    path('edit/<int:id>/success/'         , views.share)
]

