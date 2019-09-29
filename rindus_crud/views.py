from django.shortcuts import render
from rindus_crud.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class UsersList(LoginRequiredMixin, generic.ListView):
	login_url = '/login/'
	model = User
	context_object_name = 'userList'
	template_name = 'home.html'
	paginate_by = 10
	ordering = ['user_id']

	def get_users(self):
		query = super(UsersList, self).get_queryset()
		return query
