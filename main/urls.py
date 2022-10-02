"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core import views
from core.models import Produto
from core.views import index, information, login_user, login_submit, create_usuario, logout_user, registre, post, information
from django.conf import settings
from django.conf.urls.static import static
from core.views import  produto_submit
from core.views import  post, search
# from core.views import login_request, register_request, contato_request, perfil_request
from core.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('produto/', produto, name='produto'),
    path('produto/submit', produto_submit, name='produto_submit'),
    # path('login', login_user, name='login'),
    path('login/submit', login_submit, name='login_submit'),
    path('logout/', logout_user, name='logout'),
    # path('registre/', registre, name='registre'),
    path('registre/submit', create_usuario, name='create_usuario'),
    path('post/', post, name = 'post'),
    path('search/', search, name = 'search'),
    
    path('register/', register_request, name='register'),
    
    path('login', login_request, name='login'),
    path('contato', contato_request, name='contato'),
    # path('perfil', perfil_request, name='perfil'),

# ----------------------------------------------------------------
    path('perfil/<int:pk>/', view_perfil, name='perfil'),
    
    path('perfilEdit/<int:pk>/', view_perfilEdit, name='perfilEdit'),
    path('update_perfil/<int:pk>/', update_perfil, name='update_perfil'),
 


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
