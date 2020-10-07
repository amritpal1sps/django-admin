import graphene
from graphene_django import DjangoObjectType
from secret.models import Friends
from django.db.models import Q


class FriendsType(DjangoObjectType):
    class Meta:
        model = Friends

class Query(graphene.ObjectType):
    friend_list = graphene.List(FriendsType,search=graphene.String(), first=graphene.Int(),
        skip=graphene.Int())
    me=graphene.Field(FriendsType)
    def resolve_friend_list(self, info,search=None, first=None, skip=None, **kwargs):
        all_friends = Friends.objects.all()
        if search:
            print('search arg is passed')
            return all_friends.filter(Q(name__icontains= search) | Q(department__icontains=search))

        if first:
            all_friends=all_friends[:first]

        if skip:
            all_friends=all_friends[skip:]



        return all_friends




    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user


# class FriendsInput(graphene.InputObjectType):
#     name= graphene.String()
#     age=graphene.Int()
#     department=graphene.String()
  
class CreateFriends(graphene.Mutation):
    class Arguments:
        name= graphene.String(required= True)
        age=graphene.Int()
        department=graphene.String()
        # input=FriendsInput(required= True)
    
    friend = graphene.Field(FriendsType)

    # def mutate(root,info,input):
    #     friend_instance =Friends(name= input.name,age=input.age, department= input.department)
    def mutate(root,info,name,age,department):
        friend_instance =Friends(name= name,age=age, department=department)
        friend_instance.save()
        return CreateFriends(friend=friend_instance)

class UpdateFriend(graphene.Mutation):
    class Arguments:
        id= graphene.Int(required=True)
        name= graphene.String(required= True)
        age=graphene.Int()
        department=graphene.String()

    friend = graphene.Field(FriendsType)

    def mutate(root,info,name,id):
        friend_instance= Friends.objects.get(pk=id)
        if friend_instance:
            friend_instance.name= name
            friend_instance.save()
            return UpdateFriend(friend=friend_instance)
        else:
            return UpdateFriend(friend="id not found")



class Mutation(graphene.ObjectType):
    create_friends = CreateFriends.Field()
    update_friend  = UpdateFriend.Field()











