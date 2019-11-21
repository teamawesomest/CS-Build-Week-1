# from django.contrib.auth.models import User
# from adventure.models import Player, Room


# Room.objects.all().delete()

r_testy = {"title":"BOiiii", "description":"if you don't..."}

def copy_room(obj, x):
  for i in range(0, x):
    return obj

print(copy_room(r_testy, 4))  


# players=Player.objects.all()
# for p in players:
#   p.currentRoom=r_outside.id
#   p.save()