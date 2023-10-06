import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True 

    def test_hello_world(self):
        # Send GET request to the app and get the response
        response = self.app.get('/')
        
        # Assert the status code and the response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '<h1>Hello, World, Test 1!</h1>')

if __name__ == '__main__':
    unittest.main()
