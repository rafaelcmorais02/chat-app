from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from subscription.models import Plan
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .service import list_plans


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


list_plan_response = openapi.Response('', PlanSerializer)


@swagger_auto_schema(method='GET', operation_description='List all Plans', responses={200: list_plan_response})
@api_view(['GET'])
def list_plan_view(request):
    plans = list_plans()
    return Response(data=PlanSerializer(instance=plans, many=True).data, status=200)
