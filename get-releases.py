from github import Github

import os
import re

repo = os.environ['REPOSITORY']
pattern = os.environ['VERSION_PATTERN']

github = Github()
repository = github.get_repo(repo)
matching_releases = []
for release in repository.get_releases():
    if re.match(pattern, release.tag_name):
        matching_releases.append(release)

for v in matching_releases:
    print(v)