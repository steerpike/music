"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from interest.views import dashboard, interest_view, interest_delete, tags_index, tag_detail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path("links/", include("interest.urls")),
    path('rss/', include('rss.urls')),
    path('interests/delete', interest_delete, name='interests_delete'),
    path('interests/', interest_view, name='interests'),
    path('tagged/<str:label>', tag_detail, name='tag_detail'),
    path("tagged/", tags_index, name="tags_index"),
]
