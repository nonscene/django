from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import *
from home.serializers import *
@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
            'course_name' : 'python',
            'learn' : ['flask', 'django', 'Tornado', 'FastAPI'],
            'course_provider' : 'Scaler'
            }        
    if request.method == 'GET':
        print(request.GET.get('search'))
        print("You Hit An Get Method")
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print("*********")
        print(data)
        print("*********")
        print("You Hit An Post Method")
        return Response(courses)
    elif request.method == 'PUT':
        print("You Hit An Put Method")
        return Response(courses)
        

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({'message' : 'success'})
    
    return Response(serializer.errors)


class PersonAPI(APIView):

    def get(self, request):
        return Response({'message' : 'this is a get request'})
    
    def post(self, request):
        return Response({'message' : 'this is a post request'})
    
    def put(self, request):
        return Response({'message' : 'this is a put request'})

    def patch(self, request):
        return Response({'message' : 'this is a patch request'})
    
    def delete(self, request):
        return Response({'message' : 'this is a delete request'})
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        # objs = Person.objects.all() #to get all persons details
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    else:
        data = request.data
        obj = Person.objects.get(id = data['id']) 
        obj.delete()
        return Response({'message' : 'person deleted'})