## Bring up Flask

#### Make docker-compose up from Search-Workshop1 and Search-Workshop2

1. Bring postgres service up from Search-Workshop1
```
cd Search-Workshop1
docker-compose up
```

2. Bring elasticsearch and kibana services up from Search-Workshop2
```
cd Search-Workshop2
docker-compose up
```

3. Bring APIs up from Search-Workshop3
```
cd Search-Workshop3
docker build -t ws3 .
docker run -p 5000:5000 "ws3:latest"
```

###### Note: 
1. Update the ip address in logstash/logstash.conf, replace '127.0.0.1' with your local system ip.
2. Update the ip address in src/app/app.py, replace '127.0.0.1' with your local system ip.
3. Please make the following changes in the Dockerfile

###### 
```
ENV POSTGRES_HOST='127.0.0.1'
In the above line replace '127.0.0.1' with your local system ip
```

Build docker image
```
docker build -t ws3 .
```
Bring up flask app
```
docker run -p 5000:5000 "ws3:latest"
```

## Make an API Request
Copy & paste the below code and run the python script.
```
import requests
import json

# This is the post API URL, use DeliveryInfo/ProductStats
url = 'http://127.0.0.1:5000/DeliveryInfo'
headers = {"Content-Type": "application/json"}

# Use the post data to make requests based on the API
post_data = {'order_id': '47770eb9100c2d0c44946d9cf07ec65d'}

# Use requets library to invoke a request
r = requests.post(
    url=url,
    headers=headers,
    data=json.dumps(post_data))
    
# print the response
print(json.dumps(r.json(), indent=4))
```

