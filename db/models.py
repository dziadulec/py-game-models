from django.db import models

class Race(models.Model):
        RACE_CHOICES = [
        ("elf", "Elf"),
        ("dwarf", "Dwarf"),
        ("human", "Human"),
        ("ork", "Ork"),
    ]
        
        name = models.CharField(max_length=255, choices=RACE_CHOICES, unique=True)
        description = models.TextField(blank=True)


class Skill(models.Model):
        name = models.CharField(max_length=255,unique=True)
        bonus  = models.CharField(max_length=255,unique=True)
        race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
        name = models.CharField(max_length=255,unique=True)
        description = models.TextField(null=True, blank=True)






    

