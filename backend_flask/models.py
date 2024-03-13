from exts import db


# User model

"""
class User: 
    id: integer primary_key
    username: string
    email: string
    password: string
"""


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    servers = db.relationship("Server", backref="admin", lazy=True)

    def __repr__(self):
        return f"<User {self.username} >"

    def save(self):
        db.session.add(self)
        db.session.commit()


# Server model

"""
class Server:
    id: int primary key
    hostname: str
    server_username: str
    server_password: str
    port: int
"""


class Server(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    hostname = db.Column(db.String(), nullable=False)
    server_username = db.Column(db.String(), nullable=False)
    server_password = db.Column(db.String(), nullable=False)
    port = db.Column(db.Integer(), nullable=False)
    cpu_info = db.Column(db.Float())
    memory_info = db.Column(db.Float())
    disk_info = db.Column(db.Float())
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"<Server {self.title}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, hostname, server_username, server_password, port):
        self.title = title
        self.hostname = hostname
        self.server_username = server_username
        self.server_password = server_password
        self.port = port

        db.session.commit()
