import json
from tornado import web

class DefaultHTMLHandler(web.RequestHandler):
	async def get(self, *args, **kwargs):
		data = "DefaultHTMLHandler"
		self.write(str(data))
		self.finish()

class DefaultJSONHandler(web.RequestHandler):
	async def get(self,args):
		data = {'DefaultJSONHandler':args}
		self.write(json.dumps(data))
		self.finish()
