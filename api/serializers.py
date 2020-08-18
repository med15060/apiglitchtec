from rest_framework import serializers
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework import serializers



class JobSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(required=True)
    job_budget=serializers.FloatField(required=True)
    job_hours=serializers.IntegerField(required=False)
    job_media=serializers.FileField(required=False)
    job_time=serializers.DateField(required=False)
    class Meta:
        model = Job
        fields = ["id","description","job_budget","job_hours","job_time","job_media",]




class HelpSerializer(serializers.ModelSerializer):
    description=serializers.CharField(required=True)
    class Meta:
        model = Ticket
        fields = ["description"]


class PostJobSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(required=True)
    job_budget=serializers.FloatField(required=True)
    job_hours=serializers.IntegerField(required=False)
    job_media=serializers.FileField(required=False)
    job_time=serializers.DateField(required=False)
    class Meta:
        model = Job
        fields = ["description","job_budget","job_hours","job_time","job_media",]



class JoblistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(read_only=True)
    title=serializers.CharField(read_only=True)
    job_budget=serializers.FloatField(read_only=True)
    job_hours=serializers.IntegerField(read_only=True)
    job_media=serializers.FileField(read_only=True)
    job_time=serializers.DateField(read_only=True)
    rate=serializers.FloatField(read_only=True,source="get_rate")
    buyer=serializers.IntegerField(read_only=True,source="buyer__first_name")
    buyer_id=serializers.IntegerField(read_only=True,source="buyer__id")
    buyer_profile=serializers.IntegerField(read_only=True,source="buyer__profile_picture")
    open=serializers.BooleanField(read_only=True,source="open_foroffer")
    class Meta:
        model = Job
        fields = ["id","description","title","job_budget","job_hours","job_time","job_media","rate",
"buyer",
"buyer_profile","buyer_id","open"]



"""String description,
      String title,
      String address,
      String paymentMethod,
      String specialize,
      String jobPrice,
      String jobHours,
      String jobType,
      int userId"""

class Balance_transactionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    requested_on=serializers.DateTimeField( read_only=True)
    amount=serializers.FloatField(read_only=True)
    done_on=serializers.DateTimeField(read_only=True)
    pending=serializers.BooleanField(read_only=True)
    refused=serializers.BooleanField(read_only=True)
    balance=serializers.FloatField(read_only=True,source="get_balance")
    class Meta:
        model = Job
        fields = ["id","requested_on","amount","done_on","refused","pending","balance"]

class UserDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField( read_only=True)
    first_name=serializers.CharField( read_only=True)
    profile=serializers.FileField(source="profile_picture" ,read_only=True)
    rate=serializers.FloatField(read_only=True,source="get_rate")
    specializes=serializers.CharField(read_only=True)
    class Meta:
        model = Job
        fields = ["id","description","first_name","profile","rate","specializes"]

class UserDetailsownerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField( read_only=True)
    first_name=serializers.CharField( read_only=True)
    profile=serializers.FileField(source="profile_picture" ,read_only=True)
    rate=serializers.IntegerField(read_only=True,source="get_rate")
    hourlyRate = serializers.FloatField( read_only=True)
    email=serializers.CharField( read_only=True)
    name=serializers.CharField( source="get_fullname",read_only=True)
    phone=serializers.CharField(read_only=True)
    zip=serializers.IntegerField(read_only=True,source="zip_code")
    country=serializers.CharField(read_only=True)
    state=serializers.CharField(read_only=True)
    address=serializers.CharField(read_only=True)
    phone=serializers.CharField(read_only=True)
    specializes=serializers.CharField(read_only=True)
    description=serializers.CharField(read_only=True)
    seller=serializers.BooleanField(read_only=True)
    #username=serializers.CharField(read_only=True)
    #profile_picture=serializers.FileField(,read_only=True)
    class Meta:
        model = User
        fields = ["id","description","first_name","profile","rate","hourlyRate","email","name","phone","zip","country","state","address","phone","specializes","description","seller"]

class JobDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(read_only=True)
    job_budget=serializers.FloatField(read_only=True)
    job_hours=serializers.IntegerField(read_only=True)
    job_media=serializers.FileField(read_only=True)
    job_time=serializers.DateField(read_only=True)
    rate=serializers.FloatField(read_only=True,source="get_rate")
    open=serializers.BooleanField(read_only=True,source="open_foroffer")
    progress=serializers.BooleanField(read_only=True,source="getstatus")
    completed=serializers.BooleanField(read_only=True)
    created=serializers.CharField(read_only=True)
    class Meta:
        model = Job
        fields = ["id","description","open","job_budget","job_hours","job_time","job_media","rate" ,"completed","progress","open","created"]

class JobprogressSZR(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(read_only=True)
    job_budget=serializers.FloatField(read_only=True)
    job_hours=serializers.IntegerField(read_only=True)
    job_media=serializers.FileField(read_only=True)
    job_time=serializers.DateField(read_only=True)
    rate=serializers.FloatField(read_only=True,source="get_rate")
    open=serializers.BooleanField(read_only=True,source="open_foroffer")
    progress=serializers.BooleanField(read_only=True,source="getstatus")
    completed=serializers.BooleanField(read_only=True,source="completed")
    created=serializers.CharField(read_only=True)
    class Meta:
        model = Job
        fields = ["id","description","open","job_budget","job_hours","job_time","job_media","rate","progress"]




class OfferSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(label='ID', read_only=True)
    description=serializers.CharField(required=True)
    offer_price=serializers.FloatField(required=False)
    offer_hours=serializers.IntegerField(required=True)
    #job_media=serializers.FileField(required=False)
    price_per_hour=serializers.FloatField(required=True)
    #job=serializers.FloatField(required=True)
    #accepted = serializers.BooleanField( read_only=True)
    class Meta:
        model = Offer
        fields = ["description","offer_price","offer_hours","price_per_hour",]




class OfferDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    user_name=serializers.CharField(read_only=True,source="seller_first_name")
    user=serializers.IntegerField(read_only=True,source="seller_id")
    created=serializers.CharField(read_only=True,source="offer_time")
    jobId=serializers.IntegerField(read_only=True,source="job_id") 
    profile_url=serializers.CharField(read_only=True,source="seller_profile_picture") 
    class Meta:
        model = Offer
        fields = ["accepted","user","id","jobId","description","offer_price","profile_url","offer_hours","price_per_hour","user_name","created"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['total_amount',"paied","url_payment",]

class GetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["created","description","rate"]


class GetNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        #fields = ["created","description","rate"]
"""
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["created","description","rate"]

"""

class SellerReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    class Meta:
        model = Review
        fields = ["id","buyer_username","created","description","rate","order"] 


        
class BuyerReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    class Meta:
        model = Review
        fields = ["seller_username","created","description","rate","order"] 



"""
"sller"
"created"
"seller_review"
"description"
"rate"
"order"
"""



from rest_auth.registration.serializers import RegisterSerializer
class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True,style={'input_type': 'password'})
    #date_of_birth = serializers.DateField(required=True)
    phone=serializers.CharField(required=True)
    country=serializers.CharField(required=True)
    state=serializers.CharField(required=True)
    address=serializers.CharField(required=True)
    phone=serializers.CharField(required=True)
    specializes=serializers.CharField(required=False)
    description=serializers.CharField(required=False)
    seller=serializers.BooleanField(required=False)
    username=serializers.CharField(required=False)
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    profile_picture=serializers.FileField(required=False)
    resumate=serializers.FileField(required=False)
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': self.validated_data.get('username', ''),
            'description': self.validated_data.get('description', ''),
            'seller': self.validated_data.get('seller', ''),
            'phone': self.validated_data.get('phone', ''),
            'country': self.validated_data.get('country', ''),
            'address': self.validated_data.get('address', ''),
            'specializes': self.validated_data.get('specializes', ''),
            'profile_picture':self.validated_data.get('profile_picture', ''),
            'resumate': self.validated_data.get('resumate', ''),
            
        }
"""
class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','name','date_of_birth'
        "phone",
        "country",
        "address",
        "specializes",
        "description",
        

        )
        read_only_fields = ('email',)


"""
"""
{"user": 
{
'password1': "hello",
'email':'med25@gmzil.com',
'first_name': 'first_name',
'last_name': 'last_name',
'username': 'usernamedfg',
'description': 'description',
'seller': "True",
'phone': 'phone',
'country': 'country',
'address': 'address',
'specializes': 'specializes',
'date_of_birth': 'date_of_birth'}}



{"user": 
{
"password1":"fgds",
"email":"med25@gmzil.com",
"first_name": "first_name",
"last_name": "last_name",
"username": "usernamedfg",
"description": "description",
"seller": "True",
"phone": "phone",
"country": "country",
"address":"address",
"specializes": "specializes"
}}
{
"password1":"fgdsmedsidi",
"password2":"fgdsmedsidi",
 "state": "state",
"email":"med25@gmzil.com",
"first_name": "first_name",
"last_name": "last_name",
"username": "usernamedfg",
"description": "description",
"seller": "True",
"phone": "phone",
"country": "country",
"address":"address",
"specializes": "specializes"
}

            """

class AuthCustomTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if validateEmail(email_or_username):
                user_request = get_object_or_404(
                    User,
                    email=email_or_username,
                )

                email_or_username = user_request.username

            user = authenticate(username=email_or_username, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "email or username" and "password"')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password",),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs