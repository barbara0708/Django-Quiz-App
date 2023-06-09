from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.index,name='index'),
    path('categories/',views.categories,name="categories"),
    path('categories/category/',include('category.urls'),name='category'),
    path('sign-up/',views.signup_view,name="sign-up"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_request,name='logout'),
    path('reset/',views.reset_password,name='reset'),
    path('reset/done',views.reset_done,name='done')
]