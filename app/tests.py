from django.test import TestCase
from django.test import Client
from django.urls import reverse
import unittest

from app.models import Chore, ChoreDone, ChoreType, User
from app.views import chore_listview, chore_type_listview, diary_listview, user_listview, category_chart, get_entries

client = Client()

#Tests for accessing pages
class UserAuthorityTests(TestCase):
    #Chores
    def test_chore_listview(self):
        response = client.get(reverse(chore_listview))
        self.assertEqual(response.status_code, 200)
        accessBlocked = False
        content = str(response.content)
        if (content.find("login") > 0):
            accessBlocked = True
        self.assertEqual(accessBlocked, True)

    #Categories(types)
    def test_chore_type_listview(self):
        response = client.get(reverse(chore_type_listview))
        self.assertEqual(response.status_code, 200)
        accessBlocked = False
        content = str(response.content)
        if (content.find("login") > 0):
            accessBlocked = True
        self.assertEqual(accessBlocked, True)

    #Chore Diary
    def test_diary_listview(self):
        response = client.get(reverse(diary_listview))
        self.assertEqual(response.status_code, 200)
        accessBlocked = False
        content = str(response.content)
        if (content.find("login") > 0):
            accessBlocked = True
        self.assertEqual(accessBlocked, True)

    #Users
    def test_user_listview(self):
        response = client.get(reverse(user_listview))
        self.assertEqual(response.status_code, 200)
        accessBlocked = False
        content = str(response.content)
        if (content.find("login") > 0):
            accessBlocked = True
        self.assertEqual(accessBlocked, True)

    #Statistics
    def test_statisticsview(self):
        response = client.get(reverse(get_entries))
        self.assertEqual(response.status_code, 200)
        accessBlocked = False
        content = str(response.content)
        if (content.find("login") > 0):
            accessBlocked = True
        self.assertEqual(accessBlocked, True)

#Chore and ChoreType Model test
class ChoreAndTypeModelTests(TestCase):
    def setUp(self):
        newType = ChoreType.objects.create(name = "Food preparation", description = "Cooking, grilling, baking, etc")
        Chore.objects.create(name = "Baking cake", type = newType)
        
    def test_added_type_and_chore_exists(self):
        chore = Chore.objects.get(name = "Baking cake")
        self.assertEqual(chore.type.name, "Food preparation")

#Diary and User Model test
class DiaryAndUserModelTests(TestCase):
    def setUp(self):
        newUser = User.objects.create(username = "Teppo", password = "testaaja")
        newType = ChoreType.objects.create(name = "Parenting", description = "Taking care of a child")
        newChore = Chore.objects.create(name = "Putting to sleep", type = newType)
        ChoreDone.objects.create(chore = newChore, person = newUser, duration = 90)
    
    def test_added_diary_entry(self):
        diary = ChoreDone.objects.get(duration = 90)
        self.assertEqual(diary.chore.name, "Putting to sleep")
        self.assertEqual(diary.person.username, "Teppo")
    
    @unittest.expectedFailure
    def test_type_should_fail(self):
        diary = ChoreDone.objects.get(duration = 90)
        self.assertEqual(diary.chore.type.name, "Cooking")

#Testing values, that go to Category Chart
class CategoryChartTest(TestCase):
    def setUp(self):
        newUser = User.objects.create(username = "Teppo", password = "testaaja")
        newType1 = ChoreType.objects.create(name = "Parenting", description = "Taking care of a child")
        newType2 = ChoreType.objects.create(name = "Cooking", description = "Preparing meals")
        newType3 = ChoreType.objects.create(name = "Cleaning", description = "Fighting with dirt")
        newType4 = ChoreType.objects.create(name = "Gardening", description = "Taking care of plants and yard space")
        newChore1 = Chore.objects.create(name = "Putting to sleep", type = newType1)
        newChore2 = Chore.objects.create(name = "Making a dinner", type = newType2)
        newChore3 = Chore.objects.create(name = "Mopping the floors", type = newType3)
        newChore4 = Chore.objects.create(name = "Watering the plants", type = newType4)
        ChoreDone.objects.create(chore = newChore1, person = newUser, duration = 90)
        ChoreDone.objects.create(chore = newChore2, person = newUser, duration = 120)
        ChoreDone.objects.create(chore = newChore3, person = newUser, duration = 30)
        ChoreDone.objects.create(chore = newChore4, person = newUser, duration = 15)
        ChoreDone.objects.create(chore = newChore1, person = newUser, duration = 60)
        ChoreDone.objects.create(chore = newChore2, person = newUser, duration = 90)
        ChoreDone.objects.create(chore = newChore3, person = newUser, duration = 40)

    #labels is supposed to have Categories(types) listed
    #data is supposed to have durations for each individual category added and divided by 60 to give amount in hours
    #then fe. Parenting => (90 + 60)/60 => 2
    def test_category_chart_data(self):
        response = client.get(reverse(category_chart))
        content = str(response.content)
        expected = "b'{\"labels\": [\"Parenting\", \"Cooking\", \"Cleaning\", \"Gardening\"], \"data\": [2, 3, 1, 0]}'"
        self.assertEqual(content, expected)