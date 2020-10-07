import graphene
import secret.schema
import secret.schema_relay
import graphql_jwt
import api.schema


class Query(secret.schema.Query, secret.schema_relay.RelayQuery,api.schema.Query, graphene.ObjectType):
    pass

class Mutation(secret.schema.Mutation, api.schema.Mutation,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    # pass


schema = graphene.Schema(query=Query,mutation=Mutation,auto_camelcase=False)