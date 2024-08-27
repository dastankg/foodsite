from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(40)(views.FoodHome.as_view()), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.FoodCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.FoodTag.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<int:pk>/', views.DeletePage.as_view(), name='delete_page'),
]



