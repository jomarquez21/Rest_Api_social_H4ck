from django.views.generic import View
from django.core.validators import validate_email
from models import UserHack
from re import findall
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, QueryDict
from json import dumps

class User():
    def __init__(self, request, user=None):
        self.request = request
        self.POST = request.POST.copy()
        self.user = user
        self.error = []
        self.data = {}
        self.out = {'code': 409}

    def one(self):
        self.__validate_user()
        if self.error:
            self.out.update({'error': self.error})
            return
        self.out.update({'user': self.serializer(self.user), 'status': 200})

    def all(self):
        __all_user = UserHack.objects.all()
        __users = []
        for i in __all_user:
            __users.append(self.serializer(i))
        self.out.update({'users': __users, 'status': 200})

    def create(self):
        self.__validate_info()
        if self.error:
            self.out.update({'error': self.error})
            return
        self.user = UserHack.objects.create(**self.data)
        self.out.update({'code': 201, 'user_id': self.user.id})

    def update(self):
        self.__validate_user()
        if self.error:
            self.out.update({'error': self.error})
            return
        self.__validate_info()
        if self.error:
            self.out.update({'error': self.error})
            return
        self.user.gender = self.data['gender']
        self.user.name = self.data['name']
        self.user.phone = self.data['phone']
        self.user.address = self.data['address']
        self.user.company = self.data['company']
        self.user.email = self.data['email']
        self.user.save()
        self.out.update({'code': 200})

    def delete(self):
        self.__validate_user()
        if self.error:
            self.out.update({'error': self.error})
            return
        self.user.delete()
        self.out.update({'code': 200})

    def serializer(self, data):
        return {
            'gender': {'id': data.gender, 'name': data.get_gender_display()},
            'name': data.name,
            'phone': data.phone,
            'address': data.address,
            'company': data.company,
            'email': data.email,
        }

    def __validate_info(self):
        __get_data = ['name', 'gender', 'company', 'email', 'phone', 'address']
        for i in __get_data:
            if self.POST.get(i, None):
                self.data.update({i: self.POST[i]})
            else:
                self.error.append({'field': i, 'error': 'is required'})

        if self.error: return

        try:
            validate_email(self.data['email'])
        except:
            self.error.append({'field': 'email', 'error': 'format not valid'})

        __gender_valid = [i[0] for i in UserHack._gender]
        try:
            if int(self.data['gender']) not in __gender_valid:
                self.error.append({'field': 'gender', 'error': 'not valid'})
        except:
            self.error.append({'field': 'gender', 'error': 'not valid', 'format': '1 = female, 2 = male'})

        if not findall(r"^\+\d{1,4}-\d{9,11}$", self.data['phone']):
            self.error.append({'field': 'phone', 'error': 'format not valid', 'format': '+XX-XXXXXXXXXXX'})

        if self.error: return

    def __validate_user(self):
        try:
            self.user = UserHack.objects.get(pk=self.user)
        except:
            self.error.append({'field': 'user', 'error': 'not valid'})

def response_json(data=None):
    __data = data or {}
    __code = {
        200: 'Successful',
        201: 'Created',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        409: 'Conflict',
        500: 'Internal Server Error'
    }
    if 'code' in __data:
        if __data['code'] in __code:
            __data.update({'status': __code[__data['code']]})
    response = HttpResponse(dumps(__data, cls=DjangoJSONEncoder), content_type="application/json")
    return response

class ViewUser(View):
    def get(self, request, *args, **kwargs):
        if 'user' not in kwargs: return response_json({'code': 405})
        __user = User(request, kwargs['user'])
        __user.one()
        return response_json(__user.out)

    def post(self, request, *args, **kwargs):
        if 'user' in kwargs: return response_json({'code': 405})
        __user = User(request)
        __user.create()
        return response_json(__user.out)

    def put(self, request, *args, **kwargs):
        if 'user' not in kwargs: return response_json({'code': 405})
        request.POST = QueryDict(request.read())
        __user = User(request, kwargs['user'])
        __user.update()
        return response_json(__user.out)

    def delete(self, request, *args, **kwargs):
        if 'user' not in kwargs: return response_json({'code': 405})
        __user = User(request, kwargs['user'])
        __user.delete()
        return response_json(__user.out)

class ViewUserAll(View):
    def get(self, request, *args, **kwargs):
        __user = User(request)
        __user.all()
        return response_json(__user.out)
