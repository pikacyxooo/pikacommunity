from django.shortcuts import render
from django.views.generic.base import View
from .models import ArticleType
from django.http import HttpResponse
import json


class SuggestView(View):
    def get(self,request):
        keyword = request.GET.get('s','')
        suggest_list = []
        s = ArticleType.search()
        s = s.suggest('my_suggest', keyword, completion={
            "field": "suggest",
            "fuzzy": {
                "fuzziness": 2
            },
            "size": 10
        })
        suggestions = s.execute_suggest()
        for match in suggestions.my_suggest[0].options:
            source = match['_source']
            suggest_list.append(source['title'])
        return HttpResponse(json.dumps(suggest_list), content_type="application/json")

class SearchView(View):
    pass


