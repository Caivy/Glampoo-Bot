import facebook 
import requests
import json
import time 

Page_Token = "EAAFaTWn583kBAFmkulUXCnVRSCCCuTAa1b4bdYn4OyaOKwVmDYRahYXiEjFtfQPLe7qpoaM6B8JBP7FVsKllTxkHf3g7FV8YXsFShCbtP1rtcHohrm686BKt9947svBsDWDX5TeNAzjJsvoSGwOyrfRaTNp3W4DDIfUIR3ZBCGU8Pc4mX"
PAGE_ID = "112583993849066"
POST_ID_TO_MONITOR = "304138281360302"
Page_Comment_ID = "324876845953112_360627765711353"

COMBINED_POST_ID_TO_MONITOR = '%s_%s' % (PAGE_ID, POST_ID_TO_MONITOR)

graph = facebook.GraphAPI(Page_Token)

def reply_comment(data):
	# reply = graph.put_object(parent_object=data, connection_name='comments',                         message='Test')
 	
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
	url = "https://graph.facebook.com/v12.0/me/messages?access_token=EAAFaTWn583kBAFmkulUXCnVRSCCCuTAa1b4bdYn4OyaOKwVmDYRahYXiEjFtfQPLe7qpoaM6B8JBP7FVsKllTxkHf3g7FV8YXsFShCbtP1rtcHohrm686BKt9947svBsDWDX5TeNAzjJsvoSGwOyrfRaTNp3W4DDIfUIR3ZBCGU8Pc4mX"
	params = {
    "recipient": {
        "comment_id": comment_ids
    },
    "message": {
        "text":"Testing Private_Replies"
    }
}
	request = requests.post(url=url, json=params)
	print(request.text)

main()
