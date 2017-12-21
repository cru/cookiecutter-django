#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py bower_install --allow-root
python manage.py createinitialrevisions
python manage.py collectstatic_js_reverse
python manage.py migrate
python manage.py runserver_plus 0.0.0.0:8000
