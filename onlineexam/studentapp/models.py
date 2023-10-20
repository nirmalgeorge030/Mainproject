from django.db import models
from django.contrib.auth.models import User

Level_CHOICES = [
    ('exam1', 'exam1'),
    ('exam2', 'exam2'),
    ('exam3', 'exam3'),
    ('exam4', 'exam4'),
    ('exam5', 'exam5'),
    ('exam6', 'exam6'),
    ('exam7', 'exam7'),
    ('exam8', 'exam8'),
    ('exam9', 'exam9'),
    ('exam10', 'exam10'),
    ('exam11', 'exam11'),
    ('exam12', 'exam12'),
    ('exam13', 'exam13'),
    ('exam14', 'exam14'),
    ('exam15', 'exam15'),
]
class exam(models.Model):
    student_id=models.CharField(max_length=50)
    Course = models.CharField(max_length=50, choices=[('python', 'python'), ('oops', 'oops')])
    Level = models.CharField(max_length=20, choices=Level_CHOICES)
    

class student(models.Model):
    Fullname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    student_id=models.CharField(max_length=50)
    Course = models.CharField(max_length=50, choices=[('python', 'python'), ('oops', 'oops')])
    
    def __str__(self):
        return self.Fullname

    def save(self, *args, **kwargs):
        # Check if a user with the same Fullname already exists
        user_exists = User.objects.filter(username=self.Fullname).exists()

        # If not, create a new user with Fullname as the username and Phone as the password
        if not user_exists:
            user = User.objects.create_user(username=self.Fullname, password=self.student_id)
            user.save()

        super(student, self).save(*args, **kwargs)





class result(models.Model):
    Result=models.FileField(upload_to='upload_pdfs/',blank=True,null=True)
    Fullname=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Fullname