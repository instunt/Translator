from django.urls import include, path
from . import views

urlpatterns = [         
    #url(r'[Cc]eny', views.ceny, name='ceny'),   
    path(r'', views.main, name='main'),
    path('<int:page>/', views.main_pages, name="main_pages"), 
]
                                                       