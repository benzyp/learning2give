from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from app.models import Cause, Student, Learner, Donor, Locale, Session
from app.serializers import CauseSerializer, StudentSerializer, LearnerSerializer, DonorSerializer, LocaleSerializer, SessionSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

from django.utils import timezone

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])

def cause_list(request):
    """
    List all causes, or create a cause.
    """
    if request.method == 'GET':
        causes = Cause.nodes.all()
        serializer = CauseSerializer(causes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CauseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created=timezone.now())
            #serializer.save(created=datetime.strptime(str(datetime.now()),"%Y-%m-%d %H:%M:%S.%f"))
            #serializer.data contains the parameters and values formatted as a dictionary {{'goal': 10000, 'locale': 'Scranton', 'title': 'Mr. Unique'}
            #serializer.validated_data contains the parameters and values as an object OrderedDict([('goal', 10000), ('locale', 'Scranton'), ('title', 'Mr. Unique')])
            #so it doesn't fail on serializers=>fields.getattr which operates on an object
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def cause_detail(request, pk):
    """
    Retrieve, update or delete a cause.
    """
    try:
        #get is used to retrieve one result multiple results will throw an error
        #if no match is found with get a DoesNotExist error is thrown
        #filter will return a NodeSet
        #cause = Cause.nodes.filter(title="Mrs. Foo")
        #cause = Cause.nodes.get(id=int(pk)) throws DoesNotExist error when matching on the id
        cause = Cause.nodes.get(uid=pk)
    
    except Cause.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CauseSerializer(cause)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CauseSerializer(cause, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cause.delete()
        return HttpResponse(status=204)

def create_test(request):
    cause = Cause.nodes.get(uid='acd858b70b2546c2ada110205e983379')

    student = Student.nodes.get(uid='f50ac9bd24b44c72aa3abc4a311457a6')

    student.supports.connect(cause)
    
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])

def student_list(request):
    """
    List all students, or create a student.
    """
    if request.method == 'GET':
        students = Student.nodes.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created=timezone.now())
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def student_detail(request, pk):
    """
    Retrieve, update or delete a student.
    """
    try:
        cause = Student.nodes.get(uid=pk)
    
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(cause)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(cause, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(cause.errors, status=400)

    elif request.method == 'DELETE':
        cause.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])

def learner_list(request):
    """
    List all learners, or create a learner.
    """
    if request.method == 'GET':
        learners = Learner.nodes.all()
        serializer = LearnerSerializier(learners, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = LernierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created=timezone.now())
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def learner_detail(request, pk):
    """
    Retrieve, update or delete a learner.
    """
    try:
        learner = Learner.nodes.get(uid=pk)
    
    except Learner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LearnerSerializer(learner)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LearnerSerializer(learner, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(learner.errors, status=400)

    elif request.method == 'DELETE':
        learner.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])

def donor_list(request):
    """
    List all donors, or create a donor.
    """
    if request.method == 'GET':
        students = Donor.nodes.all()
        serializer = DonorSerializer(donors, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created=timezone.now())
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def donor_detail(request, pk):
    """
    Retrieve, update or delete a donor.
    """
    try:
        donor = Donor.nodes.get(uid=pk)
    
    except Donor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DonorSerializer(cause)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        donor = DonorSerializer(donor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(donor.errors, status=400)

    elif request.method == 'DELETE':
        donor.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])

def locale_list(request):
    """
    List all loations, or create a locale.
    """
    if request.method == 'GET':
        locations = Locale.nodes.all()
        serializer = LocaleSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = LocaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created=timezone.now())
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def locale_detail(request, pk):
    """
    Retrieve, update or delete a locale.
    """
    try:
        locale = Locale.nodes.get(uid=pk)
    
    except Locale.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocaleSerializer(locale)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        locale = LocaleSerializer(locale, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(locale.errors, status=400)

    elif request.method == 'DELETE':
        locale.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])

def session_list(request):
    """
    List all sessions, or create a session.
    """
    if request.method == 'GET':
        sessions = Session.nodes.all()
        serializer = SessionSerializer(sessions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created=timezone.now())
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
@csrf_exempt
def session_detail(request, pk):
    """
    Retrieve, update or delete a session.
    """
    try:
        session = Session.nodes.get(uid=pk)
    
    except Session.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SessionSerializer(locale)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        locale = SessionSerializer(session, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(locale.errors, status=400)

    elif request.method == 'DELETE':
        session.delete()
        return HttpResponse(status=204)


