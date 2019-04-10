from django.db import models
from elasticsearch_dsl import DocType,Completion,Text,Date,Keyword,Integer
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['127.0.0.1'])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer('ik_max_word',filter=['lowercase'])


class ArticleType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"

class JianShuEs(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text()
    content = Text()
    url = Keyword()
    id = Keyword()
    date_time = Date()

    class Meta:
        index = 'jianshu'
        doc_type = "article"


