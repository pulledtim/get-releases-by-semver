from github import Github

import os

repo = os.environ['REPOSITORY']
pattern = os.environ['VERSION_PATTERN']

github = Github()
repository = github.get_repo(repo)
for release in repository.get_releases():
    print(release)