from blog.models import TopicTag, SponsorTag, TypeTag
from django.http import JsonResponse


def tag(request):
  tag = request.GET.get('tag', None)
  topic_tag=[]
  type_tag=[]
  sponsor_tag=[]
  topics = TopicTag.objects.all().values('id', 'name')
  types = TypeTag.objects.all().values('id', 'name')
  sponsors = SponsorTag.objects.all().values('id', 'name')
  
  for topic in topics:
    topic_tag.append(topic)
  for type in types:
    type_tag.append(type)
  for sponsor in sponsors:
    sponsor_tag.append(sponsor)
  return JsonResponse(
      {
          'topic': topic_tag,
          'type': type_tag,
          'sponsor': sponsor_tag,
      },
      safe=False)

