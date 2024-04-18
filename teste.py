import requests

#bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRhZXNrayIsImlkIjoyLCJyb2xlIjoiU1RVREVOVCIsImlhdCI6MTcxMzQ1OTE2NCwiZXhwIjoxNzEzNTQ1NTY0fQ.GIAtTKcfjQ4CZqtAGUdxrcR0jRt9aT_6UBoqP_9DkdU'


with open('token.txt', 'r') as file:
    bearer_token = file.read()
    headers = {"Authorization": f"Bearer {bearer_token}"}

re = requests.get('http://a352189960f3d40cb8a56a6ae34ef5b6-58486820.us-east-1.elb.amazonaws.com/api/v1/profile',
                   headers=headers)

print(re)