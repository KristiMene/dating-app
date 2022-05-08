from datetime import datetime

from django.db import models
from django.conf import settings


class Profile(models.Model):
    MALE = "MALE"
    FEMALE = "FEMALE"
    BOTH = "BOTH"

    GENDER = ((MALE, "Male"), (FEMALE, "Female"))

    RELATIONSHIP_STATUS = (
        ("NEVER MARRIED", "Never Married"),
        ("DIVORCED", "Divorced"),
        ("WIDOWED", "Widowed"),
        ("SEPARATED", "Separated"),
    )

    LOOKING_FOR = ((MALE, "Men"), (FEMALE, "Women"), (BOTH, "Both"))

    EDUCATION = (
        ("HIGH SCHOOL", "High School"),
        ("COLLEGE", "College"),
        ("BACHELORS DEGREE", "Bachelors Degree"),
        ("MASTERS", "Masters"),
        ("PHD / POST DOCTORAL", "PhD / Post Doctoral"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, default="", blank=False)
    gender = models.CharField(choices=GENDER, null=True, blank=True, max_length=15)
    relationship_status = models.CharField(
        choices=RELATIONSHIP_STATUS, default="", max_length=20
    )
    looking_for = models.CharField(choices=LOOKING_FOR, default="", max_length=20)
    education = models.CharField(choices=EDUCATION, default="", max_length=200)
    birth_date = models.DateField(null=True, default="2000-01-01", blank=True)

    @property
    def age(self):
        return int((datetime.time.today() - self.birth_date).days / 365.25)

    def __str__(self):
        return self.user.username
