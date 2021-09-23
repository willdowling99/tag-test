from blog.models import BlogPage, TopicTag, TypeTag, SponsorTag
from django.http import JsonResponse


def search(request):
  topics = request.GET.getlist('topics', None)
  types = request.GET.getlist('types', None)
  sponsors = request.GET.getlist('sponsors', None)
  data=[]

  if(topics):
    topic_qs = TopicTag.objects.filter(name__in=topics)
  else:
    topic_qs = TopicTag.objects.all()
  if(types):
    type_qs = TypeTag.objects.filter(name__in=types)
  else:
    type_qs = TypeTag.objects.all()
  if(sponsors):
    sponsor_qs = SponsorTag.objects.filter(name__in=sponsors)
  else:
    sponsor_qs = SponsorTag.objects.all()

  
  results = BlogPage.objects.live().filter(topic_tags__in=topic_qs, type_tags__in=type_qs, sponsor_tags__in=sponsor_qs).values()
  count = len(results)
  data = [r for r in results]
  data.append({"count" : count})
  return JsonResponse({'items':data}, safe=False)

