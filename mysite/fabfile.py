from fabric.api import local
from fabric.api import lcd

def prepare_deployment(branch_name):
    local('python manage.py test requests')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

def deploy():
    with lcd('https://github.com/unbenchme/some-words-go-here/tree/requests_model'):
        local('git pull C:\SourceProjects\dev\some-words-go-here')
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
