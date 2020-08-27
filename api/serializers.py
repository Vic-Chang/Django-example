from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import Member
import json


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'age', 'created', 'last_modify_date']
