import random

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

from myapp.models import Profile


User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        profiles_count = options.get("count", 10)

        faker = Faker()

        users = []
        for i in range(profiles_count):
            user = User(
                username=faker.user_name(),
                email=faker.email(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
            )
            user.set_password("pass123")
            user.save()
            users.append(user)

        statuses = [s[0] for s in Profile.RELATIONSHIP_STATUS]
        looking_fors = [lf[0] for lf in Profile.LOOKING_FOR]
        educations = [e[0] for e in Profile.EDUCATION]

        for user in users:
            profile = user.profile
            profile.bio = "\n".join(faker.paragraphs(5))
            profile.gender = random.choice([Profile.MALE, Profile.FEMALE])
            profile.relationship_status = random.choice(statuses)
            profile.looking_for = random.choice(looking_fors)
            profile.education = random.choice(educations)
            profile.birth_date = faker.date_between("-50y", "-18y")
            profile.save()
