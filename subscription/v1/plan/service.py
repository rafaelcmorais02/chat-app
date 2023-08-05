from subscription.models import Plan


def list_plans():
    return Plan.objects.all()
