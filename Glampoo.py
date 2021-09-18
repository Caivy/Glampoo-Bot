import facebook 
import requests
import json
import time 
from dotenv import load_dotenv
import os
from logging import log

load_dotenv()
Page_Token = os.getenv("Page_Token")
PAGE_ID = os.getenv("PAGE_ID")
POST_ID_TO_MONITOR = os.getenv("POST_ID_TO_MONITOR")

COMBINED_POST_ID_TO_MONITOR = '%s_%s' % (PAGE_ID, POST_ID_TO_MONITOR)

graph = facebook.GraphAPI(Page_Token)

def reply_comment(data):
 	graph.put_object(data,"comments", message="សូមជួយឆែកសារ 😍")

def main():
	while True:
		data_comment = monitor_comment()
		comment_reply_id = monitor_reply_comment(data_comment)
	
		if comment_reply_id == "112583993849066":
			print("Comment has already been replies")
		else:
			reply_comment(data_comment)
			print("Reply Comment")
			time.sleep(1)
			private_reply(data_comment)
			

def monitor_reply_comment(data):
	reply_comment = graph.get_connections(data,"comments",order='reverse_chronological')
	for i in reply_comment['data']:
		return i['from']['id']
	
def monitor_comment():
		print("Bot is monitoring comments")
		time.sleep(5)
		comment_data = graph.get_connections(COMBINED_POST_ID_TO_MONITOR,"comments",order='reverse_chronological')
		commends = []
		for comment in comment_data['data'][:10]:
			commends.append (comment)
		data = commends[0]['id']
		data_converted = str(data)
		#time.sleep(5)
		print(data)
		return data_converted
def private_reply(comment_ids):
	url = "https://graph.facebook.com/v12.0/me/messages?access_token=" + Page_Token
	multi_string = """តម្លៃប្រូម៉ូសិន
- ១ទីប 15$ បង/អូន អាចប្រើបានពី១ខែទៅ២ខែ។
- ទិញ១ ថែម១ ។
- ដឹកជូនដល់កន្លែង គ្រប់ទីតាំងទូទាំងប្រទេស។"""
	params = {
    "recipient": {
        "comment_id": comment_ids
    },
    "message": {
        "text":multi_string
    }
}
	request = requests.post(url=url, json=params)
	print(request.text)

if __name__ == "__main__":
	main()

