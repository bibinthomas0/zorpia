from ..models import post_collection, Comments, Follow
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PostSerializer, CalloutSerializer, FollowSerializer
from bson import ObjectId
import json
from bson import json_util
from datetime import datetime
from bson import ObjectId


class CreatePost(APIView):
    def post(self, request):
        data = request.data
        date = datetime.now()
        data["created_at"] = date
        user = data['user']
        data["likes"] = []
        data["active"] = True
        type = data["type"]
        if type == "profile photo":
            post_collection.find_one_and_update(
                {"$and":  [{"user":user},{"type": "profile photo"},{"active":True}]} , {"$set": {"active": False}}
            )
        elif type == "cover photo":
            post_collection.find_one_and_update(
              {"$and":  [{"user":user},{"type": "cover photo"},{"active":True}]}, {"$set": {"active": False}}
            )
        post_collection.insert_one(data)
        return Response(status=status.HTTP_201_CREATED)


class PostListView(APIView):
    def get(self, request):
        posts_cursor = post_collection.find().sort("created_at", -1)
        posts_data = []
        for post in posts_cursor:
            post["_id"] = str(post["_id"])
            posts_data.append(post)
        return Response(
            posts_data, status=status.HTTP_200_OK, content_type="application/json"
        )


class PostLikeView(APIView):
    def post(self, request):
        liked_post = request.data["post"]
        liked_by = request.data["user"]
        liked_post_oid = ObjectId(liked_post)
        post = post_collection.find_one({"_id": liked_post_oid, "likes": liked_by})
        if post:
            update_query = {"$pull": {"likes": liked_by}}
        else:
            update_query = {"$push": {"likes": liked_by}}
        post_collection.find_one_and_update({"_id": liked_post_oid}, update_query)
        if post:
            return Response(status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status.HTTP_202_ACCEPTED)


class CommentCreate(APIView):
    def post(self, request):
        request.data["created_at"] = datetime.now()
        d = Comments.insert_one(request.data)
        return Response(status.HTTP_201_CREATED)


class CommentList(APIView):
    def get(self, request):
        post_id = request.query_params.get("id")
        if post_id is not None:
            data_cursor = Comments.find({"post_id": post_id}).sort("created_at", -1)
            comment_data = []
            for data in data_cursor:
                data["_id"] = str(data["_id"])
                timestamp = datetime.fromisoformat(str(data["created_at"]))
                formatted_timestamp = timestamp.strftime("%Y-%m-%d %I:%M:%S %p")
                data["created_at"] = formatted_timestamp
                comment_data.append(data)
            return Response(comment_data, status.HTTP_200_OK)
        else:
            return Response(
                {"error": 'Missing or invalid "id" parameter'},
                status.HTTP_400_BAD_REQUEST,
            )


class AddCallout(APIView):
    def post(self, request):
        serializer = CalloutSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class FollowManagementApi(APIView):
    def post(self, request):
        followed_user = request.data.get("followed_user")
        following_user = request.data.get("following_user")
        print(followed_user, following_user)
        the_user = Follow.find_one(
            {
                "user": followed_user,
                "followers": {"$elemMatch": {"$eq": following_user}},
            }
        )
        print(the_user)
        f_user = Follow.find_one({"user": followed_user})
        s_userr = Follow.find_one({"user": following_user})
        try:
            if the_user:
                Followers_update_query = {"$pull": {"followers": following_user}}
                following_update_query = {"$pull": {"following": followed_user}}
                print("kk")
            else:
                Followers_update_query = {"$push": {"followers": following_user}}
                following_update_query = {"$push": {"following": followed_user}}
                print("gg")
                if not f_user:
                    Follow.insert_one({"user": followed_user})
                if not s_userr:
                    Follow.insert_one({"user": following_user})

            Follow.find_one_and_update({"user": followed_user}, Followers_update_query)
            Follow.find_one_and_update({"user": following_user}, following_update_query)
            print("done")
            return Response(status.HTTP_202_ACCEPTED)
        except:
            return Response(status.HTTP_406_NOT_ACCEPTABLE)


class ProfileImage(APIView):
    def post(self, request):
        user = request.data['username']
        photos = (
            post_collection.find_one({"$and":  [{'user':user},{"type": "profile photo"},{"active":True}]})
        )
        if photos:
            data = photos["image"]
            return Response(data, status.HTTP_202_ACCEPTED)
        else:
            return Response(status.HTTP_204_NO_CONTENT)


class CoverImage(APIView):
    def post(self, request):
        user = request.data['username']
        photos = (
            post_collection.find_one({"$and":  [{'user':user},{"type": "cover photo"},{"active":True}]})
        )
        if photos:
            data = photos["image"] 
            return Response(data, status.HTTP_202_ACCEPTED)
        else:
            return Response(status.HTTP_204_NO_CONTENT)

class ProfilePostListView(APIView):
    def post(self, request):
        username = request.data["username"]
        posts_cursor = post_collection.find({"user":username}).sort("created_at", -1)
        posts_data = []
        for post in posts_cursor:
            post["_id"] = str(post["_id"])
            posts_data.append(post)
        return Response(
            posts_data, status=status.HTTP_200_OK, content_type="application/json"
        )
class FollowPostChecking(APIView):
    def post(self, request):
        user = request.data.get('user')
        author = request.data.get('author')

        data = Follow.find_one({'$and': [{'user': user}, {'following': {'$in': [author]}}]})

        if data:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class FollowingUsers(APIView):
    def post(self,request):
        user = request.data['user']
        datas = Follow.find_one({'user':user})
        data = datas['following']
        print(data)
        return Response(data=data,status=status.HTTP_202_ACCEPTED) 
    
class FollowersUsers(APIView):
    def post(self,request):
        user = request.data['user']
        datas = Follow.find_one({'user':user})
        data = datas['followers']
        print(data)
        return Response(data=data,status=status.HTTP_202_ACCEPTED) 