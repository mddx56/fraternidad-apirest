import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
		self.room_group_name = f"chat_{self.room_name}"
		self.channel_layer.group_add(self.room_group_name, self.channel_name)
		await self.accept()

	def disconnect(self, close_code):
		self.channel_layer.group_discard(self.room_group_name, self.channel_name)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]
		await self.channel_layer.group_send(
			self.room_group_name, {"type": "chat_message", "message": message}
		)

	async def chat_message(self, event):
		message = event["message"]
		await   self.send(text_data=json.dumps({"message": message}))





class NotificationConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.user = self.scope["url_route"]["kwargs"]["username"]
		self.user_notification = "notification_%s" % self.user
		# self.user_notification = None
		# user = User.objects.filter(username=self.user)
		# if user:
		# self.user_notification = 'notification_%s' % user[0].id

		# Join room group
		async_to_sync(self.channel_layer.group_add)(
			self.user_notification, self.channel_name
		)

		await self.accept()
		
	def disconnect(self, close_code):
		# Leave room group
		async_to_sync(self.channel_layer.group_discard)(
			self.user_notification, self.channel_name
		)

	# Receive message from WebSocket
	# you can do this out of consumers in function or class based views or signal or normal func
	# def receive(self, text_data):
	#     text_data_json = json.loads(text_data)
	#     notification = text_data_json['notification']

	#     # Send message to room group
	#     async_to_sync(self.channel_layer.group_send)(
	#         self.room_group_name,
	#         {
	#             'type': 'notifications',
	#             'notification': notification
	#         }
	#     )

	# Receive message from room group
	async def push_notification(self, event):
		title = event["title"]
		body = event["body"]
		created = event["created"]
		status = event["status"]

		# Send message to WebSocket
		await self.send(
			text_data=json.dumps(
				{"title": title, "body": body, "created": created, "status": status}
			)
		)

