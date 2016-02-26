import json
import os
from os.path import isfile
import unittest

from app import create_app, db

class TestApp(unittest.TestCase):

    def setUpClass():
        if isfile('test.db'):
            os.remove('test.db')

    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.app_context()
        self.client = self.app.test_client()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        self.ctx.pop()

    def test_create_user_and_questionnaire(self):
        # Create a new user: David.
        user = {'name': 'David'}
        self.client.post('/api/user', data = json.dumps(user),
                         headers = {'content-type': 'application/json'},)

        # Get The list of users.
        reponse = self.client.get('/api/user')
        data = json.loads(reponse.data.decode())

        # Check list of users contains David.
        self.assertEqual(data['num_results'], 1)
        self.assertEqual(data['objects'][0]['name'], 'David')

        # Create a new questionnaire.
        questionnaire = {
            'filler_id': 1,
            'some_number': 42,
            'some_text': u'Good cheese',
        }
        self.client.post('/api/questionnaire', data = json.dumps(questionnaire),
                       headers = {'content-type': 'application/json'},)

        # Get list of questionnaires.
        response = self.client.get('/api/questionnaire')
        data = json.loads(response.data.decode())
        self.assertEqual(data['num_results'], 1)
        self.assertEqual(data['objects'][0]['some_number'], 42)

if __name__ == '__main__':
    unittest.main()
