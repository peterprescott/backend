# backend

This is an example of a Flask backend, set up to run on PythonAnywhere's
free cloud service, with automatic updates whenever new changes are
pushed to GitHub, as suggested by [Bajpai
(2019)](https://medium.com/@aadibajpai/deploying-to-pythonanywhere-via-github-6f967956e664).

Basically, make a new user account on PythonAnywhere, deploy a Flask web
app, use a PythonAnywhere bash console to replace the default app with
your own repo, then move the `post-merge` hook into the `.git/hooks`
folder, and set up a GitHub webhook to trigger the endpoint whenever a
change is made.

To run it locally, just clone the repo, install the requirements, and
run flask:

```
git clone https://github.com/peterprescott/backend
cd backend
conda create -n backend
pip install -r requirements.txt
flask run
```
