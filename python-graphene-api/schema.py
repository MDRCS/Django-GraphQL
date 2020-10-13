import graphene
import json

class Query(graphene.ObjectType):
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

schema = graphene.Schema(query=Query, auto_camelcase=False) # auto_camelcase when it's on False, so all queries should be written in snakecase (is_admin).

result = schema.execute(
    '''
    {
        hello
    }
    '''
)

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))

result = schema.execute(
    '''
    {
        is_admin
    }
    '''
)

# snake case vs Camel Case
# if we enter is_admin attribute in the schema to see if admin or not we will have an error,
# instead we should change is_admin to isAdmin (CamelCase) without that, it won't work.

dictResult = dict(result.data.items())

print(json.dumps(dictResult, indent=2))
