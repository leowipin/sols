from django.urls import path
from users.views import *

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('groupCreation/', GroupView.as_view(), name='group'),
    path('signup/', SignUpView.as_view(), name='signup'),
]