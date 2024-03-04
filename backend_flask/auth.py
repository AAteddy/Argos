from flask import request, jsonify, make_response
from flask_restx import Namespace, Resource, fields
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)


auth_ns = Namespace("auth", description="User Authentication related operations")

# user signup model schema (serializer)
signup_model = auth_ns.model(
    "SignUp",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    },
)

# user login model schema (serializer)
login_model = auth_ns.model(
    "Login",
    {"email": fields.String(), "password": fields.String()},
)


@auth_ns.route("/signup")
class SignUp(Resource):

    @auth_ns.expect(signup_model)
    def post(self):
        """Create a new user"""
        data = request.get_json()

        email = data.get("email")
        db_user = User.query.filter_by(email=email).first()
        if db_user is not None:
            return jsonify({"message": f"User with email {email} already exists."})

        new_user = User(
            username=data.get("username"),
            email=data.get("email"),
            password=generate_password_hash(data.get("password")),
        )

        new_user.save()

        return make_response(jsonify({"message": f"User created successfully"}), 201)


@auth_ns.route("/login")
class Login(Resource):

    @auth_ns.expect(login_model)
    def post(self):
        """login a user with the given credentials"""
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        db_user = User.query.filter_by(email=email).first()
        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.email)
            refresh_token = create_refresh_token(identity=db_user.email)
            return jsonify(
                {"access_token": access_token, "refresh_token": refresh_token}
            )


@auth_ns.route("/refresh")
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """Refresh a token. A valid refresh token must be in the header."""
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_token}), 200)
