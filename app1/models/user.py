from app1.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

db='colegio_principe_de_paz'

class User:
    def __init__(self,data) :
        self.id=data['id']
        self.first_name=data['nombre']
        self.last_name=data['apellido']
        self.email=data['email']
        self.password=data['contraseña']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all_users(cls):
        query="select * from user"
        results=connectToMySQL('db').query_db(query)
        users=[]
        for valor in results:
            users.append(cls(valor))
        return users

    @classmethod
    def save_user(cls,data):
        query="insert into usuarios (nombre,apellido,email,contraseña, created_at, updated_at) values (%(nombre)s,%(apellido)s,%(email)s,%(contraseña)s,now(),now());"
        result=connectToMySQL(db).query_db(query,data)
        return result

    @classmethod
    def get_id(cls,data):
        query  = "select * from usuarios where id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def get_one_user(cls,data):
        query  = "select * from user where id = %(id)s;"
        result = connectToMySQL('db').query_db(query,data)
        user=[]
        print(result)
        for valor in result:
            user.append(cls(valor))
        return cls(user)

    @classmethod
    def get_email(cls,data):
        query="select * from usuarios where email=%(email)s"
        results=connectToMySQL(db).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def destroy(cls,data):
        query  = "delete from user where id = %(id)s;"
        return connectToMySQL('db').query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query  = "select * from user where id = %(id)s;"
        result = connectToMySQL('db').query_db(query,data)
        print(result)
        return cls(result[0])

    @staticmethod
    def validate_register(user):
        is_valid=True
        query="select * from usuarios where email=%(email)s"
        result=connectToMySQL(db).query_db(query,user)
        if  len(result)>=1:
            flash('Email already taken','register')
            is_valid=False
        if len(user['nombre'])<3:
            flash('First name  must be at  least 3 characters','register')
            is_valid=False
        if len(user['apellido'])<3:
            flash('Last name  must be at  least 3 characters','register')
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email!','register')
            is_valid=False
        if len(user['contraseña'])<4:
            flash('Password  must be at  least 4 characters','register')
            is_valid=False
        if user['contraseña'] != user['confirmar']:
            flash("Passwords don't match",'register')
        return is_valid
    
