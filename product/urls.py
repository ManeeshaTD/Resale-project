from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('' , views.productlist , name='product_list') , 
    path('chat/<int:slug>/', views.chat, name='chat'),
    path('chat-get/<int:slug>/<int:chat_id>/', views.chat, name='chat_get'),
    path('my-chat/', views.my_chat, name='my-chat'),
    path('main-chat-user/<int:pid>/', views.main_chat_user, name='main-chat-user'),
    path('<slug:category_slug>' , views.productlist , name='product_list_category') , 
    path('detail/<slug:product_slug>' , views.productdetail , name='product_detail'),
    path('check-for-new-objects/<int:chat_pid>/' , views.check_for_new_objects , name='check_for_new_objects'),
    path('load-new-messages/<int:chat_id>/' , views.load_new_messages , name='load_new_messages'),
    path('admin_index_olx/', views.admin_index_olx, name='admin_index_olx'),
    path('user_detail_olx/', views.user_detail_olx, name='user_detail_olx'),
    path('delete_user_olx/<int:pid>/', views.delete_user_olx, name='delete_user_olx'),
    path('edit_product_olx/<int:pid>/', views.add_product_olx, name='edit_product_olx'),
    path('add_product_olx/', views.add_product_olx, name='add_product_olx'),
    path('view_product_olx/', views.view_product_olx, name='view_product_olx'),
    path('delete_product_olx/<int:pid>/', views.delete_product_olx, name='delete_product_olx'),
    path('view_brand_olx/', views.view_brand_olx, name='view_brand_olx'),
    path('edit_category_olx/<int:pid>/', views.add_category_olx, name='edit_category_olx'),
    path('add_category_olx/', views.add_category_olx, name='add_category_olx'),
    path('view_category_olx/', views.view_category_olx, name='view_category_olx'),
    path('delete_category_olx/<int:pid>/', views.delete_category_olx, name='delete_category_olx'),
    path('edit_brand_olx/<int:pid>/', views.add_brand_olx, name='edit_brand_olx'),
    path('add_brand_olx/', views.add_brand_olx, name='add_brand_olx'),
    path('view_brand_olx/', views.view_brand_olx, name='view_brand_olx'),
    path('delete_brand_olx/<int:pid>/', views.delete_brand_olx, name='delete_brand_olx'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('change_password/', views.change_password, name="change_password"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('ad_post/', views.ad_post, name="ad_post"),
    path('ad_post/<int:pid>/', views.ad_post, name="ad_post"),
]