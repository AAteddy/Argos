from exts import db

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
    hostname = db.Column(db.String(), nullable=False)
    server_username = db.Column(db.String(), nullable=False)
    server_password = db.Column(db.String(), nullable=False)
    port = db.Column(db.Integer())

    def __repr__(self):
        return f"<Server {self.hostname}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, hostname, server_username, server_password, port):
        self.hostname = hostname
        self.server_username = server_username
        self.server_password = server_password
        self.port = port

        db.session.commit()


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

    def __repr__(self):
        return f"<User {self.username} >"

    def save(self):
        db.session.add(self)
        db.session.commit()
