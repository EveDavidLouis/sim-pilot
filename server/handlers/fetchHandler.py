from tornado import httpclient

class AsyncFetchClient():

	client = httpclient.AsyncHTTPClient()

	async def asyncFetch(self,request):

		#client = httpclient.AsyncHTTPClient()
		response = await self.client.fetch(request['url'],validate_cert=False,raise_error=False,**request['kwargs'])
		#client.close()
		return response 

	async def asyncMultiFetch(self,requests):
		
		#client = httpclient.AsyncHTTPClient()
		responses = await [ self.client.fetch(request['url'],validate_cert=False,raise_error=False,**request['kwargs'])  for request in requests]
		#client.close()
		return responses