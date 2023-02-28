from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User



# @receiver(post_save, sender=Profile) <-- decorador também é uma forma de utilizar Triggers
from users.models import Profile


def createProfile(sender, instance, created, **kwargs):
    print('Signal Triggers')
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

def deleteUser(sender, instance, **kwargs):
        user = instance.user
        user.delete()
        print('Deleting User...')

post_save.connect(createProfile, sender=Profile)

post_delete.connect(deleteUser, sender=User)