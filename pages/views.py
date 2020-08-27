import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from pos_tags.models import PosTag

from konlpy.tag import Hannanum, Twitter, Kkma, Mecab, Komoran

hannanum = Hannanum()
twitter = Twitter()
kkma = Kkma()
# mecab = Mecab()
komoran = Komoran()

class IndexView(View):
    def get(self, request):

        return render(request, 'pages/index.html')


class GetResult(View):
    def post(self, request):
        script = request.POST['script']

        return HttpResponse(json.dumps(self.analyzer(script)))

    def analyzer(self, text):
        result = []

        analyzer = 'Komoran'

        for morpheme_obj in komoran.pos(text):
            tag = morpheme_obj[1]
            if PosTag.objects.filter(analyzer=analyzer, tag=tag).exists():

                postag = PosTag.objects.get(analyzer=analyzer, tag=tag)
                result.append((morpheme_obj[0], morpheme_obj[1], postag.description))
            else:
                result.append((morpheme_obj[0], morpheme_obj[1], ''))

        print(result)

        return result

# [('분석', 'Noun'), ('할', 'Verb'), ('대본', 'Noun'), ('을', 'Josa'), ('넣어주세요', 'Verb')]
