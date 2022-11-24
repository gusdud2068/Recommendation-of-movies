from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


@api_view(["POST"])
def signup(request):
    password = request.data.get("password")
    password_confirm = request.data.get("passwordConfirm")
    if password != password_confirm:
        return Response(
            {"error : 비밀번호가 일치하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = UserSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def follow(request, user_id):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         person = User.objects.get(pk=user_id)
#         if person != request.user:
#             if person.followers.filter(pk=request.user.pk).exists():
#                 person.followers.remove(request.user)
#                 is_followed = False
#                 followers_count = person.followers.count()
#             else:
#                 person.followers.add(request.user)
#                 is_followed = True
#                 followers_count = person.followers.count()

#             return Response({'is_followed': is_followed, 'followers_count': followers_count}, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "자기 자신은 팔로우 할 수 없습니다."}, status=status.HTTP_200_OK)
#     else:
#         return Response({'message': '로그인 후 이용가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)

