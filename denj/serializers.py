from rest_framework import serializers
from .models import Denj, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    denj = serializers.HyperlinkedRelatedField(
        view_name='denj_detail', read_only=True)

    denj_name = serializers.SlugRelatedField(
        queryset=Denj.objects.all(), slug_field='name', source='denj')

    discoverer = serializers.ReadOnlyField(source='discoverer.username')

    class Meta:
        model = Review
        fields = ('denj_name','id', 'denj', 'title',
                  'body','image', 'created',  'discoverer')



class DenjSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    Denj_url = serializers.ModelSerializer.serializer_url_field(
        view_name='denj_detail')
    discoverer = serializers.ReadOnlyField(source='discoverer.username')

    class Meta:
        model = Denj
        fields = ('id', 'name', 'category', 'reviews',
                  'Denj_url', 'discoverer','location','state','gears'
                  ,'caption','created','image')