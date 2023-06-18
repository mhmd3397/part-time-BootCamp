from django.db import models


class courseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # Validate Name
        name = postData.get('name')
        if not name:
            errors['name'] = "name is required."
        elif len(name) < 5:
            errors["name"] = "course name should be at least 5 characters"
        else:
            # Check if a course with the same name already exists
            existing_course = Course.objects.filter(
                name__iexact=name).first()
            if existing_course:
                errors['name'] = "A course with this name already exists."

        # Validate description
        desc = postData.get('desc')
        if not desc:
            errors['desc'] = "Description is required."
        if desc and len(desc) < 15:
            errors['desc'] = (
                "Description should be at least 15 characters if it exists.")

        return errors


class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = courseManager()


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
