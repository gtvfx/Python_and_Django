import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


## FAKE POP SCRIPT

import random
from first_app.models import Webpage, AccessRecord, Topic
from faker import Faker

fakegen = Faker()

topics = [
    'Search',
    'Social',
    'MarketPlace',
    'News',
    'Games',
]

def add_topic():
    
    # This creates a tuple object.
    # first item is the model instance that this gets or creates
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create fake data for this entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]



if __name__ == "__main__":
    print('Populating script!')
    populate(20)
    print('Population complete!')