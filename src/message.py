
from re import L
import facebook
import Glampoo as bot
import requests
import json



page_token = "EAAH7MeZCSgQsBAKfXmmXQkBSKIaZB3fq1NdmThubW7nyRL5IZC0ZCZBA2L98V4YQvOPYL8x9XRSmcCVcD6ZBh5rHnZBhmvr4kZBM5MfMYmuZCjGZBGx82J4meZBbm1hZCslj9rTZAbkmb3PdiMygh3yyIVOipszOSP2K5fUXeMZBOianEhDt98K6CYHJsbcp2BKhZAlOHwZD"
page_id = "108201381614660"

graph_api = facebook.GraphAPI(page_token)

def send_message():
    url = "https://graph.facebook.com/v12.0/" + page_id + "/messages?access_token=" + page_token
    params = {
        "messaging_type": "MESSAGE_TAG",
        "tag": "ACCOUNT_UPDATE", 
        "recipient":{
        "id": "4511477272224365"
        },
        "message":{
        "text":"hello, world!"
        }
    }
    request = requests.post(url=url, json=params)
    print(request.text)

def fetch_id():
    conversation_id = graph_api.get_connections(page_id, 'conversations', field=id)
    conversation = []
    for i in conversation_id['data'][:10]:
        conversation.append (i)
	
    data = conversation[0]['id']
    

    # url_1 = "https://graph.facebook.com/v12.0/"+ data + "/messages?access_token=" + page_token
    # params_1 = {
    #     "field": "messsage"
    # }
    # request_1 = requests.get(url=url_1, json=params_1)
    # print(request_1.text)
    
def fetch_participants_id(fields):
    url = "https://graph.facebook.com/v12.0/" + page_id + "/conversations?fields="+ fields 
    token = "&access_token=" + page_token
    t = requests.get(url=url, params=token)
    data = t.json()
    
    one = data['data']
    # This will get the data in participants after that data and the list 'id' which is our user_id
    participants_id = one[0]['participants']['data'][0]['id']
    
    return participants_id
    
    #print(participants)
    # for i in data['data'][:10]:
    #     # parti = i['participants']['data']
    #     # for k in parti:
    #     # value.append(i)
    #     # print(value[0]['id'])
        
    #     participants = i['participants']
    #     print(participants['data'])
    #     # data_1 = data[0]['id']
    #     # data_2 = data[1]['id']
    #     print(data)
        # line = datas.partition('\n')[0]
        # print(datas.split("\n")[0])
        #for t in data:
            # data_id.append(t['id'])
            # print(data_id)
        # print(participants)
        # print(data)
    
    
def main():
    #send_message()
    fetch_participants_id("participants")


if __name__ == "__main__":
    main()
