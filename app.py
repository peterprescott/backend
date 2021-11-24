import os

import git
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, you can now POST'

@app.route('/git', methods=['GET','POST'])
def pull():
    repo = git.Repo(os.path.join('~','backend'))
    repo.remotes.origin.pull()
    return 'Updated'
