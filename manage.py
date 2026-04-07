#!/usr/bin/env python
# запускает наши приложения и позволяет нам взаимодействовать с ним через командную строку.
# делает миграции, запускает сервер, создает суперпользователя и т.д.
# не нужно изменять, пока недостаточно опыта, чтобы понять, что именно он делает. Просто запомните, что он запускает наше приложение и позволяет нам взаимодействовать с ним через командную строку.
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
