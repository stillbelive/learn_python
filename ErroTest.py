from urllib import request,error

# try:
#     response = request.urlopen('http://caiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,seq='\n')

try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)

try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)

else:
    print('request successfully')