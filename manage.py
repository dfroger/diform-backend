#!/usr/bin/env python

import os

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db, util
from app.model import User, Questionnaire

app = create_app(os.getenv('DIFORM_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, User=User, Questionnaire=Questionnaire)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run test unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def routes():
    """List routes"""
    for endpoint, methods, url in util.list_routes(app):
        print("{:50s} {:20s} {}".format(endpoint, methods, url))

if __name__ == '__main__':
    manager.run()
