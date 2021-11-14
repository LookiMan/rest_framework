from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


@api_view(['GET'])
def detail_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(f'Post with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    except:
        return Response('Unclassified error', status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes((IsAuthenticated,))
def update_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(f'Post with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    except:
        return Response('Unclassified error', status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        serializer = PostSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# @permission_classes((IsAuthenticated,))
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(f'Post with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    except:
        return Response('Unclassified error', status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        post.delete()
        return Response(f'Deleted post with id {id}')


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def vote_for_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(f'Post with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    except:
        return Response('Unclassified error', status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        post.votes += 1
        post.save(update_fields=['votes'])

        return Response(f'Succesfuly voted for post with id {id}')


@api_view(['GET'])
def detail_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(f'Comment with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    except:
        return Response('Unclassified error', status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def create_comment(request):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes((IsAuthenticated,))
def update_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except:
        return Response(f'Comment with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    else:
        serializer = CommentSerializer(instance=comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# @permission_classes((IsAuthenticated,))
def delete_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(f'Comment with id {id} does not exist', status=HTTP_400_BAD_REQUEST)
    except:
        return Response('Unclassified error', status=HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        comment.delete()
        return Response(f'Deleted comment with id {id}')
