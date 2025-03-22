from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from core.forms import ActivityRecordForm
from core.models import ActivityRecord


@login_required
def create_activity(request):
    if request.method == "POST":
        form = ActivityRecordForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("list_activities")
    else:
        form = ActivityRecordForm()
    return render(request, "core/activities/create.html", {"form": form})


@login_required
def list_activities(request):
    message = None
    if request.method == "POST":
        action = request.POST.get('action')
        activity_id = request.POST.get('id')
        if action == "delete":
            res = ActivityRecord.objects.filter(id=activity_id, user=request.user).delete()
            deleted = res[0]
            if deleted == 1:
                message = _("Successfully deleted activity record.")
            elif deleted == 0:
                message = _("Failed to delete activity record. (perhaps you don't have a permission for that or given activity does not exist?)")
    activities = ActivityRecord.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "core/activities/list.html", {"activities": activities, "message": message})