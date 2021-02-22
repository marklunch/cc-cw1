from rest_framework import serializers
from .models import Messages, Reactions, Comments
from django.contrib.auth.models import User


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = (  'title', 'body', 'expirySeconds', 'category')

        
        
class ReactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactions
        fields = ('reactor', 'message', 'reactType')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('commentor', 'message', 'comment')        