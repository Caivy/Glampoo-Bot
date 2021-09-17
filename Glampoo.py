import facebook 
import requests
import json
import time 

Page_Token = "EAAFaTWn583kBAErrB8CvAF7RSeVjmgEaXM95hPO6pl9Jwkch3OfHuzEFHH65dZAGf6dghevc9d6OOdMieBCCz0ObXwGAydHqWg4r9xic9YooTnrTvyhtPUJeF89xZBbdUy1GKqCszq0AZBUH45tVxVHAwYuHW6sEb6tyaKz1gkKgroRndNo"
PAGE_ID = "112583993849066"
POST_ID_TO_MONITOR = "324876845953112"
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
			print("Reply to comment")

def monitor_reply_comment(data):
	reply_comment = graph.get_connections(data,"comments",order='reverse_chronological')
	# for reply in reply_comment['data']:
	# 	data_reply = reply_comment['data'][0]['created_time']['from']['id']
	# print(data_reply)
	# for i in reply_comment:
	# 	print (i['id'])
	for i in reply_comment['data']:
		return i['from']['id']
	

def monitor_comment():
	# while True:
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
main()
