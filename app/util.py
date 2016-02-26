import urllib

from flask import url_for

def list_routes(app):
    """ List routes """
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        options = {arg: "[{}]".format(arg) for arg in rule.arguments}
        url = url_for(rule.endpoint, **options)
        url = urllib.parse.unquote(url)
        yield rule.endpoint, methods, url
