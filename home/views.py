from django.shortcuts import render
from typing import List

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


# 更新紀錄
def update_model(request, user_id, name):
    # 方法 1 :
    # 直接編輯物件
    # models.Member.objects.filter(id=user_id).update(name=name)

    # 方法 2 :
    # 使用 update 編輯
    # record = models.Member.objects.get(id=user_id)
    # record.update(name=name)

    # 方法 3 :
    # 使用物件編輯，並儲存
    record = models.Member.objects.get(id=user_id)
    record.name = name
    record.save()

    # object.get > 取得單一紀錄
    # object.filter > 返回符合條件陣列
    return render(request, 'home/update_model.html')


# 刪除記錄
def del_model(request, user_id):
    # 方法 1 :
    # 直接刪除物件
    # models.Member.objects.get(id=user_id).delete()

    # 方法 2 :
    # 刪除物件以刪除資料庫資料
    record = models.Member.objects.get(id=user_id)
    record.delete()

    return render(request, 'home/del_model.html')


# 讀取紀錄
def read_model(request, user_id):
    all_records = models.Member.objects.all()
    record = models.Member.objects.get(id=user_id)
    return render(request, 'home/read_model.html', {'all_records': all_records, 'record': record})
