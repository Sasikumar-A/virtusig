# import serializer as serializer
import logging

import serializer as serializer
from knox.auth import TokenAuthentication
from rest_framework import permissions
from rest_framework.views import APIView

from virtusig_app.src.Data_serialization import DataSerialization
from django.contrib.auth import login, user_logged_out
from yagmail import YagAddressError
from knox.views import LoginView as KnoxLoginView
from virtusig_app import serializer, models
# from virtusig_app.serializer import LoginSerializer
import yagmail
from rest_framework.generics import GenericAPIView, CreateAPIView
# from rest_framework.views import APIView
# from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# from virtusig_app.serializer import LoginSerializer

_logger = logging.getLogger(__name__)


class LoginReg(GenericAPIView):
    serializer_class = serializer.LoginCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = serializer.LoginSerializer(data=request.data)
        check = models.LoginUser.objects.filter(email_id=request.data['email_id'])
        if check.exists():
            return Response("this email id is already taken")
        else:
            create = models.LoginUser.objects.create(email_id=request.data['email_id'])
            # yag = yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@')
            content = ['verify the email successfully']
            subject = 'Email verification for VirtuSig'
            yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@').send([request.data['email_id']], subject, content)
            data = {'response_code': 200,
                    'message': " email send successfully",
                    'statusFlag': True,
                    'status': 'success',
                    'errorDetails': None,
                    'data': [],
                    }
            return Response('Email sent successfully')


class LoginReg1(GenericAPIView):
    serializer_class = serializer.UserSerializer

    def post(self, request, *args, **kwargs):
        # serializer_class = serializer.UserTableSeriaizer(data=request.data)
        check = models.Users.objects.filter(user_email=request.data['user_email'])
        if not check.exists():
            serializer_class = serializer.CreateUserSerializer(data=request.data)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            content = ['verify the email successfully']
            subject = 'Email verification for VirtuSig'
            yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@').send([request.data['user_email']], subject, content)
            data = {'response_code': 200,
                    'message': " email send successfully",
                    'statusFlag': True,
                    'status': 'success',
                    'errorDetails': None,
                    'data': 'Email sent successfully',
                    }
            return Response(data)
        else:
            data = {'response_code': 400,
                    'message': "This Email id is already exists ",
                    'statusFlag': False,
                    'status': 'Failed',
                    'errorDetails': 'Already exists',
                    'data': 'Not valid',
                    }
            return Response(data)


class EnvelopData(GenericAPIView):
    serializer_class = serializer.EnvelopSerializer

    def post(self, request, **kwargs):
        """Here we use post method for creating the envelop
        and sending mail for user signing the document"""
        try:
            serializer_class = serializer.EnvelopSerializer(data=request.data)
            yagmail.SMTP(request.data['email_id'], request.data['sender_password']).send(
                request.data['recepient_id'],
                subject=request.data['subjects'],
                contents=request.data['body'],
                attachments=request.data['attachment'],
                cc=request.data['cc'])
            x1 = []
            for i in range(len(serializer_class.initial_data['recepient_id'])):
                x1.append(serializer_class.initial_data["recepient_id"][i])
            x = ','.join(x1)
            print(x)
            serializer_class.initial_data['recepient_id'] = x
            print(serializer_class.initial_data['recepient_id'])
            if serializer_class.is_valid(raise_exception=True):
                serializer_class.save()
            _logger.info("Email send successfully.")
            data = {'response_code': 200,
                    'message': " email send successfully",
                    'statusFlag': True,
                    'status': 'success',
                    'errorDetails': None,
                    'data': [],
                    }
            return Response(data)

        except Exception as e:
            data = {"response_code": 500, "message": {"trace": str(e)}}
            _logger.error("sent message is failed.")
            return Response(data)


# import yagmail
#
# # yag = yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@')
# lol = input('Enter the name:-')
# sender_name = input('Enter the Assignee name:-')
#
# for i in range(5, 10):
#     content = ['Hi {}! \n This Email is for you to Signing the document for your offer letter \n Try to be a valid '
#                'signing process through this app and check whether your below mentions are right or wrong. \n if its '
#                'wrong please contact our executive for changing your authorities and build your sign valid. \n'
#                'Thank you \n \n {},\n Virtusign Pvt.ltd \n Trichy-621 112 \n Tamil Nadu \n India '
#                '\n8072070866'.format(lol, sender_name)]
#     # yag.send('@vrdella.com', 'dummy', content)
#     # content = r"C:\Users\Vrdella\Documents\content.txt"
#     subject = 'dummy{}'
#     yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@').send(['levister@vrdella.com'], subject, content,
#                                                                  attachments=[r"C:\Users\Vrdella\Downloads\sign-easy "
#                                                                               r"document.docx"])
#     print('{} Email send successfully'.format(i))

# class Login_user(GenericAPIView):
#     serializer_class = serializer.LoginDisplaySerializer
#
#     def post(self, request, *args, **kwargs):
#         try:
#             user_email = request.data.get('user_email')
#             password = request.data.get('password')
#             user_mail = models.Users.objects.filter(user_email=user_email)
#             if user_mail.exists():
#                 password1 = models.Users.objects.filter(user_email=user_email)
#                 password2 = models.Users.objects.filter(password=password)
#                 # serializer = serializer.LoginUserSerializer(user_mail, many=True)
#                 if password2 == password:
#                     password = models.Users.objects.filter(password=password)
#                     serializer_class = serializer.LoginUserSerializer(data=request.data)
#                     serializer_class.is_valid(raise_exception=True)
#                     user = serializer_class.validated_data['user']
#                     print('user', user)
#                     login(request, user)
#                     # user = serializer.validated_data['user']
#                     print('user', user)
#                     login(request, user)
#                     return Response({
#                         'response_code': 200,
#                         "message": " Email valid",
#                         'statusFlag': True,
#                         'status': 'SUCCESS',
#                         'errorDetails': None,
#                         'data': 'valid'})
#                 else:
#                     return Response({
#                         'response_code': 400,
#                         "message": " password is not valid",
#                         'statusFlag': False,
#                         'status': 'FAILURE',
#                         'errorDetails': " password is not valid",
#                         'data': 'not valid'})
#             else:
#                 return Response({'response_code': 500,
#                                  "message": " mail is not valid",
#                                  'statusFlag': False,
#                                  'status': 'FAILURE',
#                                  'errorDetails': " mail is not valid",
#                                  'data': 'not valid'})
#
#         except Exception as e:
#             return Response({
#                 'response_code': 500,
#                 "message": "Please Signup or enter the correct username password",
#                 'statusFlag': False,
#                 'status': 'FAILED',
#                 'errorDetails': str(e),
#                 'data': []
#             })
#
#
# class VerifyOTP(KnoxLoginView, CreateAPIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = serializer.LoginUserSerializer
#
#     def post(self, request, *args, **kwargs):
#         user_phone = request.data.get('user_phone')
#         user_password = request.data.get('password')
#         if user_phone and user_password:
#             user_password = models.Users.objects.filter(user_password=user_password)
#             print(user_password)
#             if str(user_password) == str(user_password):
#                 password = models.Users.objects.filter(password=user_password)
#                 serializer = serializer.LoginUserSerializer(data=user_password)
#                 serializer.is_valid(raise_exception=True)
#                 user = serializer.validated_data['user']
#                 print('user', user)
#                 login(request, user)
#                 # print('login:',login(request,user))
#                 _logger.info("logged-in successfully.Token Generated")
#                 return super().post(request, format=None)
#
#             else:
#                 _logger.error("password incorrect, please try again")
#                 return Response({
#                     'response': 500,
#                     'message': 'password incorrect, please try again'
#                 })
#         else:
#             return Response({
#                 'response': 500,
#                 'message': 'Phone not recognised. Kindly give correct number'
#             })


class Validate_Forget_Password(CreateAPIView):
    serializer_class = serializer.EmailsendingSerializer

    # permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email_id = request.data['email_id']
        user = models.VirtusigLogin.objects.filter(email_id=email_id).exists()
        if email_id and user:

            content = "Please click the below link to change your password"
            yagmail.SMTP('sasikumar@vrdella.com', 'Sasikumar5799@').send(request.data['email_id'],
                                                                         subject='reset your email here',
                                                                         contents=content)
            # sendOTP(user_phone)
            data_response = {
                'responseCode': 200,
                'message': 'link sent successfully',
                'statusFailed': True,
                'status': 'SUCCESS',
                'errorDetails': None,
                'data': []
            }
            return Response(data_response)
        else:
            _logger.error('You are not registered user')
            data_response = {
                'responseCode': 500,
                'message': 'You are not registered user.',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': 'You are not registered user.',
                'data': []
            }
            return Response(data_response)


class Update_Password(CreateAPIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = serializer.Update_PasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            user_phone = request.data['user_phone']
            password = request.data['password']
            if user_phone and password:
                user = models.Users.objects.filter(user_phone=request.data['user_phone'])
                phone_logged = models.PhoneOTP.objects.filter(user_phone=request.data['user_phone'])
                if user.exists() and phone_logged:
                    user = models.Users.objects.get(user_phone=user_phone)
                    user.set_password(password)
                    user.save()
                    _logger.info("logged-in successfully.Token Generated")
                    data_response = {
                        'responseCode': 200,
                        'message': 'Password updated successfully',
                        'statusFlag': True,
                        'status': 'SUCCESS',
                        'errorDetails': None,
                        'data': []
                    }
                    return Response(data_response)
        except Exception as e:
            data_response = {
                'responseCode': 500,
                'message': 'Please Enter the Valid Password',
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            }
            return Response(data_response)


class Login_user(KnoxLoginView, GenericAPIView):
    serializer_class = serializer.LoginDisplaySerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            user_email = request.data.get('user_email')
            password = request.data.get('password')
            user_mail = models.Users.objects.filter(user_email=user_email)
            if user_mail.exists():
                # serializer = serializer.LoginUserSerializer(user_mail, many=True)
                serializer_class = serializer.LoginUserSerializer(data=request.data)
                serializer_class.is_valid(raise_exception=True)
                user = serializer_class.validated_data['user']
                print('user', user)
                login(request, user)
                _logger.info("logged-in successfully.Token Generated")
                response = super().post(request, format=None)
                # user = serializer.validated_data['user']
                # print('user', user)
                # login(request, user)
                return Response({
                    'response_code': 200,
                    "message": " Email valid",
                    'statusFlag': True,
                    'status': 'SUCCESS',
                    'errorDetails': None,
                    'data': [response.data]})
            else:
                return Response({'response_code': 500,
                                 "message": " mail is not valid",
                                 'statusFlag': False,
                                 'status': 'FAILURE',
                                 'errorDetails': " mail is not valid",
                                 'data': 'not valid'})

        except Exception as e:
            return Response({
                'response_code': 500,
                "message": "Please Signup or enter the correct username password",
                'statusFlag': False,
                'status': 'FAILED',
                'errorDetails': str(e),
                'data': []
            })


class LogoutAllView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated, ]

    # serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        request.user.auth_token_set.all().delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)

        data = {'response_code': 200, 'message': "Logged-out Successfully"}
        return Response(data)
