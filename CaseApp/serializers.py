from rest_framework import serializers
from CaseApp.models import *


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ('id',
                  'radius_mean',
                  'texture_mean',
                  'perimeter_mean',
                  'area_mean',
                  'smoothness_mean',
                  'compactness_mean',
                  'concavity_mean',
                  'concave_points_mean',
                  'symmetry_mean',
                  'fractal_dimension_mean',
                  'diagnostic')