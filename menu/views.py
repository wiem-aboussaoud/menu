#menu/viewsets.py
from rest_framework import viewsets, status
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.schemas import AutoSchema
import coreapi
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MenuListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]: # those are two http request that allows client side to send payload
            extra_fields = [
                coreapi.Field("name"),
                coreapi.Field("description"),
                coreapi.Field("price"),

            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class MenuListCollection(APIView):

    schema = MenuListSchema()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        menues = Menu.objects.all()
        serializer = MenuSerializer(menues, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response({"success": True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()



