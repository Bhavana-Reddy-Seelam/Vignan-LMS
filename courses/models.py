from django.db import models
from users.models import User


class Course(models.Model):
    CATEGORY_CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Python'
    )
    course_image = models.ImageField(
        upload_to='course_images/',
        blank=True,
        null=True
    )

    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'instructor'}
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Progress(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    completed_lessons = models.IntegerField(default=0)
    total_lessons = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"


class Analytics(models.Model):
    total_students = models.IntegerField(default=0)
    total_courses = models.IntegerField(default=0)
    total_instructors = models.IntegerField(default=0)
    total_enrollments = models.IntegerField(default=0)

    def __str__(self):
        return "Analytics Dashboard"