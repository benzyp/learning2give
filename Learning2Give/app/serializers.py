from app.models import Cause, Student, Donor, Learner, Locale
from rest_framework import serializers
from datetime import datetime
from neomodel import (StructuredNode,StringProperty, DateTimeProperty, IntegerProperty, UniqueIdProperty,RelationshipFrom, RelationshipTo)


class LocaleSerializer(serializers.Serializer):
    name=serializers.CharField()
    state=serializers.CharField()
    def create(self, validated_data):
        return Locale.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance

class CauseSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    title = serializers.CharField()
    goal = serializers.IntegerField()
    locale = LocaleSerializer(required=False)#serializers.StringRelatedField(many=False)
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        cause = Cause.create(validated_data)
        locale_data = validated_data.pop('locale')
        locale = Locale.get_or_create(locale_data)  #only works because locale does not have uid otherwise get_or_create always creates a new object
        cause[0].location.connect(locale[0])#connect the cause to the Locale
        return cause    
        #the workaround for models that require a uid which fails get_or_create because of the uid, is to run dedicated query to verify if locale exists
        #for a newly created object, create returns an array requiriing locale[0] to access
        #try:
        #    locale = Locale.nodes.get(name=locale_data["name"],state=locale_data["state"])#first time an exception is thrown because it doesn't exist
        #except Locale.DoesNotExist:
        #    locale = Locale.create(locale_data)#create the locale
        #    cause[0].location.connect(locale[0])#create the cause
        #    return cause     
        #cause[0].location.connect(locale)#connect the cause to the existing locale
        #return cause

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.goal = validated_data.get('goal', instance.goal)
        #instance.locale = validated_data.get('locale', instance.locale)#locale is not being updated - it's possible as with save but not being done
        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    uid=serializers.CharField(required=False)
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.CharField()
    cell = serializers.CharField()
    created = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Student.create(validated_data)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.email = validated_data.get('email', instance.email)
        instance.cell = validated_data.get('cell', instance.cell)
        instance.save()
        return instance
    
class DonorSerializer(serializers.Serializer):
    pass

class LearnerSerializer(serializers.Serializer):
    pass

class SessionSerializer(serializers.Serializer):
    uid=serializers.CharField
    created=serializers.DateTimeField
    completed=serializers.DateTimeField
    price=serializers.IntegerField

#class CauseSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Cause
#        fields = ('id','title','created','goal')
