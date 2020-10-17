import json , os
from tornado import web

class DefaultHTMLHandler(web.RequestHandler):
	async def get(self, *args, **kwargs):
		data = {'DefaultHTMLHandler':args}
		self.write(str(data))
		self.finish()

class DefaultJSONHandler(web.RequestHandler):
	async def get(self, *args, **kwargs):
		data = {'DefaultJSONHandler':args}
		for v in os.environ:
			data[v]=os.environ[v]
		self.write(json.dumps(data))
		self.finish()
