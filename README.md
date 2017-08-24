# s3ninja

Simple Cli tool to compress and upload files to s3, with mutipart upload support.

## Installation :

Use pip to install s3ninja

```
pip install s3ninja
```

#### Alternate installation

You can also compile from source, just clone the repo and run the command below:

```
python setup.py install
```

## Getting Started :


To get started, start with --help
```
$ s3ninja --help
Usage: s3ninja [OPTIONS]

Options:
  -f, --filepath TEXT     path to file
  -c, --compress TEXT     compress file
  -a, --access_key TEXT   aws access_key
  -s, --secret_key TEXT   aws secret_key
  -b, --bucket_name TEXT  s3 bucket name
  --help                  Show this message and exit.
```

Check the example usage to get started

## Example Usage :

```
$ s3ninja -a xxxxxxxxxxxxxx -s xxxxxxxxxxxxxxxxxxxxx -f ~/curl-format.txt -b wynk-logs --compress True
/Users/a10k0arm/curl-format.txt.bz2 successfully created.
uploading part 1 of 1
upload_file done
removing compressed file /Users/padmakar/curl-format.txt.bz2
```

## Contributing
if your code doesn't follow the contribution guidelines it won't be merged

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. stage your feature: `git add <changed_file>`
4. Commit your changes: `git commit -m 'feat: add new feature' -m 'add my-new-feature, use it as: my-new-feautre(args)' -m 'closes #26'`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request :D
