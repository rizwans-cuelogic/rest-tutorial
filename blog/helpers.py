import requests



def generate_jwt_token(self, username, password):

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	payload = {
				'username': username,
				'password': password
			}

	protocall = 'http://'
	host = '127.0.0.1:8000'	

	return (requests.post(
				protocall + host + "/api-token-auth/",
				data=payload,
				headers=headers))