###REST API
This app implements a RESTful API which enables non-browser clients to carry out authenticated operations on the Vehicle Management System. You can perform operations by simply sending HTTP requests to a running VMS server. 

####Authentication
Clients are authenticated using `TokenAuthnetication`. To recieve a token send a POST request to `http://whateverhost:8000/rest/api-token-auth/` with parameters `username` and `password`. If successful the API will return a JSON response with the `token` field conataining the required token. You can use this token to authenticate all your requests to the API. This should be done by sending your token with the `WWW-Authenticate` header in your request, in the following format: 

`WWW-Authenticate: Token your-token`

(your-token is to be replaced by your actual token)  