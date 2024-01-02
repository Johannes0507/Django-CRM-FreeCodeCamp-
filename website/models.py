from django.db import models
from django.utils import timezone
from .utils.general_id import generate_record_code

class Record(models.Model):
    id = models.CharField(primary_key=True, max_length=50, editable=False)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # 對新增的項目生成編號根據 last_name 跟 現在時間的年月日 還有另外建構的的函式生成字母0-9 A-Z e.g. 旻恩_2024010100000
    def save(self, *args, **kwargs):
        if not self.id:
            current_time = timezone.now()
            code = generate_record_code()
            self.id = f"{self.first_name}_{current_time.strftime('%Y%m%d')}{code}"
        super(Record, self).save(*args, **kwargs)



