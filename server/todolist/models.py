from django.db import models
import uuid

# Create your models here.

class Todo(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title