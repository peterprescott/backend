'''
Based on qxf2's example.
'''

import graphene
from graphene import relay
from graphene_sqlalchemy import (
        SQLAlchemyObjectType,
        SQLAlchemyConnectionField,
        )
from flask_graphql_auth import (
        create_access_token,
        query_header_jwt_required,
        create_refresh_token
        )
from flask_app.models import db_session, User as UserModel

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )

class AuthMutation(graphene.Mutation):
    class Arguments():
        username = graphene.String()
        password = graphene.String()

    access_token = graphene.String()
    refresh_token = graphene.String()

    @classmethod
    def mutate(cls, _, infor, username, password):
        # TODO: add conditional access
        # if user is authenticated and authorized
        return AuthMutation(
                access_token = create_access_token(username),
                referesh_token = create_refresh_token(username)
                )

class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(User.connection)
    # etcetera etcetera. TODO: FINISH!

schema = graphene.Schema(query=Query, mutation=Mutation)
