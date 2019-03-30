from CaseApp.models import Case
from CaseApp.serializers import CaseSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
import json
class CaseList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        print("heloooo")
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            content=serializer.save()
            radius_mean = content.radius_mean
            texture_mean = content.texture_mean
            perimeter_mean = content.perimeter_mean
            area_mean = content.area_mean
            smoothness_mean = content.smoothness_mean
            compactness_mean = content.compactness_mean
            concavity_mean = content.concavity_mean
            concave_points_mean = content.concave_points_mean
            symmetry_mean = content.symmetry_mean
            fractal_dimension_mean = content.fractal_dimension_mean



             #TODO:: triatment




            data={
                'diagnostic':'malin'
            }
            #OU BIEN

            data={
                'diagnostic':'bénin'
            }

            data={
                'diagnostic':'malin'
            }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CaseDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Case.objects.get(pk=pk)
        except Case.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        case = self.get_object(pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        case = self.get_object(pk)
        serializer = CaseSerializer(case, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        case = self.get_object(pk)
        case.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)