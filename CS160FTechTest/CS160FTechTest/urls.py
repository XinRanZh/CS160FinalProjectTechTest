"""CS160FTechTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from CS160FTechTest import BackendMySQL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_api', BackendMySQL.test_api, name='test_api'),
    path('login', BackendMySQL.login, name='login'),
    path('register', BackendMySQL.register, name='register'),
    path('uploadText', BackendMySQL.uploadText, name = "uploadText"),
    path('getText', BackendMySQL.getText, name = "getText")
]
