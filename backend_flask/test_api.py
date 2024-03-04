import unittest
from main import create_app
from config import TestConfig
from exts import db


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client(self)

        with self.app.app_context():
            # db.init_app(self.app)
            db.create_all()

    def test_hello_world(self):
        """Test for Hello World"""
        response = self.client.get("/server/hello")
        data = response.get_json()
        # status_code = response.status_code
        # print(data, status_code)

        self.assertEqual(data, {"message": "Hello World"})

    def test_user_signup(self):
        """Test user sign up API."""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        status_code = signup_response.status_code
        # print(status_code)
        self.assertEqual(status_code, 201)

    def test_user_login(self):
        """Test the user login endpoint of the server."""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        login_response = self.client.post(
            "/auth/login",
            json={"email": "testuser@testmail.com", "password": "password"},
        )

        status_code = login_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_all_servers(self):
        """Test getting all servers from the server list route."""
        response = self.client.get("/server/")

        status_code = response.status_code

        self.assertEqual(status_code, 200)

    def test_get_one_server(self):
        """Test getting a server from the server detail route."""
        id = 1
        response = self.client.get(f"/server/{id}")

        status_code = response.status_code

        self.assertEqual(status_code, 401)

    def test_create_server(self):
        """Test creating a server"""
        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        login_response = self.client.post(
            "/auth/login",
            json={"email": "testuser@testmail.com", "password": "password"},
        )

        access_token = login_response.json["access_token"]

        create_server_response = self.client.post(
            "/server/",
            json={
                "hostname": "test-server",
                "server_username": "test@server",
                "server_password": "test123",
                "port": "22",
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = create_server_response.status_code
        # print(status_code)
        # print(create_server_response.json)
        self.assertEqual(status_code, 201)

    def test_get_a_server(self):
        """Test getting a specific server by its ID"""
        id = 1

        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        login_response = self.client.post(
            "/auth/login",
            json={"email": "testuser@testmail.com", "password": "password"},
        )

        access_token = login_response.json["access_token"]

        create_server_response = self.client.post(
            "/server/",
            json={
                "hostname": "test-server",
                "server_username": "test@server",
                "server_password": "test123",
                "port": "22",
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )

        get_server_response = self.client.get(
            f"/server/{id}",
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = get_server_response.status_code

        self.assertEqual(status_code, 200)

    def test_update_server(self):
        """Test updating an existing server."""
        id = 1

        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        login_response = self.client.post(
            "/auth/login",
            json={"email": "testuser@testmail.com", "password": "password"},
        )

        access_token = login_response.json["access_token"]

        create_server_response = self.client.post(
            "/server/",
            json={
                "hostname": "test-server",
                "server_username": "test@server",
                "server_password": "test123",
                "port": "22",
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )

        update_server_response = self.client.put(
            f"/server/{id}",
            json={
                "hostname": "Updated-test-server",
                "server_username": "Updated-test@server",
                "server_password": "Updated-test123",
                "port": "22",
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = update_server_response.status_code
        # print(update_server_response.json)
        # print(status_code)

        self.assertEqual(status_code, 200)

    def test_delete_server(self):
        """Test deleting an existing server."""
        id = 1

        signup_response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        login_response = self.client.post(
            "/auth/login",
            json={"email": "testuser@testmail.com", "password": "password"},
        )

        access_token = login_response.json["access_token"]

        create_server_response = self.client.post(
            "/server/",
            json={
                "hostname": "test-server",
                "server_username": "test@server",
                "server_password": "test123",
                "port": "22",
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )

        delete_server_response = self.client.delete(
            f"/server/{id}",
            headers={"Authorization": f"Bearer {access_token}"},
        )

        status_code = delete_server_response.status_code

        self.assertEqual(status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
