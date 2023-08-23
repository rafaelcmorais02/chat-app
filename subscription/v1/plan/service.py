from subscription.models import Plan
from subscription.v1.plan.serializers import PlanSerializer


def list_plans():
    plans = Plan.objects.all()
    return PlanSerializer(instance=plans, many=True).data
