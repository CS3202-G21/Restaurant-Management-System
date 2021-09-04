from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CustomerSerializer, RegisterCustomerSerializer

# Register API
class RegisterCustomerAPI(generics.GenericAPIView):
    serializer_class = RegisterCustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        return Response({
            "user": CustomerSerializer(customer, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(customer)[1]
        })

# Login API

# Get Customer User API
