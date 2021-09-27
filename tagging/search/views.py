from blog.models import BlogPage, TopicTag, TypeTag, SponsorTag
from django.http import JsonResponse


def search(request):
  topics = request.GET.getlist('topics', None)
  types = request.GET.getlist('types', None)
  sponsors = request.GET.getlist('sponsors', None)
  data=[]
  tag_filters = {}

  if(topics):
    tag_filters["topic_tags__in"] = TopicTag.objects.filter(name__in=topics)
  if(types):
    tag_filters["type_tags__in"] = TypeTag.objects.filter(name__in=types)
  if(sponsors):
    tag_filters["sponsor_tags__in"] = SponsorTag.objects.filter(name__in=sponsors)
  print(tag_filters)
  results = BlogPage.objects.live().filter(**tag_filters).values()
  count = len(results)
  data = [r for r in results]
  data.append({"count" : count})
  return JsonResponse({'items':data}, safe=False)

