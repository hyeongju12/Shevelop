import requests

JWT_TOKEN = (
	"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
	"eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imh5ZW9uZ2p1IiwiZXhwIjoxNjUzMjE3Njk5LCJlbWFpbCI6IiJ9."
	"ORXq7zM0i1uFkMVGvZJgWvMkEmRhndWPeD2mB0xo7V8"
)
headers = {
	'Authorization' : f'JWT {JWT_TOKEN}'
}

res = requests.get("http://localhost:8000/shareinfo/post/2/", headers=headers)
print(res.json())