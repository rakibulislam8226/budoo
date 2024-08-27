from channels.generic.websocket import AsyncWebsocketConsumer
import json

class StatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'status_updates'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def status_update(self, event):
        status = event['status']
        user = event['user']

        await self.send(text_data=json.dumps({
            'status': status,
            'user': user
        }))
