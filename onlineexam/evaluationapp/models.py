from django.db import models

# Create your models here.
# class Assign_Evaluation(models.Model):
#     Name=models.CharField(max_length=50)


# class Create_Evaluation(models.Model):
#     Name=models.CharField(max_length=50)
class Trainer(models.Model):
      trainer=models.CharField(max_length=50)

      def __str__(self):
           return self.trainer
      



class question_Bank(models.Model):
    # Name=models.CharField(max_length=50)
    Trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    Course=models.CharField(max_length=50,
                            choices=[('python','python'),('oops','oops')])
    Level= models.CharField(max_length=20, 
                                 choices=[('exam1', 'exam1'), ('exam2', 'exam2'),('exam3','exam3'),('exam4','exam4'),('exam5','exam5'),('exam6','exam6'),('exam7','exam7'),('exam8','exam8'),('exam9','exam9'),('exam10','exam10'),('exam11','exam11'),('exam12','exam12'),('exam13','exam13'),('exam14','exam14'),('exam15','exam15')])
    

    # def _str_(self):
    #     return self.Trainer
    

    

# class Question_Topic(models.Model):
#     Name=models.CharField(max_length=50)