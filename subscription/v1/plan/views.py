from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from subscription.models import Plan
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .service import list_plans


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


@swagger_auto_schema(method='GET', operation_description='List all Plans')
@api_view(['GET'])
def list_plan_view(request):
    plans = list_plans()
    return Response(data=PlanSerializer(instance=plans, many=True).data, status=200)
