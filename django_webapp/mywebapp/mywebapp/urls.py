"""mywebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #blog related urls
    path('admin/', admin.site.urls),
    path('', blog_views.PostListView.as_view(), name='home-page'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='postdetail-page'),
    path('post/new/', blog_views.PostCreateView.as_view(), name='postcreate-page'),
    path('post/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='postupdate-page'),
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='postdelete-page'),
    path('about/', blog_views.about, name='about-page'),
    #Profile related Urls
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    path('register/', user_views.register, name='register-page'),
    path('profile/', user_views.profile, name='profile-page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


