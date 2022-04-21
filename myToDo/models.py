from django.db import models
import datetime

# Create your models here.
class ToDoItem(models.Model):
    """Item on To-Do list"""

    list_item = models.CharField(
        max_length=150,
        help_text="Task to add to list."
    )

    complete = models.BooleanField(
        help_text="Task is completed or not.",
        default = False
    )

    tags=models.ManyToManyField(
        'Tags', through='TodoTags'
    )

    def __str__(self) -> str:
        return self.list_item

class Tags(models.Model):
    """Tags defining a ToDoItem"""

    tag = models.CharField(
        max_length=50,
        help_text="Tag for to-do item."
    )

    def __str__(self) -> str:
        return self.tag

class TodoTags(models.Model):
    """ToDoItems Tags"""
    todo = models.ForeignKey(
        ToDoItem,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE
    )

class Note(models.Model):
    """Note on an item"""
    note = models.TextField(
        help_text="Note about task."
    )

    task = models.ForeignKey(
        ToDoItem,
        on_delete=models.CASCADE,
        help_text="The task that this note is for."
        )

    date_created = models.DateTimeField(
        default=datetime.datetime.now,
        help_text='The date and time the note was created.'
    )

    def __str__(self) -> str:
        return self.note
