'''
Run Flask app.
'''

import os

import git
from flask import Flask
from flask_graphql_auth import (
        AuthInfoField,
        GraphQLAuth,
        get_jwt_identity,
        get_raw_jwt,
        create_access_token,
        create_refresh_token,
        query_jwt_required,
        mutation_jwt_refresh_token_required,
        mutation_jwt_required,
        )
from flask_graphql import GraphQLView
from app.models import db_session
from app.schema import schema
from app.secret import JWT_SECRET_KEY

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['REFRESH_EXP_LENGTH'] = 30
app.config['ACCESS_EXP_LENGTH'] = 10
auth = GraphQLAuth(app)
app.add_url_rule('/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,
            )
        )

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/git', methods=['GET','POST'])
def pull():
    repo = git.Repo(os.path.join('~','backend'))
    repo.remotes.origin.pull()
    return 'Updated'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=='__main__':
    app.run()
