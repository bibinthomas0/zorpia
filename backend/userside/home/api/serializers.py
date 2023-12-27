from rest_framework import serializers
from home.models import post_collection, Callouts,Follow


class PostSerializer(serializers.Serializer):
    class Meta:
        model = post_collection
        fields = "__all__"


class CalloutSerializer(serializers.Serializer):
    class meta:
        model = Callouts
        fields = "__all__"
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

class FollowSerializer(serializers.Serializer):
    class meta:
        model = Follow
        fields = '__all__'

            