from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from models import Server
from flask_jwt_extended import jwt_required

server_ns = Namespace("server", description="Server related operations")

# server model (serializer)
server_model = server_ns.model(
    "Server",
    {
        "id": fields.Integer(),
        "hostname": fields.String(),
        "server_username": fields.String(),
        "server_password": fields.String(),
        "port": fields.String(),
    },
)


@server_ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello World"}


@server_ns.route("/")
class ServersResource(Resource):

    @server_ns.marshal_list_with(server_model)
    def get(self):
        """Get all remote servers"""

        servers = Server.query.all()

        return servers

    @server_ns.marshal_with(server_model)
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


@server_ns.route("/<int:id>")
class ServerResource(Resource):

    @server_ns.marshal_with(server_model)
    @jwt_required()
    def get(self, id):
        """Get a specific server by its ID"""
        server = Server.query.get_or_404(id)

        return server

    @server_ns.marshal_with(server_model)
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

    @server_ns.marshal_with(server_model)
    @jwt_required()
    def delete(self, id):
        """Delete a specific server by its ID"""
        server_to_delete = Server.query.get_or_404(id)

        server_to_delete.delete()

        return server_to_delete
