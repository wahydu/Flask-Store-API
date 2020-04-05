import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):

    param = reqparse.RequestParser()
    param.add_argument('username', 
        type=str,
        required=True,
        help="This field cannot be blank!"
    )
    param.add_argument('password', 
        type=str,
        required=True,
        help="This field cannot be blank!"
    )
    
    def post(self):
        data = UserRegister.param.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists!"}, 400

        #user = UserModel.find_by_username(data['username'], data['password'])
        user = UserModel(**data) # unpacking
        user.save_to_db()

        return {"message" : "user created successfully!"}, 201