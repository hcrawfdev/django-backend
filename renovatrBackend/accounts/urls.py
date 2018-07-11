from django.urls import include, path, re_path

from accounts.views import (
    User_Creation_View
)

from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$', User_Creation_View.as_view(), name='accounts'),
    re_path(r'^login/$',obtain_jwt_token),
]