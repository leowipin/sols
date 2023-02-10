from django.urls import path
from users.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('groupCreation/', GroupView.as_view(), name='group'),
    path('signup/', SignUpView.as_view(), name='signup'),
]