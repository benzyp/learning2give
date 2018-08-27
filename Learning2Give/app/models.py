"""
Definition of models.
"""

from django.db import models
from django_neomodel import DjangoNode
from neomodel import (StructuredNode,StringProperty, DateTimeProperty, IntegerProperty, UniqueIdProperty,RelationshipFrom, RelationshipTo)

class Cause(StructuredNode):
    uid=UniqueIdProperty()
    title = StringProperty()
    created = DateTimeProperty()
    goal = IntegerProperty()
    #relationships
    location=RelationshipTo('Locale','LOCATED_IN')

 
    
class User(StructuredNode):
    __abstract_node__ =  True
    uid=UniqueIdProperty()
    username=StringProperty()
    firstName=StringProperty()
    lastName=StringProperty()
    email=StringProperty()
    cell=StringProperty()
    created=DateTimeProperty()

class Session(StructuredNode):
    uid=UniqueIdProperty()
    created=DateTimeProperty()
    completed=DateTimeProperty()
    price=IntegerProperty()
    #relationships
    belongs=RelationshipTo(Cause,'BELONGS_TO')
    supported = RelationshipFrom('Student','LEARNS_FOR')
    supported = RelationshipFrom('Learner','LEARNS_FOR')
    supported = RelationshipFrom('Donor','DONATES_FOR')
    summarized = RelationshipFrom('Synopsis','SUMMARIZED_BY')

class Student(User):
    uid=UniqueIdProperty()
    supports=RelationshipTo('Session','LEARNS_FOR')
    sumarizes=RelationshipTo('Synopsis',"SUMARIZED_BY")

class Learner(User):
    uid=UniqueIdProperty()
    supports=RelationshipTo('Session','LEARNS_FOR')

class Donor(User):
    uid=UniqueIdProperty()
    supports=RelationshipTo('Session','DONATES_FOR')

class Synopsis(StructuredNode):
    uid=UniqueIdProperty()
    summarizes = RelationshipTo('Session','SUMMARIZES')
    summarized = RelationshipFrom('Student','SUMMARIZED_BY')

class Locale(StructuredNode):
    name=StringProperty(required=True)
    state=StringProperty(required=True)
    #relationships
    location = RelationshipFrom('Cause','LOCATED_IN')




