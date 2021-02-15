from .models import Client


def create_client(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        avatar = f'https://graph.facebook.com/{response["id"]}/picture?type=large'

    if not Client.objects.filter(user_id=user.id):
        Client.objects.create(user_id=user.id, avatar=avatar)
