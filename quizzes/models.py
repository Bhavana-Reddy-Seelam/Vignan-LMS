from django.db import models
from users.models import User
from courses.models import Course


class Quiz(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )

    question_text = models.CharField(max_length=500)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_answer = models.CharField(max_length=200)

    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text


class Result(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )

    score = models.IntegerField(default=0)

    total_marks = models.IntegerField(default=0)

    status = models.CharField(
        max_length=10,
        default='Fail'
    )

    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}"