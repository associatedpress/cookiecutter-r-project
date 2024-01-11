import re
import sys

SLUG_REGEX = r'^[a-zA-Z0-9][-_a-zA-Z0-9]+$'
slug = '{{ cookiecutter.project_slug }}'

if not re.match(SLUG_REGEX, slug):
    print(f'ERROR: {slug} is not a valid project slug!')
    sys.exit(1)
