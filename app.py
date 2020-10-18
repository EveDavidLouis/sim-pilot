#!/usr/bin/python
import os
import logging
import json

from tornado import ioloop, web
from motor.motor_tornado import MotorClient
from server import config
from server.handlers import webHandler

logger = logging.getLogger('app')
logging.basicConfig(level=logging.WARNING)

class Application(web.Application):

	def __init__(self):
		handlers = [
			(r"/images/(.*)"        , web.StaticFileHandler,{'path': 'docs/images'}),
			(r"/templates/(.*)"     , web.StaticFileHandler,{'path': 'docs/templates'}),
			(r"/styles/(.*)"        , web.StaticFileHandler,{'path': 'docs/styles'}),
			(r"/scripts/(.*)"       , web.StaticFileHandler,{'path': 'docs/scripts'}),
			(r"/dbTest(.*)"         , webHandler.DbTestHandler),
			(r"/json(.*)"           , webHandler.DefaultJSONHandler),
			(r"/(.*)"               , webHandler.DefaultHTMLHandler),
			]
		settings = dict(
			cookie_secret=config.server['secret'],
			template_path=os.path.join(os.path.dirname(__file__),'server/templates'),
			static_path=os.path.join(os.path.dirname(__file__), 'docs'),
			static_url_prefix='/static/',
			xsrf_cookies=False,
			debug=False,
			autoreload=True,	
			)
		super(Application, self).__init__(handlers, **settings)

if __name__ == '__main__':

	# application
	app = Application()

	# modules
	app.settings['co'] = config
	#app.settings['db'] = MotorClient(config.mongodb['url'])[config.mongodb['db']]
	app.settings['db'] = MotorClient(config.mongodb['url'])[config.mongodb['db']]
	
	# listen
	app.listen(config.server['port'], config.server['host'])
	logger.warning(config.server['host'] + ':' + str(config.server['port']))

	# starting IOLoop
	ioloop.IOLoop.instance().start()