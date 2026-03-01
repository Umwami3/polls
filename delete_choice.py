#!/usr/bin/env python
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'umwami.settings')
django.setup()

from polls.models import Choice


def delete_one_choice_by_text(text):
    qs = Choice.objects.filter(choice_text__iexact=text)
    obj = qs.first()
    if not obj:
        print(f'No Choice found for "{text}"')
        return False
    print(f'Found Choice pk={obj.pk} text="{obj.choice_text}" — deleting...')
    obj.delete()
    print('Deleted.')
    return True


if __name__ == '__main__':
    text = 'Goood!'
    if len(sys.argv) > 1:
        text = sys.argv[1]
    delete_one_choice_by_text(text)
