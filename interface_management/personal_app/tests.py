from django.test import TestCase
import requests
# Create your tests here.

# 测试登录
url = "http://localhost:8000/api/personal/user_login"
r = requests.post(url, data={"username":"admin", "password":"admin123456"})
print(r.text)


# 测试token是否生效
# url2 = "http://localhost:8000/api/personal/user_auth_test"
# headers = {'Authorization': 'token f11c9efacab8b2a824c0434897caf9baf9b8ab72'}
# #headers = {'Authorization': 'token abc'}
# r = requests.get(url2, headers=headers)
# print(r.text)
