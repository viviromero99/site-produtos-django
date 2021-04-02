from django.urls import path

from produto import views

app_name = 'produto'

urlpatterns = [
    path('shopAll/', views.shopAll, name='shopAll'),
    path('skincare/', views.skincare, name='skincare'),
    path('makeup/', views.makeup, name='makeup'),
    path('bath&body/', views.bathbody, name='bath&body'),
    path('fragrances/', views.fragrances, name='fragrances'),
]