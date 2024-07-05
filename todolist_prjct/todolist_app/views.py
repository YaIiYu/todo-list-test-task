from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    tags = Tag.objects.all()
    print(f"tag qua: {len(tags)}")
    for tag in tags:
        print(f"Tag: {tag.name}")
    return render(request, 'templates/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            new_tags = request.POST.get('new_tags', '')
            print(f"Tags: {new_tags}")
            if new_tags:
                tags = new_tags.split(',')
                for tag_name in tags:
                    tag_name = tag_name.strip()
                    if tag_name:
                        tag, created = Tag.objects.get_or_create(name=tag_name)
                        task.tags.add(tag)
            task.save()

        return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def complete(request, task_id, status):
    task = get_object_or_404(Task, id=task_id)
    if status != 'done':
        task.status = 'done'
    else:
        task.status = 'not_done'
    task.save()
    return redirect('home')

def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'templates/update_task.html', {'form': form, 'task': task})

def remove(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'templates/tags.html', {'tags': tags})