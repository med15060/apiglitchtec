from django.urls import path
from django.conf.urls import include


from .import views

from .views import obtain_auth_token,CustomObtainAuthToken
urlpatterns = [
    path('api-token-auth1/', obtain_auth_token),
    path('api-token-auth/', CustomObtainAuthToken.as_view()),
    path('sellers/', views.userlist,name='userlist'),
    path('user/', views.scretuserdetail,name='userdetailowner'),
    path('user/<str:pk>/', views.userdetail,name='userdetail'),
    path('user-create/', views.usercreate,name='usercreate'),
    path('user-update/<str:pk>', views.userupdate,name='userupdate'),
    path('user-delete/<str:pk>', views.userdelete,name='userdelete'),
    path('job/', views.joblist,name='joblist'),
    path('job/<str:pk>/', views.jobdetail,name='jobdetail'),
    path('myjobs/', views.myjobs,name='myjobs'), 
    path('myjobs_seller/', views.myjobs_seller,name='myjobs'), 
    
    path('notifications/', views.notification,name='notification'),
    path('job-create/', views.jobcreate,name='jobcreate'),
    path('job-update/<int:pk>', views.jobupdatetocomplate,name='jobupdate'),
    path('job-delete/<int:pk>', views.jobdelete,name='jobdelete'),
    path('offer/<int:pk>/', views.offercreate,name='offerlist'),
    path('myoffers/', views.myoffers_seller,name='myoffers'),
    path('myjoboffers/', views.myoffers,name='myoffers'),
    path('myjoboffers/<int:pk>/', views.myoffers,name='myoffers'),
    path('offer-detail/<str:pk>/', views.offerdetail,name='offerdetail'),
    path('offer-create/<int:pk>/', views.offercreate,name='offercreate'),
    path('offer-delete/<str:pk>', views.offerdelete,name='offerdelete'),
    path('checkout/', views.order, name='paypal'),
    path('review/<int:pk_order>/', views.review,name='review'),
    path('buyerreview/<int:pk_order>/<int:pk_user>/<int:is_seller>/', views.review,name='buyerreview'),
    path('sellerreview/<int:pk_order>/<int:pk_user>/<int:is_seller>/', views.review,name='sellerreview'),
    # path('offer-detail/<str:pk>/', views.offerdetail,name='offerdetail'),
    path('offer-create/', views.offercreate,name='offercreate'),
    path('helprequest/', views.helprequest,name='helprequest'),
    path('userdeviceid/', views.userdeviceid,name='userdeviceid'),
    #path('offer-delete/<str:pk>', views.offerdelete,name='offerdelete'),
    path('order/<int:pk>/', views.order, name='paypal'),
    path('return_paid/<int:pk>/', views.orderpaied, name='paypalreturn'),
    path('return_notpaid/<int:pk>/', views.ordercancell, name='paypalcancel'),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
        path('transactions/', views.get_Balance, name='google_login'),
    

]
