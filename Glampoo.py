import facebook 
import requests
import json
import time 
from dotenv import load_dotenv
import os

load_dotenv()

Page_Token = os.getenv("Page_Token")
PAGE_ID = os.getenv("PAGE_ID")
POST_ID_TO_MONITOR = os.getenv("POST_ID_TO_MONITOR")

# So that we can use it more easier

COMBINED_POST_ID_TO_MONITOR = '%s_%s' % (PAGE_ID, POST_ID_TO_MONITOR)

graph = facebook.GraphAPI(Page_Token)

class caivy_comment:
	def __init__(self):
		pass
	# Getting the reply of the comment data so that we can check on ^^^^						
	def monitor_reply_comment(self, reply_comment):
		reply_comment = graph.get_connections(reply_comment,"comments",order='reverse_chronological')
		for i in reply_comment['data']:
			return i['from']['id']

	# Private Reply with comment_id
	def private_reply(self, comment_ids):
		# Defining the facebook graph api url + access token
		url = "https://graph.facebook.com/v12.0/" + PAGE_ID + "/messages?access_token=" + Page_Token
		# The message where you will private reply the user 
		message = """តម្លៃប្រូម៉ូសិន
	- ១ទីប 15$ បង/អូន អាចប្រើបានពី១ខែទៅ២ខែ។
	- ទិញ១ ថែម១ ។
	- ដឹកជូនដល់កន្លែង គ្រប់ទីតាំងទូទាំងប្រទេស។"""
		# Specify the comment_id + the message variable ^^^
		params = {
		"recipient": {
			"comment_id": comment_ids
		},
		"message": {
			"text": message
		}
	}
		# Make a post requests to the api using the parameters above
		request = requests.post(url=url, json=params)
		# Printing the request log
		print(request.text)

	# Make a put request to facebook 
	# Reply to the user 
	def reply_comment(self, data):
		graph.put_object(data,"comments", message="សូមជួយឆែកសារ 😍")

	# A Method for running the bot
	def bot_on(self):
		while True:
			print("Bot is monitoring comments")
			time.sleep(1)
			comment_data = graph.get_connections(COMBINED_POST_ID_TO_MONITOR,"comments",order='chronological')
			# This loop in interation of the data structure 'data''id'
			for i in comment_data['data']:
				comment_id = i['id']
				
				# The reply id of the variable comment_id
				reply_data = self.monitor_reply_comment(comment_id)
				
				# Checking if the reply id match the Page_ID and if so print the statment
				if reply_data == PAGE_ID:
					time.sleep(1)
					print("Comment has already been replies: " + comment_id)
				
				# Else it will Reply to the comment_id and private_reply the user that just commented
				else:
					self.reply_comment(comment_id)
					print("Reply Comment to " + comment_id)
					time.sleep(1)
					self.private_reply(comment_id)

def main():
	caivy = caivy_comment()
	caivy.bot_on()


if __name__ == "__main__":
	main()

