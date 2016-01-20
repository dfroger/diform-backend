import json
import os
from os.path import isfile
import unittest
import tempfile

import diform

class TestDiform(unittest.TestCase):

    def setUpClass():
        if isfile('test.db'):
            os.remove('test.db')
        diform.app.config.from_object('config.TestingConfig')
        diform.init_db()

    def setUp(self):
        self.app = diform.app.test_client()

    def test_create_user_and_questionnaire(self):
        # Create a new user: David.
        user = {'name': 'David'}
        self.app.post('/api/user', data = json.dumps(user),
                       headers = {'content-type': 'application/json'},)

        # Get The list of users.
        reponse = self.app.get('/api/user')
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
        self.app.post('/api/questionnaire', data = json.dumps(questionnaire),
                       headers = {'content-type': 'application/json'},)

        # Get list of questionnaires.
        response = self.app.get('/api/questionnaire')
        data = json.loads(response.data.decode())
        self.assertEqual(data['num_results'], 1)
        self.assertEqual(data['objects'][0]['some_number'], 42)

if __name__ == '__main__':
    unittest.main()
