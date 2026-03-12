import unittest
from src.create_app import create_app

class TodoTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_todos_initially_empty(self):
        response = self.client.get('/todos')
        self.assertEqual(response.json, [])
        self.assertEqual(response.status_code, 200)

    
if __name__ == '__main__':
    unittest.main()