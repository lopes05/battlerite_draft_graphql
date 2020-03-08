from django.db import models

# Create your models here.
class Champion(models.Model):
    name = models.CharField(max_length=40, unique=True)
    picture = models.ImageField()
    role = models.CharField(max_length=12)

class Map(models.Model):
    name = models.CharField(max_length=40, unique=True)
    picture = models.ImageField()


class Team(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)


class Captain(models.Model):
    name = models.CharField(max_length=100)

class DraftLobby(models.Model):
    captain_a = models.ForeignKey(Captain, on_delete=models.CASCADE, related_name='captain_a')
    captain_b = models.ForeignKey(Captain, on_delete=models.CASCADE, related_name='captain_b')
    
    team_a = models.ForeignKey(Team, related_name='team_a', on_delete=models.CASCADE)
    team_b = models.ForeignKey(Team, related_name='team_b', on_delete=models.CASCADE)
    
    chosen_map = models.ForeignKey(Map, related_name='map', on_delete=models.SET_NULL, null=True)

    team_a_bans = models.ForeignKey(Champion, related_name='bans_a', on_delete=models.SET_NULL, null=True)
    team_b_bans = models.ForeignKey(Champion, related_name='bans_b', on_delete=models.SET_NULL, null=True)