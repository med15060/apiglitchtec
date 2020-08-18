from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()
import six
import sys
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status




"""
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': unicode(token.key),
        }

        return Response(content)


"""



from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from .serializers import *


class MyAuthToken(auth_views.ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = MyAuthToken.as_view()



class CustomObtainAuthToken(MyAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user_token=Token.objects.get(key=token).user_id
        user = User.objects.get(id=user_token)
        serializer=UserDetailsownerSerializer(user)
        data=serializer.data
        data["token"]=token.key
        #print(serializer.data,token)
       
        #if serializer.errors:
        #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scretuserdetail(request, pk=None):
        user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
        user = User.objects.get(id=user_token)
        #user = User.objects.get(id=pk)
        serializer = UserDetailsownerSerializer(user, many=False)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userdeviceid(request):
        user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
        user = User.objects.get(id=user_token)
        user.deivceid=request.data["deviceid"] if "deviceid" in request.data.keys() else None
        user.save()
        #user = User.objects.get(id=pk)
        #serializer = UserDetailsownerSerializer(user, many=False)
        return Response("done")



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usersignupdetail(request, pk):
    tasks = User.objects.get(id=pk)
    serializer = UserSerializer(tasks, many=False)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userlist(request):
    users = User.objects.all().filter(seller=True,is_active=True)
    serializer = UserDetailsSerializer(users, many=True)
    print(serializer.data)
    if users:
            return Response(serializer.data)
    print("nothing")
    return Response("No sellers right now availeble",status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userdetail(request, pk=None):
    if pk==None:
            user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
            user = User.objects.get(id=pk)
            #user = User.objects.get(id=pk)
            serializer = UserDetailsownerSerializer(user, many=False)
            return Response(serializer.data)
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['POST',"GET"])
def usercreate(request):
    print(request.data)
    try:
        if "email" in request.data.keys():
            user_object = User.objects.get(email=request.data['email'])
            print(user_object)
        else:
            return Response({"message":"Email already exists"})
    except User.DoesNotExist:
        user_object = None
    if request.method == 'POST':
        print("what is the problem")
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""       for k, v in request.data.items():
            setattr(user, k, v)
        user.save()
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        #     """


@api_view(['POST',"GET"])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def usercreate(request):
    print(request.data)
    try:
        if "email" in request.data.keys():
            user_object = User.objects.get(email=request.data['email'])
            print(user_object)
        else:
            return Response({"message":"Email already exists"})
    except User.DoesNotExist:
        user_object = None
    if request.method == 'POST':
        print("what is the problem")
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request=request)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def userupdate(request,pk):
    task = Account.objects.get(id=pk)
    for key, value in request.data.items():
        setattr(task, key, value)
    task.save()

    serializer = TaskSerializer(instance = task ,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def userdelete(request,pk=None):
    user= User.objects.get(pk=Token.objects.get(key=response.data['token']).user_id)
    #return Response({'token': token.key, 'id': token.})
    #task = Account.objects.get(id=pk)
    user.delete()
    return Response('Delete successfully.')









@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_Balance(request):
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    balance=Balance_transactions.objects.filter(user=user)
    if balance:
        serializer = Balance_transactionsSerializer(tasks, many=True)
        return Response(serializer.data)
    return Response("this job doesn't exist")

@api_view(['GET'])
def joblist(request,filter=None):
    tasks = Job.objects.all()
    if filter:
        tasks=tasks.filter(description__icontains=filter)
    serializer = JoblistSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jobdetail(request, pk):
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    print(request.data)
    #serializer = JobSerializer(data=request.data, many=False)
    if Job.objects.filter(pk=pk):
        Job=Job.objects.get(id=pk)
        if Job.buyer==user or Job.seller==user:
            serializer = JobDetailsSerializer(tasks, many=False)
            return Response(serializer.data)
    return Response("this job doesn't exist")

"""
@api_view(['GET'])
def jobscreated(request, pk):
    tasks = Job.objects.filter(creator=pk)
    serializer = JobSerializer(tasks, many=True)
    return Response(serializer.data)"""

@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
@permission_classes([IsAuthenticated])
def jobcreate(request):
    print(request.headers)
    print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    print(request.data)
    serializer = JobSerializer(data=request.data, many=False)
    if serializer.is_valid():
        #serializer.save()
        serializer.save(buyer=user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def jobupdate(request,pk):
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    try:
        Job=Job.objects.get(id=pk) 
    except:
        return Response("try later", status=status.HTTP_400_BAD_REQUEST)
    if Job.buyer==user:
        Job.completed=True
        Job.save()
    elif Job.seller==user:
        Job.complete_request=True
        Job.save()
    serializer = JobSerializer(instance = Job )
    #if serializer.is_valid():
    #    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myjobs(request): #list of jobs i got accepted
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    Jobs=Job.objects.filter(buyer__id=user_token) 
    serializer = JoblistSerializer(Jobs, many=True)
    if Jobs:
        print(Jobs)
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({"message":"No jobs for you "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myjobs_seller(request): #list of jobs i got accepted
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    Jobs=Job.objects.filter(seller__id=user_token).exclude(description__isnull=True)
    print([x.description for x in Jobs])
    serializer = PostJobSerializer(Jobs,many=True)
    if Jobs:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        return Response(serializer.data)
    else:
        return Response({"message":"No jobs for you "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#from .serializers import FileSerializer

"""
class jobcreate(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = JobSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""








@api_view(['POST'])
@permission_classes([IsAuthenticated])
def jobupdatetocomplate(request,pk):
    if Job.objects.filter(id=pk):
        job = Job.objects.get(id=pk)
    else:
        return Response("Couldn't find the job asking for it")
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    job.completed=True
    job.save()
    serializer = JobDetailsSerializer(instance = job )
    return Response(serializer.data)



@api_view(['DELETE'])
def jobdelete(request,pk):
    task = Job.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')


from .serializers import OfferDetailsSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myoffers_seller(request): #list of offers i got according to a job
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    offers=Offer.objects.filter(seller=user) #here is a problem OfferDetailsSerializer
    serializer = OfferDetailsSerializer(offers, many=True)
    print("---hi",serializer.data)
    #print(offer.job.buyer)
    if offers:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        return Response(serializer.data)
    else:
        return Response({"message":"you have no offer "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myoffers(request,pk): #list of offers i got according to a job
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(id=user_token)
    print(user_token)
    offers=Offer.objects.filter(job__id=int(pk),buyer=user) #here is a problem
    serializer = OfferDetailsSerializer(offers, many=True)
    print(offers)
    #print(offer.job.buyer)
    if offers:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({"message":"Not autherized "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offerlist(request,pk): #list of offers i got according to a job
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    job = Offer.objects.get(id=pk)
    offers=Offer.objects.filter(job=job) #here is a problem
    serializer = OfferDetailsSerializer(offers, many=True)
    if job.buyer==user:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({"message":"this job is not yours. "}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def offercreate(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    job=Job.objects.get(pk=pk)
    print("------------------",request.data)
    serializer = OfferSerializer(data=request.data, many=False)
    if serializer.is_valid():
        #serializer.save()
        serializer.save(seller=user,job=job)
        #serializer.data["accepted"]=offer.accepted
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def helprequest(request):
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    serializer = HelpSerializer(data=request.data, many=False)
    if serializer.is_valid():
        #serializer.save()
        serializer.save(user =user)
        #serializer.data["accepted"]=offer.accepted
        return Response("Hellp request was submitted we will conact you soon.")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offerdetail(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    offer = Offer.objects.get(id=pk)
    serializer = OfferDetailsSerializer(offer, many=False)
    print(offer.job.buyer)
    if offer.seller==user or offer.job.buyer==user:
        #serializer.save()
        #serializer.save(seller=request.user,job=job)
        serializer.data["accepted"]=offer.accepted
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    if pk:
        user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
        user= User.objects.get(pk=user_token)
        offer=Offer.objects.get(pk=pk)
        offer=offer.accepte()
        if Order.objects.filter(offer=offer):
            try:
                order=Order.objects.get(offer=offer)
            except:
                order=Order.objects.filter(offer=offer).first()
            url=order.paypal()
        else:
            order=Order()
            order.save(buyer=user ,offer=offer,seller=offer.seller)
            url=order.paypal()
        serializer= OrderSerializer(instance=order)
        if url:
            """if serializer.is_valid():
            #serializer.save()
            serializer.save(seller=request.user,job=job)
            return Response(serializer.data, status=status.HTTP_201_CREATED)"""
            return Response(serializer.data )
        else:
            return Response( "please try again later", status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def orderpaied(request,pk=None):
    if pk:
        #if Order.objects.filter(id=pk):
        #    #try:
        order=Order.objects.get(id=id)
        order.paied=True
        job=order.job
        job.open=False
        job.save()
        order.save()
        serializer= OrderSerializer(instance=order)
        return Response(serializer.data )
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response( "please try again later", status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def ordercancell(request,pk=None):
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    if pk:
        #if Order.objects.filter(id=pk):
        #    #try:
        order=Order.objects.get(id=id)
        serializer= OrderSerializer(instance=order)
        return Response(serializer.data )
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response( "please try again later", status=status.HTTP_400_BAD_REQUEST)






"""
@api_view(['POST'])
def offercreate(request):
   
    try:
        offer_object = Offer.objects.filter(job=request.data['job'],user=request.data['user'])
    except Offer.DoesNotExist:
        offer_object = None
        
    if offer_object:
        return Response({"error":"Offer already submitted"})
    else:
        serializer = OfferSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
"""







@api_view(['GET'])
@permission_classes([IsAuthenticated])
def notification(request): #list of offers i got according to a job
    #print(request.headers)
    #print("pk " , Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id)
    #print(request.data)
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    #job = Offer.objects.get(id=pk)
    Notifications=Notification.objects.filter(user=user) #here is a problem
    serializer = GetNotificationSerializer(Notifications, many=True)
    print(serializer.data)
    return Response(serializer.data)








@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def review(request,pk_user=None, pk_order=None,is_seller=0):
    if is_seller==0:
        is_seller=False
    else:
        is_seller=True
    user_token=Token.objects.get(key=request.headers["Authorization"].split()[1]).user_id
    user= User.objects.get(pk=user_token)
    if pk_order and  not request.POST:
        try:
            order=Order.objects.get(pk=pk_order)
        except:
            return Response("there is a problem in the order ID", status=status.HTTP_400_BAD_REQUEST) 
        reviews=Review.objects.filter(order=order)  
        reviews=reviews.filter(buyer=user).filter(seller=user) 
        if is_seller:
            review=reviews.filter(seller_review=is_seller)[0]
            serializer=GetReviewSerializer(instance=reviews)
            return Response(serializer.data)
        else:
            review=reviews.filter(seller_review=is_seller)[1]
    if pk_order and request.POST:
        try:
            order=Order.objects.get(pk=pk_order)
        except:
            return Response("there is a problem in the order ID", status=status.HTTP_400_BAD_REQUEST)
        if not is_seller:
            serializer= BuyerReviewSerializer(request.data)
            if serializer.is_valid():
                serializer.save(buyer=user,order=order)
            #serializer.save(seller=request.user,job=job)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else:
            serializer= SellerReviewSerializer(request.data,)
            if serializer.is_valid():
                serializer.save(seller=user,seller_review=True,order=order)
            #serializer.save(seller=request.user,job=job)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""@api_view(['GET'])
def userreviews(request,pk):
    tasks = Review.objects.filter(user=pk)
    serializer = ReviewSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def jobreview(request,pk):
    tasks = Review.objects.filter(job=pk)
    serializer = ReviewSerializer(tasks, many=True)
    return Response(serializer.data)"""

@api_view(['DELETE'])
def offerdelete(request,pk):
    task = Offer.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')


