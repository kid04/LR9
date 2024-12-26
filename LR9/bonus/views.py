from rest_framework import generics
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import UserLevel
from .permissions import IsOwner
from .filters import UserRequestFilter
from .serializers import BonusSerializer


class BonusAPIView(generics.ListAPIView):

    serializer_class = BonusSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):

        queryset = UserLevel.objects.filter(user=self.request.user)
        return queryset
