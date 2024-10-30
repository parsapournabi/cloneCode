import requests
from git import Repo
from urllib.request import getproxies
import os

# URL to check for the latest version
version_url = 'https://api.github.com/repos/parsapournabi/runByClone/releases/latest'
# Path to clone the repository
repo_path = 'src/clone'
# URL to your GitHub repository
repo_url = 'https://github.com/parsapournabi/runByClone.git'


class Main:
    @staticmethod
    def check_for_update():
        response = requests.get(version_url, proxies={'http': getproxies().get('http'), 'https': getproxies().get('http')})
        latest_version = response.json()['tag_name']
        return latest_version

    @staticmethod
    def clone_or_pull():
        if os.path.exists(repo_path):
            repo = Repo(os.path.join(repo_path))
            origin = repo.remotes.origin
            origin.pull()
            print("Repository updated")
        else:
            Repo.clone_from(repo_url, repo_path)
            print("Repository cloned")


