from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    tags = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now_add=True)
    notebook = models.ForeignKey(
        Notebook, 
        on_delete=models.CASCADE, 
        verbose_name="The notebook containing the note")
    