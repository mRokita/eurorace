from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.gis.geos import Point
from .models import LocationReport


class LocationConsumer(AsyncJsonWebsocketConsumer):
    """
    Event handler for device location coordinates
    """
    async def connect(self):
        # Authentication would be handled here
        # For now, we'll assume the user is authenticated
        self.user = self.scope["user"]

        # Accept the connection
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive_json(self, content):
        if content.get("type", None) == "location_update":
            latitude = content["latitude"]
            longitude = content["longitude"]

            # Save location to database
            await self.save_location(latitude, longitude)

            # Send acknowledgment to the client
            await self.send_json({
                "type": "location_saved",
                "success": True
            })

    @database_sync_to_async
    def save_location(self, latitude, longitude):
        """Save the location to the database"""
        point = Point(longitude, latitude)
        LocationReport.objects.create(
            user=self.user,
            location=point
        )
