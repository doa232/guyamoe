from django.core.management.base import BaseCommand

from reader.models import Series
from django.conf import settings

import os


class Command(BaseCommand):
    help = "Search/replace utility for synopsis of series"

    def add_arguments(self, parser):
        parser.add_argument("--search", required=True, help="String you want to search for")
        parser.add_argument("--replace", required=True, help="String you want to replace the search input by")
        parser.add_argument('--test', action="store_true", default=False, help="Don't actually apply the change")

    def handle(self, *args, **options):
        for series in Series.objects.all():
            new_synopsis = str(series.synopsis).replace(options["search"], options["replace"])
            if options["test"] and new_synopsis != str(series.synopsis):
                print(f"Before: {repr(str(series.synopsis))}")
                print(f"After:  {repr(new_synopsis)}")
            elif not options["test"]:
                series.synopsis = new_synopsis
                series.save()