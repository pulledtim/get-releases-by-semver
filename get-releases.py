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
    if not semver.VersionInfo.isvalid(release.title):
        continue

    version = semver.VersionInfo.parse(release.title)
    if excludePrereleases and version.prerelease is not None:
        continue

    if include == "MAJOR":
        if int(version.major) < int(minMajor): 
            continue
        if version.major in majorDict:
            if majorDict[version.major].compare(version) < 1:
                majorDict[version.major] = version
        else:
            majorDict[version.major] = version
        continue
    elif include == "MINOR":
        if int(version.major) < int(minMajor) or int(version.minor) < int(minMinor): 
            continue
        versionKey = "{}-{}".format(version.major, version.minor)
        if versionKey in minorDict:
            if minorDict[versionKey].compare(version) < 1:
                minorDict[versionKey] = version
        else:
            minorDict[versionKey] = version
        continue
    elif include == "PATCH":
        if int(version.major) < int(minMajor) or int(version.minor) < int(minMinor) or int(version.patch) < int(minPatch): 
            continue
        versionKey = "{}-{}-{}".format(version.major, version.minor, version.patch)
        if versionKey in patchDict:
            if patchDict[versionKey].compare(version) < 1:
                patchDict[versionKey] = version
        else:
            patchDict[versionKey] = version
        continue
    else: 
        allReleases.append(release.title)

releases = []
if include == "MAJOR":
    for r in list(majorDict.values()):
        releases.append(r.__str__())
elif include == "MINOR":
    for r in list(minorDict.values()):
        releases.append(r.__str__())
elif include == "PATCH":
    for r in list(patchDict.values()):
        releases.append(r.__str__())
else: 
    releases = allReleases

print(releases)
print(f"::set-output name=releases::{releases}")