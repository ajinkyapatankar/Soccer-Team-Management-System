
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
#
# login_required(profile_decorator.required_user_types(SUPER_ADMIN, ENTERPRISE_ADMIN, SUPERVISOR, USER)(views.Dashboard.as_view())),
#         name='dashboard')
urlpatterns = [
    url(r'^books/',views.Books.as_view(), name='books'),
    url(r'^build/',views.BuildTeam.as_view(), name='books'),
url(r'^manage/',views.ManageTeam.as_view(), name='books'),
url(r'^substitute/',views.SubstituteTeam.as_view(), name='books'),
url(r'^analytics/',views.Analytics.as_view(), name='books'),
url(r'^BuildBudgetTeam/',views.BuildBudgetTeam.as_view(), name='books'),

    ]