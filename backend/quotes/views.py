from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Quote, Category
from .serializers import CategorySerializers, QuoteSerializers


# Create your views here.
@api_view(['GET', 'POST'])
def quotes_list(request):
    if request.method == 'GET':
        quotes = Quote.objects.all()
        quote_serializer = QuoteSerializers(quotes, many=True)
        return Response(quote_serializer.data)
    
    elif request.method == 'POST':
        quote_serializer = QuoteSerializers(data=request.data)
        if quote_serializer.is_valid():
            quote_serializer.save()
            return Response(data=quote_serializer.data, status=status.HTTP_201_CREATED)
        return Response(quote_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def quotes_details(request, id):
    try:
        quote = Quote.objects.get(pk=id)
    except Quote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        quote_serializer = QuoteSerializers(quote)
        return Response(quote_serializer.data)
    
    elif request.method == 'PUT':
        quote_serializer = QuoteSerializers(quote, data=request.data)
        if quote_serializer.is_valid():
            quote_serializer.save()
            return Response(data=quote_serializer.data, status=status.HTTP_200_OK)
        return Response(quote_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        category_serializer = CategorySerializers(categories, many=True)
        return Response(category_serializer.data)
    
    elif request.method == 'POST':
        category_serializer = CategorySerializers(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(data=category_serializer.data, status=status.HTTP_201_CREATED)
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_details(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        category_serializer = CategorySerializers(category)
        return Response(category_serializer.data)
    
    elif request.method == 'PUT':
        category_serializer = CategorySerializers(category, data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(data=category_serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)