from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models  import *
from user.serializer import *


class UserseriView(APIView):
	def get(self, request):
		a = User.objects.all()
		s = Userseri(a, many = True)
		return Response(s.data)

	def post(self, request):
		s = Userseri(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)


class BolimseriView(APIView):
	def get(self, request):
		a = Bolim.objects.all()
		s = Bolimseri(a, many = True)
		return Response(s.data)

	def post(self, request):
		s = Bolimseri(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)
	

class Ish_turiseriView(APIView):
	def get(self, request):
		a = Ish_turi.objects.all()
		s = Ish_turiseri(a, many = True)
		return Response(s.data)

	def post(self, request):
		s = Ish_turiseri(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)


class MaxsulotseriView(APIView):
	def get(self, request):
		a = Maxsulot.objects.all()
		s = Maxsulotseri(a, many = True)
		return Response(s.data)

	def post(self, request):
		s = Maxsulotseri(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)


class XodimseriView(APIView):
	def get(self, request):
		a = Xodim.objects.all()
		s = Xodimseri(a, many = True)
		return Response(s.data)

	def post(self, request):
		s = Xodimseri(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)


class ProblemseriView(APIView):
	def get(self, request):
		a = Problem.objects.all()
		s = Problemseri(a, many = True)
		return Response(s.data)

	def post(self, request):
		s = Problemseri(data=request.data)
		if s.is_valid():
			s.save()
			return Response(s.data)
		return Response(s.errors)
	
