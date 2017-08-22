#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

celery -A 10token.taskapp worker -l INFO
