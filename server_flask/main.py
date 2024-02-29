from flask import Flask, request
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Server
from exts import db

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

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


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello World"}


@api.route("/servers")
class ServersResource(Resource):

    @api.marshal_list_with(server_model)
    def get(self):
        """Get all remote servers"""

        servers = Server.query.all()

        return servers

    @api.marshal_with(server_model)
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


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Server": Server}


if __name__ == "__main__":
    app.run()
