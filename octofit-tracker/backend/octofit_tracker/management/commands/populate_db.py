from django.core.management.base import BaseCommand
from octofit_tracker.test_data import get_test_data
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

print('populate_db module loaded')

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.DATABASES['default']['localhost'], settings.DATABASES['default']['27017'])
        db = client[settings.DATABASES['default']['octofit_db']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        
        test_data = get_test_data()

        # Insert test data into collections
        # Create users
        db.users.insert_many(test_data['users'])
        # Create teams
        db.teams.insert_many(test_data['teams'])
        # Create activities
        db.activities.insert_many(test_data['activities'])
        # Create leaderboards
        db.leaderboard.insert_many(test_data['leaderboard'])
        # Create workouts
        db.workouts.insert_many(test_data['workouts'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
