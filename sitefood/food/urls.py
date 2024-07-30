from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('post/<slug:post_slug>/', views.post, name='post'),
    path('category/<int:cat_id>/', views.show_categories, name='category'),
]
