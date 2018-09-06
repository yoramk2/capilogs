#!/usr/bin/env python
import wrapt
import datetime
import os
import re
import uuid
import time
import socket


"""
	Wrap all Lambda invocations and prints a log before calling it.
	
	{
	u'body': None, 
	u'resource': u'/{proxy+}', 
	u'requestContext': {
		u'requestTime': u'29/Aug/2018:12:08:26 +0000', 
		u'protocol': u'HTTP/1.1', 
		u'resourceId': u'fadq07', 
		u'apiId': u'lzeig1o6l6', 
		u'resourcePath': u'/{proxy+}', 
		u'httpMethod': u'GET', 
		u'requestId': u'3baff547-ab84-11e8-8c32-fbaaf2440742', 
		u'extendedRequestId': u'MYrtEF3IoAMFdRw=', 
		u'path': u'/yor_dev/upc/0887276201993/', 
		u'stage': u'yor_dev', 
		u'requestTimeEpoch': 1535544506022, 
		u'identity': {
			u'userArn': None, 
			u'cognitoAuthenticationType': None, 
			u'accessKey': None, 
			u'caller': None, 
			u'userAgent': u'python-requests/2.18.4', 
			u'user': None, 
			u'cognitoIdentityPoolId': None, 
			u'cognitoIdentityId': None, 
			u'cognitoAuthenticationProvider': None, 
			u'sourceIp': u'52.3.249.158', 
			u'accountId': None
			}, 
		u'accountId': u'510393669663'
		}, 
	u'queryStringParameters': {
		u'search': u'', 
		u'curr': u'USD', 
		u'd': u'e7771599-2177-44c7-b640-c1564774f09c', 
		u'pid': u'94f0d99d-2d9b-415d-b046-48dbf7412a7f', 
		u'jwt': u'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpcCI6IjYyLjIxOS4yMzcuMTcwIn0.sha-XZu6J3BFnASeAsXZJg5NZOxoqmeYMAkKhlPnK8I', 
		u'limit': u'5', 
		u'skip': u'0', 
		u'_': u'1535544482816'
		}, 
	u'httpMethod': u'GET', 
	u'pathParameters': {
		u'proxy': u'upc/0887276201993'
		}, 
	u'headers': {
		u'Via': u'1.1 c7e9845a8e7864e58e8dc46809f0d30f.cloudfront.net (CloudFront)', 
		u'CloudFront-Is-Desktop-Viewer': u'true', 
		u'CloudFront-Is-SmartTV-Viewer': u'false', 
		u'CloudFront-Forwarded-Proto': u'https', 
		u'aws_request_id': u'3b9ce23f-ab84-11e8-9ffd-7314d47057b5', 
		u'CloudFront-Viewer-Country': u'US', 
		u'x-user-agent': u'webfront-dev1:/dev1/rupc/0887276201993/:GET:38f8', 
		u'Accept': u'*/*', 
		u'User-Agent': u'python-requests/2.18.4', 
		u'X-Amzn-Trace-Id': u'Root=1-5b868cba-303f293237cade99dc580ae7', 
		u'debug-log-enabled': u'false', 
		u'Host': u'lzeig1o6l6.execute-api.us-east-1.amazonaws.com', 
		u'X-Forwarded-Proto': u'https', 
		u'X-Amz-Cf-Id': u'f-PB22vme6poGOPk2GNr_JqfRHhnnIJOE7SrAas7KH0f55tsVYWQAw==', 
		u'CloudFront-Is-Tablet-Viewer': u'false', 
		u'X-Forwarded-Port': u'443', 
		u'x-correlation-id': u'3b83db53-ab84-11e8-8a6f-6dce0c1c5074', 
		u'CloudFront-Is-Mobile-Viewer': u'false', 
		u'X-Forwarded-For': u'52.3.249.158, 52.46.14.66', 
		u'Accept-Encoding': u'gzip, deflate'
		}, 
	u'stageVariables': None, 
	u'path': u'/upc/0887276201993/', 
	u'isBase64Encoded': False
	}
		
	{
	u'body': None, 
	u'resource': u'/', 
	u'requestContext': {
		'requestTime': u'29/Aug/2018:15:36:23 +0000', 
		u'protocol': u'HTTP/1.1', 
		u'resourceId': u'7wqq3uvpqa', 
		u'apiId': u'lzeig1o6l6', 
		u'resourcePath': u'/', 
		u'httpMethod': u'GET', 
		u'requestId': u'489ea191-aba1-11e8-8bb7-b7760df8feba', 
		u'extendedRequestId': u'MZKKnEWgIAMF7yg=', 
		u'path': u'/yor_dev', 
		u'stage': u'yor_dev', 
		u'requestTimeEpoch': 1535556983124, 
		u'identity': {
			u'userArn': None, 
			u'cognitoAuthenticationType': None, 
			u'accessKey': None, 
			u'caller': None, 
			u'userAgent': u'python-requests/2.18.4', 
			u'user': None, 
			u'cognitoIdentityPoolId': None, 
			u'cognitoIdentityId': None, 
			u'cognitoAuthenticationProvider': None, 
			u'sourceIp': u'62.219.237.170', 
			u'accountId': None
			}, 
		u'accountId': u'510393669663'
		}, 
	u'queryStringParameters': None, 
	u'httpMethod': u'GET', 
	u'pathParameters': None, 
	u'headers': {
		u'Via': u'1.1 ad93a72606d0015c6aa5ceae5dc8a8d5.cloudfront.net (CloudFront)', 
		u'Accept-Encoding': u'gzip, deflate', 
		u'CloudFront-Is-SmartTV-Viewer': u'false', 
		u'CloudFront-Forwarded-Proto': u'https', 
		u'X-Forwarded-For': u'62.219.237.170, 52.46.26.17', 
		u'CloudFront-Viewer-Country': u'IL', 
		u'Accept': u'*/*', 
		u'User-Agent': u'python-requests/2.18.4', 
		u'X-Amzn-Trace-Id': u'Root=1-5b86bd77-f92bc2fc70991668e74a6ea8', 
		u'Host': u'lzeig1o6l6.execute-api.us-east-1.amazonaws.com', 
		u'X-Forwarded-Proto': u'https', 
		u'X-Amz-Cf-Id': u'Dg2rjkpxokJ9IQJEPj3MzxXVoYaoiznNBhUWs831Gg-4sMqmIXd32g==', 
		u'CloudFront-Is-Tablet-Viewer': u'false', 
		u'X-Forwarded-Port': u'443', 
		u'CloudFront-Is-Mobile-Viewer': u'false', 
		u'CloudFront-Is-Desktop-Viewer': u'true'
		}, 
	u'stageVariables': None, 
	u'path': u'/', 
	u'isBase64Encoded': False
	}
	
	return:
	{
	u'body': u'eyJsYXN0X2V2YWx1YXRlZF9rZXkiOm51bGwsIml0ZW1zIjpbeyJhdmwiOiIxIiwic3RhdHVzIjowLCJsaW5rIjoiaHR0cDovL3JvdmVyLmViYXkuY29tL3JvdmVyLzEvNzExLTUzMjAwLTE5MjU1LTAvMT9mZjM9MiZ0b29saWQ9MTAwNDEmY2FtcGlkPTUzMzgyNDIxMTMmY3VzdG9taWQ9JmxnZW89MSZ2ZWN0b3JpZD0yMjk0NjYmaXRlbT0xODMzNjY2MDMyMjIiLCJuYW1lIjoiZWJheSIsImNvbmQiOiJOZXcgb3RoZXIgKHNlZSBkZXRhaWxzKTtQcmljZXMgdXBkYXRlZCA0IGhvdXJzIGFuZCA5IG1pbnV0ZXMgYWdvLiIsImJpZCI6Mzc5OS4wLCJfaWQiOiJlNzc3MTU5OS0yMTc3LTQ0YzctYjY0MC1jMTU2NDc3NGYwOWMiLCJ1c2VyIjoiZWJheSJ9LHsiYXZsIjoiMSIsInN0YXR1cyI6MCwibGluayI6Imh0dHA6Ly9yb3Zlci5lYmF5LmNvbS9yb3Zlci8xLzcxMS01MzIwMC0xOTI1NS0wLzE/ZmYzPTImdG9vbGlkPTEwMDQxJmNhbXBpZD01MzM4MjQyMTEzJmN1c3RvbWlkPSZsZ2VvPTEmdmVjdG9yaWQ9MjI5NDY2Jml0ZW09MTgzMzIwMzA0MzY3IiwibmFtZSI6ImViYXkiLCJjb25kIjoiTmV3O1ByaWNlcyB1cGRhdGVkIDQgaG91cnMgYW5kIDkgbWludXRlcyBhZ28uIiwiYmlkIjo0MDI5LjAsIl9pZCI6ImU3NzcxNTk5LTIxNzctNDRjNy1iNjQwLWMxNTY0Nzc0ZjA5YyIsInVzZXIiOiJlYmF5In0seyJhdmwiOiIxIiwic3RhdHVzIjowLCJsaW5rIjoiaHR0cDovL3JvdmVyLmViYXkuY29tL3JvdmVyLzEvNzExLTUzMjAwLTE5MjU1LTAvMT9mZjM9MiZ0b29saWQ9MTAwNDEmY2FtcGlkPTUzMzgyNDIxMTMmY3VzdG9taWQ9JmxnZW89MSZ2ZWN0b3JpZD0yMjk0NjYmaXRlbT0zMTIxNjE0NDg1NzgiLCJuYW1lIjoiZWJheSIsImNvbmQiOiJOZXc7UHJpY2VzIHVwZGF0ZWQgNCBob3VycyBhbmQgOSBtaW51dGVzIGFnby4iLCJiaWQiOjQyOTkuMCwiX2lkIjoiZTc3NzE1OTktMjE3Ny00NGM3LWI2NDAtYzE1NjQ3NzRmMDljIiwidXNlciI6ImViYXkifSx7ImF2bCI6IjEiLCJzdGF0dXMiOjAsImxpbmsiOiJodHRwOi8vcm92ZXIuZWJheS5jb20vcm92ZXIvMS83MTEtNTMyMDAtMTkyNTUtMC8xP2ZmMz0yJnRvb2xpZD0xMDA0MSZjYW1waWQ9NTMzODI0MjExMyZjdXN0b21pZD0mbGdlbz0xJnZlY3RvcmlkPTIyOTQ2NiZpdGVtPTE3MzQ4Njk5MTU4MSIsIm5hbWUiOiJlYmF5IiwiY29uZCI6Ik5ldztQcmljZXMgdXBkYXRlZCA0IGhvdXJzIGFuZCA5IG1pbnV0ZXMgYWdvLiIsImJpZCI6NTI5OS45NSwiX2lkIjoiZTc3NzE1OTktMjE3Ny00NGM3LWI2NDAtYzE1NjQ3NzRmMDljIiwidXNlciI6ImViYXkifSx7ImF2bCI6IjEiLCJzdGF0dXMiOjAsImxpbmsiOiJodHRwOi8vcm92ZXIuZWJheS5jb20vcm92ZXIvMS83MTEtNTMyMDAtMTkyNTUtMC8xP2ZmMz0yJnRvb2xpZD0xMDA0MSZjYW1waWQ9NTMzODI0MjExMyZjdXN0b21pZD0mbGdlbz0xJnZlY3RvcmlkPTIyOTQ2NiZpdGVtPTI2MzU0NDA1MTE1NiIsIm5hbWUiOiJlYmF5IiwiY29uZCI6Ik5ldztQcmljZXMgdXBkYXRlZCA0IGhvdXJzIGFuZCA5IG1pbnV0ZXMgYWdvLiIsImJpZCI6NTk3OS4wLCJfaWQiOiJlNzc3MTU5OS0yMTc3LTQ0YzctYjY0MC1jMTU2NDc3NGYwOWMiLCJ1c2VyIjoiZWJheSJ9LHsiYXZsIjoiMSIsInN0YXR1cyI6MCwibGluayI6Imh0dHA6Ly9yb3Zlci5lYmF5LmNvbS9yb3Zlci8xLzcxMS01MzIwMC0xOTI1NS0wLzE/ZmYzPTImdG9vbGlkPTEwMDQxJmNhbXBpZD01MzM4MjQyMTEzJmN1c3RvbWlkPSZsZ2VvPTEmdmVjdG9yaWQ9MjI5NDY2Jml0ZW09MTEzMjEyNTY5MDE1IiwibmFtZSI6ImViYXkiLCJjb25kIjoiTmV3O1ByaWNlcyB1cGRhdGVkIDQgaG91cnMgYW5kIDkgbWludXRlcyBhZ28uIiwiYmlkIjo5OTk3Ljk5LCJfaWQiOiJlNzc3MTU5OS0yMTc3LTQ0YzctYjY0MC1jMTU2NDc3NGYwOWMiLCJ1c2VyIjoiZWJheSJ9XSwidG90YWwiOjYsImxhc3RfdXBkYXRlZCI6bnVsbH0=', 
	u'headers': {
		'Content-Type': 'application/json', 
		'Content-Length': '1955', 
		'Vary': 'Accept, Accept-Language,Cookie', 
		'Allow': 'GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS', 
		'Content-Language': 'en'
		}, 
	u'isBase64Encoded': u'true', 
	u'statusCode': 200
	}


	"""
class Util:

	logprefix = None

	@staticmethod
	def get_epoch():
		return int(round(time.time() * 1000))
	
	@staticmethod
	def get_start_log_msg(event):
		"""
		Wrap all Lambda invocations and prints a log before calling it.
		
		log structure:
			1 user name - string
			2 client ip - ip address
			target domain - string
			4 target ip address - ip address
			5 target host name - string
			6 target user name - string
			7 source host name - string
			8 action return code - 1/0 or 200/400 success or failiare
			action fail code - string
			action fail desc - string
			11 action name - string
			12 action authentication code - string (code,token,else)
			13 action start time - datetime
			14 action log time - datetime
			
		"""
		if "httpMethod" in event and "requestContext" in event:
			requestContext = event["requestContext"]
			if "identity" in requestContext:
				identity = requestContext["identity"]
				if "user" in identity:
					userName = identity["user"] #1
				if "sourceIp" in identity:
					sourceIp = identity["sourceIp"] #2
				if "cognitoAuthenticationType" in identity:
					cognitoAuthenticationType = identity["cognitoAuthenticationType"] #12
				if "cognitoIdentityId" in identity:
					cognitoIdentityId = identity["cognitoIdentityId"] #6
				if "cognitoIdentityPoolId" in identity:
					cognitoIdentityPoolId = identity["cognitoIdentityPoolId"] #7
			if "requestTime" in requestContext:
				requestTimeEpoch = requestContext["requestTimeEpoch"] #13
			if "requestId" in requestContext:	
				requestId = requestContext["requestId"]
			if "headers" in event:
				headers = event["headers"]
				if "Host" in headers:
					Host = headers["Host"] #5
				#get correlation-id
				if "x-correlation-id" in headers:
					correlate_id = headers["x-correlation-id"]
				if "x-user-agent" in headers:
					user_agent = headers["x-user-agent"]
				if 'AWS_LAMBDA_FUNCTION_NAME' in os.environ:
					func_name = os.environ['AWS_LAMBDA_FUNCTION_NAME']
				else:
					if "apiId" in event["requestContext"]:
						func_name = event["requestContext"]["apiId"]
					else:
						func_name = headers["Host"]
				if "path" in event["requestContext"]:
					path = event["requestContext"]["path"] #11
				else:
					path = "path"
				if "httpMethod" in event:
					method = event["httpMethod"] #11
				else:
					if "httpMethod" in event["requestContext"]:
						method = event["requestContext"]["httpMethod"] 
					else:
						method = "method"
				host_ip = socket.gethostbyname(socket.gethostname()) #4
			msg = {"userName":userName,"sourceIp":sourceIp,"cognitoAuthenticationType":cognitoAuthenticationType,"cognitoIdentityId":cognitoIdentityId,
				"requestTimeEpoch":requestTimeEpoch,"Host":Host,"path":path,"method":method,"cognitoIdentityPoolId":cognitoIdentityPoolId,"hostIp":host_ip}
		else:
			msg = {"error":str(event)}
		return msg
		
	
	@staticmethod
	def get_finish_log_msg(event,ret):
		msg = Util.get_start_log_msg(event)
		if ret is not None and "statusCode" in ret:
			statusCode = ret["statusCode"] #8
			msg["statusCode"] = statusCode
		logTimeEpoch = Util.get_epoch() #14
		msg["logTimeEpoch"] = logTimeEpoch
		return msg
	
	@staticmethod
	def get_correlation_from_event(event):
		if Util.logprefix:
			print("cached logprefix "+Util.logprefix)
			return Util.logprefix
		correlate_id = ''
		user_agent = ''
		#from api gateway
		if "httpMethod" in event and "requestContext" in event:
			if "headers" in event:
				headers = event["headers"]
				#get correlation-id
				if "x-correlation-id" in headers:
					correlate_id = headers["x-correlation-id"]
				else:
					if "aws_request_id" in headers:
						correlate_id = headers["aws_request_id"]
					else:
						correlate_id = uuid.uuid4().__str__()
				# get user-agent = get_func_name + ':' + path + ':' + request.method + ':' + host_ip
				if "x-user-agent" in headers:
					user_agent = headers["x-user-agent"]
				else:
					if 'AWS_LAMBDA_FUNCTION_NAME' in os.environ:
						func_name = os.environ['AWS_LAMBDA_FUNCTION_NAME']
					else:
						if "apiId" in event["requestContext"]:
							func_name = event["requestContext"]["apiId"]
						else:
							func_name = headers["Host"]
					if "path" in event["requestContext"]:
						path = event["requestContext"]["path"]
					else:
						path = "path"
					if "httpMethod" in event:
						method = event["httpMethod"]
					else:
						if "httpMethod" in event["requestContext"]:
							method = event["requestContext"]["httpMethod"]
						else:
							method = "method"
					host_ip = "12.34.56.78"
					user_agent = func_name + ':' + path + ':' + method + ':' + host_ip	
		#from other source
		else:	
			if "x-correlation-id" in event:
				correlate_id = event["x-correlation-id"]
			if "x-user-agent" in event:
				user_agent = event["x-user-agent"]
			if "Debug-Log-Enabled" in event:
				debug_flag = event["Debug-Log-Enabled"]
		logprefix =  user_agent + " " + correlate_id
		Util.logprefix = logprefix
		return logprefix


def wrapper(wrapped, instance, args, kwargs):
	"""
	Wrap all Lambda invocations and prints a log before calling it.
	
	"""
	request_handler = args[0]
	def _wrapper(event, context):
		print("event="+str(event))
		logprefix = Util.get_correlation_from_event(event)
		print(logprefix+' This is a start log by instrumenter '+str(Util.get_start_log_msg(event)))
		ret = request_handler(event, context)
		print("ret=",str(ret))
		print(logprefix+' This is an end log by instrumenter '+str(Util.get_finish_log_msg(event,ret)))
		return ret
	return wrapped(_wrapper, *args[1:], **kwargs)

try:
	wrapt.wrap_function_wrapper('__main__', 'handle_event_request', wrapper)
	print("instrumenter : ok")
except Exception as e:
	print("instrumenter error :"+str(e))