# Get releases by semver

This action retrieves a list of release-versions from the requested repository. Only valid semver versions will be included. Depending on the requested version depth, only the latest version will be included. E.g. if "MINOR" is configured, for versions ```['0.1.0','0.2.0','0.2.1']``` only ```['0.1.0','0.2.1']``` will be included.  

## Inputs

### `repository`

**Required** The repository to retrieve releases for.

### `include`

**Required** Lowest field to be included. Possible values: ["MAJOR","MINOR","PATCH","ALL"]

### `minMajor`

The minimum major version to be included. Default: ```0```

### `minMinor`

The minimum minor version to be included. Default: ```0```

### `minPatch`

The minimum patch version to be included. Default: ```0```

### `excludePre`

Should pre-release versions be excluded. Default: ```true```


## Example usage

```yaml
uses: wistefan/get-releases-by-pattern@master
with:
    include: "MINOR"
    repository: wistefan/get-releases-by-pattern
    minMinor: "2"
```