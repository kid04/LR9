from django_filters import rest_framework as filters

from bonus.models import UserLevel


class UserRequestFilter(filters.FilterSet):

    class Meta:
        model = UserLevel
        fields = ['user']

    @property
    def qs(self):
        parent = super().qs
        user = getattr(self.request, 'user', None)

        return parent.filter(user=user)
