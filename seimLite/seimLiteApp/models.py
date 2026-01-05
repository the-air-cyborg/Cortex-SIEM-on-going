from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Log(models.Model):
    LEVEL_CHOICES = [
        ("INFO", "Info"),
        ("WARNING","Warning"),
        ("CRITICAL","Critical"),
    ]
    
    STATUS_CHOICES=[
        ("OK","Ok"),
        ("INVESTIGATE","Investigate"),
        ("BLOCKED","Blocked")
    ]
    
    timestamp=models.DateTimeField(auto_now_add=True)
    level=models.CharField(max_length=10,choices=LEVEL_CHOICES)
    source=models.CharField(max_length=50)
    message=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES)
    
    def __str__(self):
        return f"{self.level} | {self.source}"
    