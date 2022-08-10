from typing import Optional
from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from graphql.type.definition import GraphQLResolveInfo
from tornado.escape import to_unicode


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node,)


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node,)


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node,)


class QueryRoot(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    all_roles = SQLAlchemyConnectionField(Role.connection)
    role = graphene.Field(Role)
    thrower = graphene.String(required=True)
    request = graphene.String(required=True)
    test = graphene.String(who=graphene.String())

    def resolve_thrower(self, info):
        raise Exception("Throws!")


    def resolve_request(self, info: GraphQLResolveInfo) -> str:
        return to_unicode(info.context.arguments["q"][0])

    def resolve_test(self, info: GraphQLResolveInfo, who: Optional[str] = None) -> str:
        return "Hello %s" % (who or "World")


class MutationRoot(graphene.ObjectType):
    write_test = graphene.Field(QueryRoot)

    def resolve_write_test(self, info: GraphQLResolveInfo) -> QueryRoot:
        return QueryRoot()


schema = graphene.Schema(query=QueryRoot, mutation=MutationRoot)

