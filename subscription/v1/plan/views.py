from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .service import list_plans
from subscription.v1.plan.serializers import PlanResponseSerializer


openapi_plan_response = openapi.Response('', PlanResponseSerializer)


@swagger_auto_schema(method='GET', operation_description='List all Plans', responses={200: openapi_plan_response})
@api_view(['GET'])
def list_plan_view(request):
    plans = list_plans()
    return Response(data=plans, status=200)
