from dao.serializers import ReadOnlyModelSerializer
from subscription.models import Plan


class PlanResponseSerializer(ReadOnlyModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
