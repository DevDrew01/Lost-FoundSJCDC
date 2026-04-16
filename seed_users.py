import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
django.setup()

from django.contrib.auth.models import User


def create_dummy_users():
    # The exact list of ID numbers
    dummy_ids = [
        ('10-2526-301491', 'Student 1'),
        ('10-2526-301492', 'Student 2'),
        ('10-2526-301493', 'Student 3'),
        ('10-2526-301494', 'Student 4'),
        ('10-2526-301495', 'Student 5'),
    ]

    password = 'password123'

    for s_id, s_name in dummy_ids:
        if not User.objects.filter(username=s_id).exists():
            # Using create_user ensures the password is encrypted/hashed
            User.objects.create_user(
                username=s_id,
                password=password,
                first_name=s_name,
                email=f"{s_id}.SJCDC@phinma.ph"
            )
            print(f"Successfully created: {s_id}")
        else:
            print(f"User {s_id} already exists.")


if __name__ == '__main__':
    create_dummy_users()