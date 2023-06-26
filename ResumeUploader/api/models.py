from django.db import models

# Create your models here.
STATE_CHOICE = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))


class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Image', blank=True)
    docs = models.FileField(upload_to='Document', blank=True)

    def __str__(self) -> str:
        return self.name
