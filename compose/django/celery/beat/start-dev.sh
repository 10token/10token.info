#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

rm -f './celerybeat.pid'
celery -A 10token.taskapp beat -l INFO
