
from django.urls import path
from . import views
from project_blog.settings import *
from django.conf.urls.static import static


app_name = "app_blog"

urlpatterns = [
    path('', views.home, name='home')
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
#urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)


