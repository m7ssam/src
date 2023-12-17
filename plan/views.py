from django.shortcuts import redirect, render
from .models import Project
from .forms import PostProject
from django.contrib.auth.decorators import login_required
@login_required()
def projects(request):
  name = Project.objects.all()
  context = {"name": name}
  return render(request, 'plan/projects_list.html',context )


@login_required()
def home(request):
  name = Project.objects.all()
  context = {"name": name}
  return render(request, 'plan/plan_home.html',context )


@login_required()
def create_project(request):
  if request.method == 'POST':
    form = PostProject(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      return redirect("project_home")
  else:
    form = PostProject()
  context = {"form": form}
  return render (request, 'project/project_creation.html', context )

