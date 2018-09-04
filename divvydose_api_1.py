from flask import Flask
from flask_restplus import Api, Resource, fields,Model,marshal_with,reqparse
import requests

from divvydose_api_models import * 

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
test = parser.add_argument('Bit-Bucket Username',type=str, help = "Can not be blank")
payload = {'username': test }

userInputModel = {
    'BitBucket-User-PublicRepos-count': len(requests.get('https://api.bitbucket.org/2.0/users/mailchimp/repositories', params=payload).json()),
    'BitBucket-User-PublicRepos': requests.get('https://api.bitbucket.org/2.0/users/mailchimp/repositories', params=payload).json(),
    'GitHub-User-PublicRepos': requests.get('https://api.github.com/users', params=payload).json()
}

"""This method/route takes in a username specified by the user. The returned results given user info for both GitHub and BitBucket APIs
"""
@api.route('/user/')
class UserProvided(Resource):
    @api.expect(test)
    def get(self):
        return userInputModel

""" This method/Route returns the total number of forks and public repos for a given username"""
@api.route('/total')
class TotalNumber(Resource):
    def get(self):
        return totalModel

""" This method/Route returns the total number of watchers for a given username"""
@api.route('/watchers')
class WatcherNumber(Resource):
    def get(self):
        return watcherModel

""" This method/Route returns the total number of stars for a given username"""
@api.route('/stars')
class StarCount(Resource):
    def get(self):
        return starsModel

""" This method/Route returns the total number of issues for a given username"""
@api.route('/issues')
class IssuesCount(Resource):
    def get(self):
        return issuesModel

""" This method/Route returns the total number of commits for a given username"""
@api.route('/commits')
class CommitsCount(Resource):
    def get(self):
        return commitsModel


"""This method/Route returns the total number of languages used for a given username"""
@api.route('/languages-used')
class Languages(Resource):
    def get(self):
        return languagesModel



if __name__ == '__main__':
    app.run(debug=True)