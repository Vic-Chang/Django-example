from django.shortcuts import render

# home 的 Controller
from home import models


def home(request):
    return render(request, 'home/home.html')


# 新增 Model Data
def add_model(request, name):
    # 方法 1 :
    # 使用 objects.create 創建物件並立即儲存置資料庫
    # models.Member.objects.create(name=name, is_female=True)

    # 方法 2 :
    # 建立物件後，呼叫 Save 即儲存
    record = models.Member(name=name, is_female=True)
    record.save()

    return render(request, 'home/add_model.html')
