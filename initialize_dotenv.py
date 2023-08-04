#!/usr/bin/env python
# This will create your initial .env files
# These are not to be checked in to git, as you may populate them
# with confidential information

# Standard Library
import os
import random
import string


def random_string(n):
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(n)
    )


PGUSER = random_string(30)
PGPASSWORD = random_string(60)

SECRET_KEY = 'django-insecure-eyiudt)c4efbabjqea@k^+od%p0a@rmw+v6%ys9+dn0tq%z_ga'
DEBUG = True
ALLOWED_HOSTS = ''
LETSENCRYPT_EMAIL='chris.hartley@anymouse.org'
LETSENCRYPT_HOST='www.commonplace.tools'
POSTGRES_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
AWS_S3_ACCESS_KEY_ID = 'AKIA3TSVFRSM2C7PHIDG'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'media.commonplace.tools'
AWS_S3_REGION_NAME = 'us-east-2'

with open('.env', "w") as file:
    