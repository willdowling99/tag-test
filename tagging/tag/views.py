from blog.models import TopicTag, SponsorTag, TypeTag
from django.http import JsonResponse


def tag(request):
  t = request.GET.get('a', None)
  topic_tag=[]
  type_tag=[]
  sponsor_tag=[]
  aa = TopicTag.objects.all().values('id', 'name')
  bb = TypeTag.objects.all().values('id', 'name')
  cc = SponsorTag.objects.all().values('id', 'name')
  
  for a in aa:
    topic_tag.append(a)
  for b in bb:
    type_tag.append(b)
  for c in cc:
    sponsor_tag.append(c)
  return JsonResponse(
      {
          'topic': topic_tag,
          'type': type_tag,
          'sponsor': sponsor_tag,
      },
      safe=False)

