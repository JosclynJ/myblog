from rest_framework import serializers
from artikels.models import ArtikelBlog

class ArtikelBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtikelBlog
        fields = ['id', 'kategori', 'judul', 'konten', 'gambar', 'status', 'created_at', 'created_by']
        # fields = "__all__"