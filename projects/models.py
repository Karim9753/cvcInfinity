from django.db import models

class Project(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
class Reseau(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    type_reseau = models.CharField(max_length=100)

    def __str__(self):
        return self.nom