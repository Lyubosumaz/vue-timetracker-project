import os
import django
import random
from faker import Faker

# FAKE POP SCRIPT
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    return Topic.objects.get_or_create(top_name=random.choice(topics))[0]


def populate(N=5):
    for _ in range(N):
        # create topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == "__main__":
    print('populating script!')
    os.environ.setdefault('DJANGO_SETTINGS_MODULES', 'first_project.settings')
    django.setup()
    from first_app.models import AccessRecord, Topic, Webpage

    populate(20)
    print('popilating successful!')
