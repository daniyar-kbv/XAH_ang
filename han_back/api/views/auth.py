from rest_framework.generics import CreateAPIView
from ..serializers.user import UserModelSerializer

class Register(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserModelSerializer

    def perform_create(self, serializer):
        return serializer.save()