from bottle import route, run, template, static_file
import lynxmotion
import behaviors
import os.path

static_root = os.path.join(os.path.dirname(__file__), 'static')

@route('/')
def home_page():
    return template('controller')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=static_root)

#run(reloader=False, host='localhost', port=8080, server='cherrypy')
run(reloader=False, host='0.0.0.0', port=8080)