from django.core.management.base import BaseCommand
from core.models import User
from core.choices import UserStatus, UserGender
from faker import Faker


class Command(BaseCommand):
    help = "Create 100,000 users with unique emails and phone numbers"

    def handle(self, *args, **kwargs):
        fake = Faker()
        batch_size = 10000
        total_users = 100000
        users = []

        for i in range(total_users):
            phone = f"+88017{i:08d}"

            email = fake.unique.email()
            user = User(
                username=phone,
                phone=phone,
                email=email,
                slug=fake.unique.slug(),
                nid=fake.unique.ssn(),
                status=UserStatus.ABSENT,
                gender=UserGender.UNKNOWN,
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90),
            )
            users.append(user)

            if len(users) >= batch_size:
                User.objects.bulk_create(users)
                users = []

        if users:
            User.objects.bulk_create(users)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {total_users} users")
        )
