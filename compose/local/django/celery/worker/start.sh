#!/bin/bash

set -o errexit
set -o nounset

watchfiles --filter python 'celery -A rentify_core worker --loglevel=info'