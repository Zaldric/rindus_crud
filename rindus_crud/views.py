from django.shortcuts import render
from rindus_crud.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy


class UsersList(LoginRequiredMixin, generic.ListView):
	login_url = '/login/'
	redirect_field_name = 'redirect_to'
	model = User
	context_object_name = 'userList'
	template_name = 'home.html'
	paginate_by = 10
	ordering = ['id']

	def get_users(self):
		query = super(UsersList, self).get_queryset()
		return query

class CreateUser(LoginRequiredMixin, generic.edit.CreateView):
	login_url = '/login'
	redirect_field_name = 'home'
	model = User
	fields = ('first_name', 'last_name', 'iban')
	template_name = 'user_form.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.admin_id = self.request.user
		return super(CreateUser, self).form_valid(form)
