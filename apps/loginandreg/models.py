from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^a-zA-Z$')

class UserManager(models.Manager):
    def register(self, postdata):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        errors=[]
        if len(postdata['first_name']) < 2 or len(postdata['last_name']) < 2:
            errors.append('names need to be longet than 2 characters')
            # return {"Status": False, "errors":message}
        if not NAME_REGEX.match(postdata['first_name']):
            # print postdata['first_name']
            errors.append('only letters')
            # return {"Status": False,"errors":message}
        if not NAME_REGEX.match(postdata['last_name']):
            errors.append('only letters')
            # return {"Status": False,"errors":message}
        if len(postdata['email']) < 0:
            errors.append('cannot be empty')
            # return{"Status":False, "errors":message}
        if not EMAIL_REGEX.match(postdata['email']):
            errors.append('email format')
            # return {"Status": False, "errors":message}
        if postdata['password']!=postdata['confirm_password']:
            errors.append('passwords must match')
            # return {"Status": False, "errors": message}

        user = self.filter(email=postdata['email'])
        if user:
            errors.append('email already in use')
        response={}
        if errors:
            response['Status']=False
            response['errors'] = errors
        else:
            password= bcrypt.hashpw(postdata['password'].encode(),bcrypt.gensalt())
            email =self.create(first_name = postdata["first_name"],last_name= ["last_name"],email = postdata['email'],password=password)
            response['Status']=True
            response['email'] = email

        return response


    def login(self, postdata):
        user = self.filter(email=postdata['email'])
        if len(user) == 0:
            message = "you need to register"
            return {"Status":False, "errors":message}
        else:
            if bcrypt.hashpw(postdata['password'].encode(),user[0].password.encode()) != user[0].password:
                message="password incorrect"
                return{"Status":False,"errors":message}
        return {"Status":True, "user":user[0]}


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email =models.CharField(max_length=140, default='SOME STRING')
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
