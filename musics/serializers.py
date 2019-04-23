from rest_framework import serializers
from .models import Music, Artist, Comment
 
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields=('id', 'title','artist',)
        
        
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model= Artist
        fields=('id','name','music_set',)
    
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    class Meta:
        model= Artist
        fields=('id','name','music_set',)
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content',)