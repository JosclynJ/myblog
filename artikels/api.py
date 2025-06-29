from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from artikels.models import ArtikelBlog
from artikels.serializers import ArtikelBlogSerializer

@api_view(['GET'])
def api_artikel_blog_list(request):
    artikel = ArtikelBlog.objects.all()
    serializer = ArtikelBlogSerializer(artikel, many=True)
    content = {
        "message":"berhasil",
        "records":artikel.count(),
        "rows":serializer.data
    }
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_artikel_blog_tambah(request):
    data = request.data.copy()

    serializer = ArtikelBlogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Artikel berhasil ditambahkan",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Gagal menambahkan artikel",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def api_artikel_blog_update(request, id_artikel):
    artikel = get_object_or_404(ArtikelBlog, id=id_artikel)

    data = request.data.copy()
    serializer = ArtikelBlogSerializer(instance=artikel, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Artikel berhasil diperbarui",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "message": "Gagal memperbarui artikel",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_artikel_blog_delete(request, id_artikel):
    try:
        artikel = get_object_or_404(ArtikelBlog, id=id_artikel)
        artikel.delete()
        content = {
            "message": "artikel success didelete"
        }
        status_code = status.HTTP_200_OK
    except:
        content = {
            "message": "artikel gagal didelete"
        }
        status_code = status.HTTP_400_BAD_REQUEST

    return Response(content, status=status_code)
