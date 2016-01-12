import json
import os
from os.path import isfile
import unittest
import tempfile

import diform

class TestDiform(unittest.TestCase):

    def setUp(self):
        if isfile('test.db'):
            os.remove('test.db')
        diform.app.config.from_object('config.TestingConfig')
        self.app = diform.app.test_client()
        diform.init_db()

    def test_users(self):
        newperson = data={'name': u'David'}
        self.app.post('/api/user', data = json.dumps(newperson),
                       headers = {'content-type': 'application/json'},)
        r = self.app.get('/api/user')
        data = json.loads(r.data.decode())
        self.assertEqual(data['num_results'], 1)
        self.assertEqual(data['objects'][0]['name'], 'David')

if __name__ == '__main__':
    unittest.main()
