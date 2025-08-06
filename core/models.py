# tasks/models.py
from django.conf import settings
from django.db import models

class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(ModelBase):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tasks',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_by', 'completed']),
            models.Index(fields=['due_date']),
        ]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return f"{self.title} - {'✓' if self.completed else '•'}"
