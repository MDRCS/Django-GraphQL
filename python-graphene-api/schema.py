import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime() # createdAt in CamelCase

class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit=None): # make it optional
        return [
            User(id="1", username="Fred", created_at=datetime.now()),
            User(id="2", username="MDR", created_at=datetime.now()),
            User(id="3", username="AMINE", created_at=datetime.now())
        ][:limit]

class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()

    def mutate(self, info, username):
        user = User(id="3", username=username, created_at=datetime.now())
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation) # we can use (query=Query, mutation=Mutation, auto_camelcase=False) # auto_camelcase when it's on False, so all queries should be written in snakecase (is_admin).

# Hello field query

result = schema.execute(
    '''
    {
        hello
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))

# isAdmin field query

result = schema.execute(
    '''
    {
        isAdmin
    }
    '''
)

# snake case vs Camel Case
# if we enter is_admin attribute in the schema to see if admin or not we will have an error,
# instead we should change is_admin to isAdmin (CamelCase) without that, it won't work.

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))

# User field query with arguments

result = schema.execute(
    '''
    {
        users(limit: 2) {
          id
          username
          createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))

# User field creation.

result = schema.execute(
    '''
        mutation {
            createUser(username: "Jeff") {
                user {
                    id
                    username
                    createdAt
                }
            }

        }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))
