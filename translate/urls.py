
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),
   # url(r'accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}), 
    path('admin/', admin.site.urls),
    path(r'', include('Translator.urls')),
]


