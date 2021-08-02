from django.shortcuts import render
from rest_framework import generics
from denj.models import Denj, Review
from .serializers import DenjSerializer, ReviewSerializer
from rest_framework import permissions
from denj.permissions import IsDiscovererOrReadOnly


class DenjList(generics.ListCreateAPIView):
    queryset = Denj.objects.all()
    serializer_class = DenjSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(discoverer=self.request.user)

class DenjDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Denj.objects.all()
    serializer_class = DenjSerializer
    permission_classes = [IsDiscovererOrReadOnly]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(discoverer=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsDiscovererOrReadOnly]        
