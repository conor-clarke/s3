from auth import auth

def upload_file(local_filename, s3_object_key):
    s3_resource, s3_bucket = auth('config.ini')
    try:
        bucket = s3_resource.Bucket(s3_bucket)
        bucket.upload_file(local_filename, s3_object_key)
        return True
    except Exception as e:
        print(f'Error uploading file to S3: {str(e)}')
        return False
