from django.contrib                  import admin
from django.urls                     import path , include
from .                               import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static         import static
from django.conf                     import settings


urlpatterns = [
    path('delete/<int:id>/' , views.delete),
    path('admin/'           , admin.site.urls),
    path('admin_photos/'    , views.admin_photos),
    path('accounts/'        , include('accounts.urls')),
    path('upload/'          , include('upload.urls')) ,
    path('shared_photos/'   , include('shared_photos.urls')),
    path(''                 , views.homepage)
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()