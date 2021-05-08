from django.urls import path
from members import views as member_views

app_name = "members"

urlpatterns = [path("list", member_views.member_list_view_handler, name="member_list")]
