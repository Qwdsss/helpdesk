from django.db import models
from django.contrib.auth.models import User

PRIORITY_CHOICES = (
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
)

STATUS_CHOICES = (
    ('new', 'new'),
    ('in_progress', 'in progress'),
    ('confirmed', 'Confirmed'),
    ('resolved', 'resolved'),
)


class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    actions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new')
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_problems')
    resolved_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_problems')
