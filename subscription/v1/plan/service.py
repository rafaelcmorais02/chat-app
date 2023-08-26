from subscription.models import Plan
from subscription.v1.plan.serializers import PlanResponseSerializer


def list_plans():
    plans = Plan.objects.all()
    return PlanResponseSerializer(instance=plans, many=True).data
