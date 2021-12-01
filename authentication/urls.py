from django.urls import path
from django.views.generic import TemplateView
from .views import UsersList, HomeView, UsersDetails, create_order


urlpatterns = [
        path('', HomeView.as_view(template_name='home.html'), name='home'),
        path('users/shop_user_list', UsersList.as_view(), name='shopuserlist'),
        path('users/<pk>/customer_details', UsersDetails.as_view(), name='userdetails'),
        path('users/<pk>/create_order', create_order, name='createorder'),
]
