from django.urls import path
import adminapp.views as adminapp
from adminapp.views import UsersListView, UserCreateView, UserUpdateView, UserDeleteView, CategoriesListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductCreateView, ProductListView, ProductReadListView, \
    ProductUpdateView, ProductDeleteView


app_name = 'adminapp'

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/read/', UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', CategoriesListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', ProductCreateView.as_view(), name='product_create'),
    path('products/read/category/<int:pk>/', ProductListView.as_view(), name='products'),
    path('products/read/<int:pk>/', ProductReadListView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
