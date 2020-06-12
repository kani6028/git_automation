from _repo.repo import Repo
from github import Github

user = "kani6028"
password = "Omashkani@5"
g = Github(user,password)
repo = g.get_user().get_repo('git_automation')
PATH_OF_GIT_REPO = r'https://github.com/kani6028/git_automation.git'
COMMIT_MESSAGE = "comment from python script"

file_list = [
    'C:\\New folder\\New folder(1)'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()

    except:
        print("Some error occured while pushing the code")
git_push()
