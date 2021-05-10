from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from num_to_english.numbers_to_english import NumberToWords
import json
from django.http import HttpResponse

@api_view(['GET'])
def num_to_english_view(request):
    """
    Numbers JSON REST View
    """
    try:

        numbers = NumberToWords()
        number = request.GET["number"]
        num = numbers.number_to_words(number)
        to_json = {
            "status": "ok",
            "num_to_english": num
        }

        return HttpResponse(json.dumps(to_json))

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def numbers_detail(request, pk, format = None):
    """
    Numbers REST View
    """
    try:
        numbers = NumberToWords()
        num = numbers.number_to_words(pk)

    except numbers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        json_response = {"status": "ok",
                         "num_in_english": num}
        return Response(json_response)


