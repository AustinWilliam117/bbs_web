from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/blog/
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type'),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name='blog_with_date'),
    path('blog_create/', views.blog_create, name='blog_create'),
    path('blog_delete/<int:id>/', views.blog_delete, name='blog_delete'),
    path('blog_update/<int:id>/', views.blog_update, name='blog_update'),
]