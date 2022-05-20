import generics as generics
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status, generics
# from .forms import  CreateUserForm
# from bookingapp.booking.decorators import unauthenticated_user
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .paginator import BasePagination
from .models import Routes, Train, User, TicKet, Comment, Booking
from .serializers import (
	RoutesSerializer, TrainSerializer,
	UserSerializer, TicketSerializer,
	CommentSerializer, BookingSerializer,
	TrainDetailSerializer
)


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.ListAPIView):
	queryset = User.objects.filter(is_active=True)
	serializer_class = UserSerializer
	parser_classes = [MultiPartParser]
	permission_classes = [permissions.IsAuthenticated]



	@action(methods=['get'], detail=True, url_path="active-user", url_name="active-user")
	def active_user(self, request):
		return Response(self.serializer_class(request.user, context={'request': request}).data,
						status=status.HTTP_200_OK)




class RoutesViewSet(viewsets.ViewSet, generics.ListAPIView, generics.GenericAPIView):
	queryset = Routes.objects.filter(active=True)
	serializer_class = RoutesSerializer
	pagination_class = BasePagination


	# def get_permissions(self):
	# 	if self.action == 'list':
	# 		return [permissions.AllowAny()]
	#
	# 	return [permissions.IsAuthenticated()]
	#
	def get_queryset(self):
		router =  Routes.objects.filter(active=True)

		kw = self.request.query_params.get('kw')
		if kw is not None:
			router = router.filter(starting_point__icontains=kw)
		return router


	@action(methods=['get'], detail=True, url_path='trains')
	def get_trains(self, request, pk):
		trains = Routes.objects(pk=pk).trains.filter(active=True)

		return Response(TrainSerializer(trains, many=True).data,status=status.HTTP_200_OK)


class TrainViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
	queryset = Train.objects.filter(active=True)
	serializer_class = TrainDetailSerializer

	#
	# def get_permissions(self):
	# 	if self.action == 'add_comment':
	# 		return [permissions.IsAuthenticated()]
	#
	# 	return [permissions.AllowAny()]


	@swagger_auto_schema(
		operation_description='This API is used to hidden the train',
		responses={
			status.HTTP_200_OK: TrainSerializer()
		}
	)


	@action(methods=['post'], detail=True, url_path='add-comment')
	def add_comment(self, request, pk):
		content = request.data.get('content')
		if content:
			c = Comment.objects.create(content=content, train=self.get_object(),
						user= request.user)
			return Response(CommentSerializer(c).data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST )


	@action(methods=['post'], detail=True, url_path='hide-train', url_name='hide-train')
	def hide_train(self, request, pk):
		try:
			t = Train.objects.get(pk=pk)
			t.active = False
			t.save()
		except Train.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)

		return Response(data=TrainSerializer(t).data, status=status.HTTP_200_OK)



class TicketViewSet(viewsets.ViewSet, generics.ListAPIView):
	queryset = TicKet.objects.filter(active=True)
	serializer_class = TicketSerializer


	def get_permissions(self):
		if self.action == 'list':
			return [permissions.AllowAny()]

		return [permissions.IsAuthenticated()]


class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.CreateAPIView):
	queryset = Comment.objects.filter(active=True)
	serializer_class = CommentSerializer
	permission_classes = [permissions.IsAuthenticated]

	def destroy(self, request, *args, **kwargs):
		if request.user == self.get_object().user:
			return super().destroy(request, *args, **kwargs)

		return Response(status=status.HTTP_403_FORBIDDEN)


	def partial_update(self, request, *args, **kwargs):
		if request.user == self.get_object().user:
			return super().partial_update(request, *args, **kwargs)

		return Response(status=status.HTTP_403_FORBIDDEN)


class BookingViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
	queryset = Booking.objects.filter(active=True)
	serializer_class = BookingSerializer

	def get_permissions(self):
		if self.request.method == 'GET':
			return [permissions.AllowAny()]

		return [permissions.IsAuthenticated()]


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