from django.shortcuts import render
from django.views.generic.base import View
from .models import ArticleType
from django.http import HttpResponse
from elasticsearch import Elasticsearch
import json

client = Elasticsearch(hosts=['127.0.0.1'])


class SuggestView(View):
    def get(self, request):
        keyword = request.GET.get('s', '')
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
    def get(self, request):
        key_word = request.GET.get('q', '')
        page = request.GET.get('p','1')
        try:
            page = int(page)
        except:
            page = 1
        response = client.search(
            index="_all",
            body={
                "indices_boost": {
                    "jianshu": 2,
                    "jobbole": 1
                },
                "query": {
                    "multi_match": {
                        "query": key_word,
                        "fields": ["title^10", "content"]
                    }
                },
                "from": (page-1)*10,
                "size": 10,
                "highlight": {
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "title": {},
                        "content": {},
                    }
                }
            }
        )
        totol_nums = response['hits']['total']
        hits_list = []
        for hit in response['hits']['hits']:
            hit_dict = {}
            hit_dict['index_from'] = hit['_index']
            if 'title' in hit['highlight']:
                hit_dict['title'] = "".join(hit['highlight']['title'])
            else:
                hit_dict['title'] = hit['_source']['title']
            if 'content' in hit['highlight']:
                hit_dict['content'] = "".join(hit['highlight']['content'][:500])
            else:
                hit_dict['content'] = hit['_source']['content'][:500]
            hit_dict['date_time'] = hit['_source']['date_time']
            hit_dict['url'] = hit['_source']['url']
            hit_dict['score'] = hit['_score']
            hits_list.append(hit_dict)
        return render(request,'search.html',{
            'hits_list':hits_list,
            'total_nums':totol_nums,
            'page':page,
            'key_word':key_word,
        })
