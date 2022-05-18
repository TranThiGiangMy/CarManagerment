from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, status
# from .forms import  CreateUserForm
# from bookingapp.booking.decorators import unauthenticated_user
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Routes, Train, User, TicKet
from .serializers import RoutesSerializer, TrainSerializer, UserSerializer, TicketSerializer




class RoutesViewSet(viewsets.ModelViewSet):
	queryset = Routes.objects.filter(active=True)
	serializer_class = RoutesSerializer
	# permission_classes = [permissions.IsAuthenticated]


	def get_permissions(self):
		if self.action == 'list':
			return [permissions.AllowAny()]

		return [permissions.IsAuthenticated()]


class TrainViewSet(viewsets.ModelViewSet):
	queryset = Train.objects.filter(active=True)
	serializer_class = TrainSerializer

	@action(methods=['post'], detail=True, url_path='hide-train', url_name='hide-train')
	def hide_train(self, request, pk):
		try:
			t = Train.objects.get(pk=pk)
			t.active = False
			t.save()
		except Train.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		return Response(data=TrainSerializer(t).data, status=status.HTTP_200_OK)

#
# class UserViewSet(viewsets.ModelViewSet):
# 	queryset = User.objects.filter(active=True)
class TicketViewSet(viewsets.ModelViewSet):
	queryset = TicKet.objects.filter(active=True)
	serializer_class = TicketSerializer





#
# @unauthenticated_user
# def registerPage(request):
# 	form = CreateUserForm()
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')
#
# 			group = Group.objects.get(name='customer')
# 			user.groups.add(group)
#
# 			messages.success(request, 'Account was created for ' + username)
#
# 			return redirect('login')
#
# 	context = {'form': form}
# 	return render(request, 'accounts/register.html', context)
#
#
# @unauthenticated_user
# def loginPage(request):
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
#
# 		user = authenticate(request, username=username, password=password)
#
# 		if user is not None:
# 			login(request, user)
# 			return redirect('home')
# 		else:
# 			messages.info(request, 'Username OR password is incorrect')
#
# 	context = {}
# 	return render(request, 'accounts/login.html', context)
#
#
# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')
#
#
# @login_required(login_url='login')


def userPage(request):
	context = {}
	return render(request, 'accounts/user.html', context)