import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')

import django
django.setup()


## FAKE POP SCRIPT

from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        # create fake data for this entry
        nameList = (fakegen.name()).split()
        fake_first_name = nameList[0]
        fake_last_name = nameList[1]

        fake_email = fakegen.email()

        # create the new User entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        # user.save()


if __name__ == "__main__":
    print('Populating script!')
    populate(20)
    print('Population complete!')