from tornado import web

class DefaultHTMLHandler(web.RequestHandler):
	async def get(self,args):
		self.write(self.render('../../docs/index.html'))
		self.finish()

class DefaultJSONHandler(web.RequestHandler):
	async def get(self,args):
		data = {}
		self.write(json.dumps(data))
		self.finish()
