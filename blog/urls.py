from django.urls import path
from .views import *

urlpatterns = [
    path('', ListBlog.as_view(), name='list-blog'),
    path('<str:pk>', BlogDetail.as_view(), name='blog-detail'),
]
