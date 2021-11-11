from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('searchbooks', views.searchbooks, name='search'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist_add/<int:book_id>', views.wishlist_add, name='wishlist_add'),
    path('wishlist_remove', views.wishlist_remove, name='wishlist_remove'),
]
