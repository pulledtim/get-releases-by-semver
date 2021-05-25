from github import Github

import semver

import os
import sys

supportedIncludes = ["MAJOR","MINOR", "PATCH", "ALL"]

repo = os.environ['REPOSITORY']
include = os.environ['INCLUDE']
excludePrereleases = os.environ['EXCLUDE_PRE']
minMajor = os.environ['MIN_MAJOR']
minMinor = os.environ['MIN_MINOR']
minPatch = os.environ['MIN_PATCH']

if include not in supportedIncludes:
    print(include + " is not a supported field.")

github = Github()
repository = github.get_repo(repo)

matching_releases = []

majorDict = {}
minorDict = {}
patchDict = {}
allReleases = []

for release in repository.get_releases():
    version = semver.VersionInfo.parse(release.title)
    if excludePrereleases and version.prerelease is not None:
        continue

    if include == "MAJOR":
        if version.major in majorDict:
            if majorDict[version.major].compare(version) > -1:
                majorDict[version.major] = version
        else:
            majorDict[version.major] = version
        continue
    elif include == "MINOR":
        versionKey = "{}-{}".format(version.major, version.minor)
        if versionKey in minorDict:
            if minorDict[versionKey].compare(version) > -1:
                minorDict[versionKey] = version
        else:
            minorDict[versionKey] = version
        continue
    elif include == "PATCH":
        versionKey = "{}-{}-{}".format(version.major, version.minor, version.patch)
        if versionKey in patchDict:
            if patchDict[versionKey].compare(version) > -1:
                patchDict[versionKey] = version
        else:
            patchDict[versionKey] = version
        continue
    else: 
        allReleases.append(release.title)

releases = []
if include == "MAJOR":
    releases = list(majorDict.values())
elif include == "MINOR":
    releases = list(minorDict.values())
elif include == "PATCH":
    releases = list(patchDict.values())
else: 
    releases = allReleases

print(f"::set-output name=releases::{releases}")