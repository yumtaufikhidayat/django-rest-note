from rest_framework.reverse import reverse
from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'tags', 'createdAt', 'updatedAt', 'links']

    def get_links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "create",
                "href": reverse('note-list', request=request),
                "action": "POST",
                "types": ["application/json"]
            },
            {
                "rel": "self",
                "href": reverse('note-detail', kwargs={'pk': str(obj.pk)}, request=request),
                "action": "GET",
                "types": ["application/json"]
            },
            {
                "rel": "update",
                "href": reverse('note-detail', kwargs={'pk': str(obj.pk)}, request=request),
                "action": "PUT",
                "types": ["application/json"]
            }
        ]
