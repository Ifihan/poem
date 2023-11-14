import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        result = self.app.get('/')

        # Assert the response data
        self.assertEqual(result.status_code, 200)

    def test_generate_poem(self):
        result = self.app.post('/generate-poem', json={'prompt': 'test prompt'})

        # Assert the response
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
