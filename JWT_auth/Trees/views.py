from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tree
from .serializers import TreeSerializer
import math

@api_view(['GET'])
def get_trees(request):
    trees = Tree.objects.all()
    serializer = TreeSerializer(trees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_tree(request):
    serializer = TreeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_tree(request, pk):
    try:
        tree = Tree.objects.get(pk=pk)
    except Tree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TreeSerializer(tree, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_tree(request, pk):
    try:
        tree = Tree.objects.get(pk=pk)
    except Tree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tree.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def calculate_oxygen(tree):
    canopy_area = math.pi * (tree.width / 2) ** 2
    oxygen_per_year = canopy_area * 9.38
    if tree.age >= 20:
        adjusted_oxygen = oxygen_per_year * 0.7
    else:
        adjusted_oxygen = oxygen_per_year
    total_oxygen = adjusted_oxygen * tree.number_of_trees
    return total_oxygen

@api_view(['POST'])
def calculate_oxygen_production(request):
    serializer = TreeSerializer(data=request.data)
    if serializer.is_valid():
        tree_data = serializer.save()
        total_oxygen = calculate_oxygen(tree_data)
        return Response({"total_oxygen_kg_per_year": total_oxygen})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
