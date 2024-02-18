"""
Django Command to wait for the DB to be available
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Command to wait for db"""

    def handle(self, *args, **options):
        pass
