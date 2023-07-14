from django.db import models
from django.contrib.auth.models import User

# User Level Model
class Role(models.Model):
    name = models.CharField(max_length=50)
    # action = models.CharField(max_length=100, blank=True, null=True)

    def str(self):
        return self.name 

#Employee Register Model
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MARITAL_STATUS_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    )
    
    EMPLOYMENT_TYPE_CHOICES = (
        ('fulltime_permanent', 'Fulltime Permanent'),
        ('fulltime_probation', 'Fulltime Probation'),
        ('part_time_contract', 'Part Time Contract'),
    )

    # Personal Details
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(blank=True)
    nationality = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    
    #Contact Details
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    # Employment Details
    joined_date = models.DateField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, unique=True)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    role = models.ForeignKey(Role, verbose_name=("User Level"), on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_designation = models.CharField(max_length=100, blank=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    # action = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def str(self):
        return f"{self.employee_id} - {self.first_name}"

# Departments Model
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_head = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='head_of_department')
    total_employees = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # action = models.CharField(max_length=100, blank=True, null=True)

    def str(self):
        return f"{self.department_name} - {self.department_head}"

# Competencies Model
class Competency(models.Model):
    competency_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    designation = models.ForeignKey(Employee, to_field='designation', on_delete=models.CASCADE, null=True, blank=True)
    weight = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    initiated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Competenceis"

    def str(self):
        return self.competency_name
    
# Onboarding Model
class Onboarding(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    onboarding_end_date = models.DateField()
    # action = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def str(self):
        return f"Onboarding for {self.employee.employee_id}"

# Task Model
class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
        # ('overdue_and_other', 'Overdue and Other'),
    )

    PRIORITY_CHOICES = (
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    assigned_to = models.ManyToManyField(Employee)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    approval = models.BooleanField(default=False, choices=[(True, 'Request Accepted'), (False, 'Request Declined')], blank=True, null=True)
    performance_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # action = models.CharField(max_length=100, blank=True, null=True)

    def str(self):
        return f"{self.title} - {self.status}"

# Probation Model
class Probation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_of_permanency = models.DateField()
    # ACTION_CHOICES = (
    #     ('extend', 'Extend Probation'),
    #     ('reduce', 'Reduce Probation'),
    #     ('terminate', 'Terminate Employee'),
    # )
    # action = models.CharField(max_length=100, blank=True, null=True)#, choices=ACTION_CHOICES)
    comment = models.TextField(blank=True, null=True)

    def str(self):
        return f"{self.employee.employee_id} - {self.employee.first_name}"

# Promotion/Recognition Model..myb make it models

# Termination Model
class Termination(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_of_termination = models.DateField()
    reason = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)

    def str(self):
        return f"{self.employee.employee_id} - {self.employee.first_name} - Terminated"

# Courses Model
class Course(models.Model):
    course_id = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    coach = models.ManyToManyField(Employee, blank=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    # action = models.CharField(max_length=100, blank=True, null=True)

    def str(self):
        return self.course_id

# Training Model
class Training(models.Model):
    training_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    trainer = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='trainer')
    initiated_date = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Employee)
    STATUS_CHOICES = (
        ('PA', 'Pending Approval'),
        ('S', 'Scheduled'),
        ('C', 'Completed'),
        ('C', 'Cancelled'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # action = models.CharField(max_length=100, blank=True, null=True)

    def str(self):
        return self.training_course

# Development Model
class DevelopmentPlan(models.Model):
    IDP_name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='IDP_employee')
    goal = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    coach = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='coach')
    initiated_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('NI', 'Not Initiated'),
        ('I', 'Initiated'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)
    # action = models.CharField(max_length=100, blank=True, null=True)

    def str(self):
        return f"IDP for {self.IDP_name} - {self.employee.first_name}"

# Appraisal Model
class Matrix(models.Model):
    POTENTIAL_CHOICES = (
        ('L', 'Low'),
        ('M', 'Moderate'),
        ('H', 'High'),
    )
    category = models.CharField(max_length=2, choices=POTENTIAL_CHOICES)
    note = models.CharField(max_length=100)
    weight = models.IntegerField(choices=POTENTIAL_CHOICES)

    class Meta:
        verbose_name_plural = "Matrices"

    def str(self):
        return self.category

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    weight = models.IntegerField(blank=True, null=True)

class Appraisal(models.Model):
    employee = models.ManyToManyField(Employee)
    appraisal_cycle = models.CharField(max_length=100) #appraisal_name
    competencies = models.ManyToManyField(Competency)
    questions = models.ManyToManyField(Question)
    potential = models.ForeignKey(Matrix, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    evaluators = models.ManyToManyField(Employee, related_name='evaluators')
    colleagues = models.ManyToManyField(Employee, related_name='colleagues')
    others = models.CharField(max_length=100, blank=True, null=True) # students - but it is hard to prepare a form to be filled by a student so manager/admin ymolawal
    start_from = models.DateTimeField(auto_now_add=True)
    to = models.DateTimeField()
    due_date = models.DateTimeField() #for report ከጠቀመ እንጂ no other use
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
        # ('O', 'Overdue'),
    )
    appraisal_Status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    final_rating = models.DecimalField(max_digits=10, decimal_places=2) #potential assessment
    
    def str(self):
        return f"{self.appraisal_cycle} - {self.appraisal_Status}"

# Report Model ....may not be necessary

# Document Model
class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='documents/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Employees who can view this news
    employees = models.ManyToManyField(Employee, related_name='documents', blank=True)

    # Managers who can view this news
    managers = models.ManyToManyField(Employee, related_name='manager_docs', blank=True)

    def str(self):
        return f"{self.title} - {self.author}"

# News Model
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    news_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    # Employees who can view this news
    employees = models.ManyToManyField(Employee, related_name='news', blank=True)

    # Managers who can view this news
    managers = models.ManyToManyField(User, related_name='manager_news', blank=True)

    class Meta:
        verbose_name_plural = "News"

    def str(self):
        return f"{self.title} - {self.publisher}"
