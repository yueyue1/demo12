from django.shortcuts import render
from .models import TuWen
from .serializers import TuWenModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.
class UTF8CharsetJSONRenderer(JSONRenderer):
    charset = 'utf-8'


class GetTuWenView(APIView):
    renderer_classes = [UTF8CharsetJSONRenderer]
    def get(self, request):
        t_list = TuWen.objects.all()
        re = TuWenModelSerializer(t_list, many=True)
        return Response(re.data)

