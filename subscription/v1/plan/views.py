from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer
from subscription.models import Plan


class PlanListAPIView(ListAPIView):
    class PlanSerializer(ModelSerializer):
        class Meta:
            model = Plan
            fields = '__all__'
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
