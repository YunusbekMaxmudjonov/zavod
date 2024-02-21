from rest_framework import serializers

from .models  import *

class Userseri(serializers.ModelSerializer):

	class Meta:
		model = User
		fields =['id', 'gender', 'phone', 'image']
		
class Bolimseri(serializers.ModelSerializer):
	class Meta:
		model = Bolim
		fields = ['id', 'name', 'bolim_id']
		

class Ish_turiseri(serializers.ModelSerializer):
	class Meta:
		model = Ish_turi
		fields = ['id', 'ish_name','ish_id']
		
class Maxsulotseri(serializers.ModelSerializer):
	class Meta:
		model = Maxsulot
		fields = ['id', 'name','maxsulot_id']
		

class Xodimseri(serializers.ModelSerializer):
	class Meta:
		model = Xodim
		fields = ['id', 'gender','name','last_name','image','phone','ish_turi','xodim_id','bolimi']
		

class Problemseri(serializers.ModelSerializer):
	class Meta:
		model = Problem
		fields =['id','xato_id','problem_name']

class Mistakesseri(serializers.ModelSerializer):
	class Meta:
		model = Mistakes
		fields = ['id','xodim','user','problem','rasm','file','izoh','created','updated','maxsulot']