from django.db import models


class Member(models.Model):

    # 姓名, 文字屬性, 最大長度 6
    name = models.TextField(max_length=6, help_text='使用者姓名')
    # 年齡, int屬性, Default 是 0 歲
    age = models.IntegerField(default=0)
    # 生日, Datetime屬性, 可為 NULL ( 預設為不可 NULL )
    birth_day = models.DateTimeField(null=True)
    # 照片, 網址屬性, verbose_name 為完整的欄位名稱
    pic_url = models.URLField(null=True, verbose_name='會員的照片網址')
    # Email, 信箱屬性
    email = models.EmailField(null=True)
    # 男女, Bool屬性
    is_female = models.BooleanField()
    # 修改日, 時間屬性, 只要更新資料將自動更新時間
    last_modify_date = models.DateTimeField(auto_now=True)
    # 建立日, 時間屬性, 只要新增資料將自動填入時間
    created = models.DateTimeField(auto_now_add=True)

    # Metadata
    # 參數可以參考 : https://docs.djangoproject.com/en/3.1/ref/models/options/
    class Meta:
        # 依照年齡排序，接著依照男女排序
        ordering = ['-age', 'is_female']

    # Methods
    def get_user_first_name(self):
        return self.name[:1]

    # 建議最少建立一個 __str__ 讓人了解 Model 是什麼
    def __str__(self):
        return self.name
