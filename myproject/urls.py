"""myproject URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .routers import router
from django.views.generic import TemplateView
from users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('usuario', TemplateView.as_view(template_name='indexUser.html')),
    path('reportes', TemplateView.as_view(template_name='reportes.html')),
    path('formulario', TemplateView.as_view(template_name='indexFormulario.html')),
    path('respuesta', TemplateView.as_view(template_name='indexRespuesta.html')),
    path('',users_view.login_view, name='login'),
    path('users/logout',users_view.logout_view, name='logout'),
    path('users/signup',users_view.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
