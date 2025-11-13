from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        self.assertEqual(team.name, 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', universe='DC')
        user = User.objects.create(name='Batman', email='batman@dc.com', team=team)
        self.assertEqual(user.name, 'Batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-11-13')
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        workout = Workout.objects.create(name='Super Strength', description='Strength workout')
        workout.suggested_for.add(team)
        self.assertEqual(workout.name, 'Super Strength')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='DC', universe='DC')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
