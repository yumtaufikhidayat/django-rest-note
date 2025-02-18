from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from notes.serializers import NoteSerializer
from .models import Note


# Create your views here.
class NoteList(APIView):
    def post(self, request):
        note = NoteSerializer(data=request.data, context={'request': request})  # Pass request context
        if note.is_valid(raise_exception=True):
            note.save()
            return Response(note.data, status=status.HTTP_201_CREATED)

        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True, context={'request': request})
        return Response({
            "notes": serializer.data
        }, status=status.HTTP_200_OK)
