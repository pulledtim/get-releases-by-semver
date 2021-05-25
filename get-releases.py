from github import Github

import semver

import os
import sys

supportedIncludes = ["MAJOR","MINOR", "PATCH", "ALL"]

repo = os.environ['REPOSITORY']
include = os.environ['INCLUDE']
minMajor = os.environ['MIN_MAJOR']
minMinor = os.environ['MIN_MINOR']
minPatch = os.environ['MIN_PATCH']

if include not in supportedIncludes:
    print(include + " is not a supported field.")

github = Github()
repository = github.get_repo(repo)

matching_releases = []

for release in repository.get_releases():
    print(release.title)
    version = semver.VersionInfo.parse(release.tag)
    print(version)