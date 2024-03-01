from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Server, User
from exts import db
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    jwt_required,
)

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

migrate = Migrate(app, db)
JWTManager(app)

api = Api(app, doc="/docs")


# server model (serializer)
server_model = api.model(
    "Server",
    {
        "id": fields.Integer(),
        "hostname": fields.String(),
        "server_username": fields.String(),
        "server_password": fields.String(),
        "port": fields.String(),
    },
)

# user signup model schema (serializer)
signup_model = api.model(
    "SignUp",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
    },
)

# user login model schema (serializer)
login_model = api.model(
    "Login",
    {"email": fields.String(), "password": fields.String()},
)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello World"}


@api.route("/signup")
class SignUp(Resource):

    @api.expect(signup_model)
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

        return jsonify({"message": f"User created successfully"})


@api.route("/login")
class Login(Resource):

    @api.expect(login_model)
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
                {"access-token": access_token, "refresh_token": refresh_token}
            )


@api.route("/servers")
class ServersResource(Resource):

    @api.marshal_list_with(server_model)
    def get(self):
        """Get all remote servers"""

        servers = Server.query.all()

        return servers

    @api.marshal_with(server_model)
    @jwt_required()
    def post(self):
        """Create a new remote server"""

        data = request.get_json()

        new_server = Server(
            hostname=data.get("hostname"),
            server_username=data.get("server_username"),
            server_password=data.get("server_password"),
            port=data.get("port"),
        )

        new_server.save()

        return new_server, 201


@api.route("/server/<int:id>")
class ServerResource(Resource):

    @api.marshal_with(server_model)
    @jwt_required()
    def get(self, id):
        """Get a specific server by its ID"""
        server = Server.query.get_or_404(id)

        return server

    @api.marshal_with(server_model)
    @jwt_required()
    def put(self, id):
        """Update a specific server by its ID"""
        server_to_update = Server.query.get_or_404(id)

        data = request.get_json()

        server_to_update.update(
            data.get("hostname"),
            data.get("server_username"),
            data.get("server_password"),
            data.get("port"),
        )

        return server_to_update

    @api.marshal_with(server_model)
    @jwt_required()
    def delete(self, id):
        """Delete a specific server by its ID"""
        server_to_delete = Server.query.get_or_404(id)

        server_to_delete.delete()

        return server_to_delete


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Server": Server}


if __name__ == "__main__":
    app.run()
