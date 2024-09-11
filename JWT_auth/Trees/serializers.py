from rest_framework import serializers
from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['species_name', 'number_of_trees', 'age', 'height', 'width']
