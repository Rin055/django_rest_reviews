from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Review, Product
from .serializers import ReviewSerializer, ProductSerializer


class ReviewListCreateAPIView(APIView):
	def get(self, request):
		reviews = Review.objects.all()
		serializer = ReviewSerializer(reviews, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ReviewSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewRetrieveDeleteAPIView(APIView):
	def get(self, request, uuid):
		review = get_object_or_404(Review, uuid=uuid)
		serializer = ReviewSerializer(review)
		return Response(serializer.data)

	def delete(self, request, uuid):
		review = get_object_or_404(Review, uuid=uuid)
		review.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListCreateAPIView(APIView):
	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveAPIView(APIView):
	def get(self, request, pk):
		try:
			product = Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
		serializer = ProductSerializer(product)
		return Response(serializer.data)
