from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trainer(models.Model):
      trainer=models.CharField(max_length=50)
      trainer_id=models.CharField(max_length=50)
      # phone=models.CharField(max_length=50)

      def __str__(self):
           return self.trainer
      
      def save(self, *args, **kwargs):
        # Check if a user with the same Fullname already exists
        user_exists = User.objects.filter(username=self.trainer).exists()

        # If not, create a new user with Fullname as the username and Phone as the password
        if not user_exists:
            user = User.objects.create_user(username=self.trainer, password=self.trainer_id)
            user.save()

        super(Trainer, self).save(*args, **kwargs)

class District(models.Model):
      district=models.CharField(max_length=50)

      def __str__(self):
           return self.district


class State(models.Model):
      state=models.CharField(max_length=50)

      def __str__(self):
           return self.state

class Branch(models.Model):
    branch=models.CharField(max_length=50)
    Branchcode=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    Pincode=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)




    def __str__(self):
           return self.branch




# class Batch(models.Model):
#       batch=models.CharField(max_length=50)
#       def _str_(self):
#            return self.batch
      
class Course(models.Model):
      course=models.CharField(max_length=50)
      def __str__(self) :
            return self.course
      
class Batch(models.Model):      
      batch=models.CharField(max_length=50)
      Trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
      Course=models.ForeignKey(Course,on_delete=models.CASCADE)
      # States=models.ForeignKey(States,on_delete=models.CASCADE)
      Branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
      Startdate=models.DateField()
      Enddate=models.DateField()
      def __str__(self):
           return self.batch

class Company(models.Model):
      Company=models.CharField(max_length=50)
      Address1=models.CharField(max_length=50)
      Address2=models.CharField(max_length=50)
      Address3=models.CharField(max_length=50)
      Phone=models.CharField(max_length=50)
      Email=models.CharField(max_length=50)
      Website=models.CharField(max_length=50)
      Logo=models.FileField(upload_to='upload_pdfs/',blank=True,null=True)



      def __str__(self) :
        return self.Company


# class Master_Data(models.Model):
#      Name=models.CharField(max_length=50)
#      Value=models.CharField(max_length=50)
#      Type=models.CharField(max_length=50)




#      def _str_(self) :
#         return self.Master_Data