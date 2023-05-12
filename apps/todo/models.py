"""
    Todo app Models
"""
import uuid
from django.db import models

class Tasks(models.Model):
    """
        Model Tasks
        id -> uuid
        title -> string
        description -> text
        completed -> boolean
        created_at -> timestamps
        updated_at -> timestamps
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(default=None, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.title}"
    