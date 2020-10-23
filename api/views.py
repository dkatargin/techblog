import datetime
from rest_framework import generics, response, status
from .models import Entity
from .serializers import EntitySerializer, EntityDetailSerializer


class EntitiesView(generics.ListAPIView):
    queryset = Entity.objects.all().order_by('-creation_date')
    serializer_class = EntitySerializer


class EntitiesDetailView(generics.RetrieveAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntityDetailSerializer
    lookup_field = 'slug'


class CalendarView(generics.GenericAPIView):
    queryset = Entity.objects.all().order_by('-creation_date')

    def get(self, request):
        current_month = datetime.datetime.now().strftime("%Y-%m")
        date_str = request.GET.get('date', current_month)
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m")
        except ValueError:
            return response.Response({"msg": "Wrong date format. Please use YYYY-MM"},
                                     status=status.HTTP_400_BAD_REQUEST)

        timedelta = datetime.timedelta(days=31)
        qs = self.queryset.filter(creation_date__gte=date).filter(creation_date__lt=date + timedelta)
        result = {}
        for i in qs:
            i_data = {'title': i.title, 'slug': i.slug}
            if not result.get(i.creation_date):
                result[i.creation_date.day] = [i_data]
            else:
                result[i.creation_date.day].append(i_data)
        return response.Response(result, status=status.HTTP_200_OK)
