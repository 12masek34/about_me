from django.urls import path
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('blogs/', blog_list),
    path('blogs/<int:pk>/', blog_detail),

]
urlpatterns = format_suffix_patterns(urlpatterns)