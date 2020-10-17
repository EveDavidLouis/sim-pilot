import json
from tornado import web

class DefaultJSONHandler(web.RequestHandler):
	async def get(self,args):
		data = {'data':args}
		self.write(json.dumps(data))
		self.finish()
