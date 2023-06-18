from django.shortcuts import render, redirect
from .models import Course, Description, Comment
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')

        errors = Course.objects.basic_validator(request.POST)
        if errors:
            # If there are errors, render the form again with the errors
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                'name': name,
                'desc': desc,
                "courses": Course.objects.all()
            }
            return render(request, 'index.html', context)
        new_desc = Description.objects.create(description=desc)
        Course.objects.create(name=name, description=new_desc)
        return redirect('home')
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)


def comment(request, course_id):
    course = Course.objects.get(id=course_id)
    comments = Comment.objects.filter(course=course)

    if request.method == 'POST':
        text = request.POST.get('comment_text')

        # Perform any additional validation or processing for the comment data

        Comment.objects.create(course=course, text=text)
        return redirect('comment', course_id=course_id)

    context = {
        'course': course,
        'comments': comments,
    }
    return render(request, 'comment.html', context)


def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'course': course
    }
    return render(request, 'destroy.html', context)


def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('home')
