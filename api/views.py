from home.models import Member
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-last_modify_date')
    serializer_class = MemberSerializer

    # 設定必須要有權限才可讀取
    # 可透過呼叫 api-auth/login 登入帳號
    permission_classes = [permissions.IsAuthenticated]


