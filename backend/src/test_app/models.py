from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TestApi(TimeStamp):
    name = models.CharField(max_length=255,unique=True, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    is_alive = models.BooleanField(null=True, blank=True)
    phone_no = models.PositiveIntegerField(null=True,blank=True)
    extra_name = models.CharField(max_length=255,default="null",editable=False)
    amount = models.FloatField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Test Api Table"
    
    def save(self,*args,**kwargs):
        self.extra_name = f"{self.name} - {self.phone_no}"
        super().save(*args,**kwargs)

class ModelX(TimeStamp):
    test_content = models.ForeignKey("TestApi", on_delete=models.SET_NULL, null=True,related_name="test_x")
    milage = models.FloatField(null=True,blank=True)
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "ModelX"
    
    def __str__(self):
        return f"{self.test_content.name} {self.milage}"
    
class ModelY(TimeStamp):
    test_content = models.OneToOneField("TestApi", on_delete=models.SET_NULL, null=True,related_name="test_y")
    milage = models.FloatField(null=True,blank=True)
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "ModelY"
    
    def __str__(self):
        return f"{self.test_content.name} {self.milage}"