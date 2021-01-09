"""blogapp URL Configuration

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

urlpatterns = [
    # regex do path  https://docs.python.org/3/howto/regex.html
    path('admin/', admin.site.urls),
    # include bo ladujesz urle z aplikacji
    # namespace po to zeby odnosic sie do url blogow z mojej aplikacji np blog:post_details
    # https://docs.djangoproject.com/en/2.0/topics/http/urls/#url-namespaces.
    path('blog/', include('blog.urls', namespace='blog'))
]
