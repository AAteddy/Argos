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
        response = self.client.get("/server/hello")
        data = response.get_json()
        # status_code = response.status_code
        # print(data, status_code)

        self.assertEqual(data, {"message": "Hello World"})

    def test_user_signup(self):
        response = self.client.post(
            "/auth/signup",
            json={
                "username": "testuser",
                "email": "testuser@testmail.com",
                "password": "password",
            },
        )

        status_code = response.status_code
        # print(status_code)
        self.assertEqual(status_code, 201)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
