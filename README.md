# Get releases by semver

This action retrieves a list of release-versions from the requested repository. Only valid semver versions will be included. Depending on the requested version depth, only the latest version will be included. E.g. if "MINOR" is configured, for versions ```['0.1.0','0.2.0','0.2.1']``` only ```['0.1.0','0.2.1']``` will be included.  

## Inputs

### `repository`

**Required** The repository to retrieve releases for.

### `include`

**Required** Lowest field to be included. Possible values: ["MAJOR","MINOR","PATCH","ALL"]

### `versionField`

Field to be used for extracting the version. Possible values: ["TITLE", "TAG-NAME"] Default: ```TITLE```

### `minMajor`

The minimum major version to be included. Default: ```0```

### `minMinor`

The minimum minor version to be included. Default: ```0```

### `minPatch`

The minimum patch version to be included. Default: ```0```

### `excludePre`

Should pre-release versions be excluded. Default: ```true```

### `excludeMajor`

Should some major versions be excluded. Example ```5,9```

### `token`

Access token to be used when requesting the github-api. Its recommended to use, since the ratelimit for unauthenticated requests is 60/h while authenticated is 1000/h.



## Example usage

```yaml
uses: wistefan/get-releases-by-semver@master
with:
    include: "MINOR"
    repository: wistefan/get-releases-by-semver
    minMinor: "2"
```
