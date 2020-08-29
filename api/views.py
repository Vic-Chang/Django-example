from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


@api_view(['GET', 'POST'])
def member_all_data(request, format=None):
    if request.method == 'GET':
        snippets = Member.objects.all()
        serializer = MemberSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
