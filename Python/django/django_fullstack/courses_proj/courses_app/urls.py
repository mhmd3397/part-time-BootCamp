from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('courses/comment/<int:course_id>', views.comment, name='comment'),
    path('courses/destroy/<int:course_id>', views.destroy, name='destroy'),
    path('courses/delete/<int:course_id>', views.delete, name='delete'),
]
