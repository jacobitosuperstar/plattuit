"""plattuit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import (
    path,
    include,
)
from django.conf import settings
from django.conf.urls.static import static

# VIEWS IMPORTED DIRECTLY FROM THE ACCOUNT APP #
from account.views import (
    registration_view,
    logout_view,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

]

# account views
urlpatterns += [
    # USER REGISTRATION/CREATION VIEWS ##
    path('register/', registration_view, name='register'),

    # CUSTOM LOG OUT VIEW ##
    path('logout/', logout_view, name='logout'),

    # CUSTOM LOG IN VIEW ##
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='account/login.html'),
        name='login',
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
