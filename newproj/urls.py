"""newproj URL Configuration

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
from django.urls import path,include
from django.conf import settings
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    #auth
    path('signup/', views.signupuser,name='signupuser'),
    path('signin/', views.signinuser,name='signinuser'),

    path('student_views/', views.student_views,name='student_views'),
    path('faculty_views/', views.faculty_views,name='faculty_views'),
    path('admin_views/', views.admin_views,name='admin_views'),
    path('student/', views.student,name='student'),
    path('faculty/', views.faculty,name='faculty'),
    path('admin/', views.admin,name='admin'),



]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
