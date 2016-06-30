from __future__ import unicode_literals

from django.db import models
from ..login_reg_app.models import User

class GoalManager(models.Manager):
    def insert_goal(self, title, description, due_date, priority, category_name, user_id, animal_name):
        category = Category.objects.get(category=category_name)
        user = User.userManager.get(id=user_id)
        self.create(title=title, description=description, due_date=due_date, category_id=category, user_id=user)
        this_goal = self.get(title=title, user_id=user, description=description)
        animal = Animal.objects.get(name=animal_name)
        GoalAnimal.objects.create(goal_id=this_goal, animal_id=animal, current_image=animal.image)

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Animal(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category)
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=50)

    category_id = models.ForeignKey(Category)
    user_id = models.ForeignKey(User)

    goalManager = GoalManager()
    objects = models.Manager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GoalAnimal(models.Model):
    goal_id = models.ForeignKey(Goal)
    animal_id = models.ForeignKey(Animal)
    current_image = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Milestone(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField()
    reoccuring = models.BooleanField()
    goal_id = models.ForeignKey(Goal)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
