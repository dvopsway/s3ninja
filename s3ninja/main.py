import click
import os
import sys
import math
import boto
import bz2
from os import path

compressionLevel = 9


class NinjaError(Exception):
    """Exception for sshmux specific errors"""
    pass


def validate_file(file_path):
    if path.exists(file_path):
        return file_path
    else:
        raise NinjaError('{0} file doesn\'t exist'.format(file_path))


def upload_file(s3, bucketname, file_path):
    b = s3.get_bucket(bucketname)
    filename = os.path.basename(file_path)
    k = b.new_key(filename)
    mp = b.initiate_multipart_upload(filename)
    source_size = os.stat(file_path).st_size
    bytes_per_chunk = 5000 * 1024 * 1024
    chunks_count = int(math.ceil(source_size / float(bytes_per_chunk)))
    for i in range(chunks_count):
        offset = i * bytes_per_chunk
        remaining_bytes = source_size - offset
        bytes = min([bytes_per_chunk, remaining_bytes])
        part_num = i + 1
        print "uploading part " + str(part_num) + " of " + str(chunks_count)
        with open(file_path, 'r') as fp:
            fp.seek(offset)
            mp.upload_part_from_file(fp=fp, part_num=part_num, size=bytes)
    if len(mp.get_all_parts()) == chunks_count:
        mp.complete_upload()
        print "upload_file done"
    else:
        mp.cancel_upload()
        print "upload_file failed"


def compress_file(filepath):
    destination_file = "%s.bz2" % filepath
    tarbz2contents = bz2.compress(
        open(filepath, 'rb').read(), compressionLevel)
    fh = open(destination_file, "wb")
    fh.write(tarbz2contents)
    fh.close()
    print "%s successfully created." % destination_file
    return destination_file


@click.command()
@click.option('--filepath', '-f', help='path to file')
@click.option('--compress', '-c', default=False, help='compress file')
@click.option('--access_key', '-a', help='aws access_key')
@click.option('--secret_key', '-s', help='aws secret_key')
@click.option('--bucket_name', '-b', help='s3 bucket name')
def main(filepath, compress, access_key, secret_key, bucket_name):
    if compress:
        file_path = compress_file(validate_file(filepath))
    else:
        file_path = validate_file(filepath)
    s3 = boto.connect_s3(access_key, secret_key)
    try:
        upload_file(s3, bucket_name, file_path)
    except:
        print "Upload failed, trying again"
        try:
            upload_file(s3, bucket_name, file_path)
        except:
            try:
                print "Upload failed, last try"
                upload_file(s3, bucket_name, file_path)
            except:
                print "Upload failed again, Exiting"

    if compress:
        print "removing compressed file %s" % file_path
        os.remove(file_path)
