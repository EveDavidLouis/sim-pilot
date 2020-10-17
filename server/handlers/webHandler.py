class DefaultHTMLHandler(web.RequestHandler):
	@gen.coroutine
	def get(self,args):
		self.write(self.render('../../docs/index.html'))
		self.finish()

class DefaultJSONHandler(web.RequestHandler):
	@gen.coroutine
	def get(self,args):
    data = {}
		self.write(json.dumps(data))
		self.finish()
