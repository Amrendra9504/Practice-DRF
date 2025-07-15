from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)



class Department(models.Model):
    department_name = models.CharField(max_length=50)
    def __str__(self):
        return self.department_name
    

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    def __str__(self):
        return self.name
