#!/usr/bin/env python
import sys
from django.conf import settings


if __name__ == "__main__":
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=['gentelella'],
        ROOT_URLCONF='gentelella.urls',
        SECRET_KEY='SECRET',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            }
        ]
    )

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
