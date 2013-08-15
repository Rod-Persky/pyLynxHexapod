from bottle import route, run, template
import lynxmotion
import behaviors


run(reloader=False, host='localhost', port=8080, server='cherrypy')