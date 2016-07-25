from django.db import models
from django.utils import timezone

# # defines our model
# # class - special key word that indicates we are defiing an object
# # Post - name of the model (always start with capital, don't inclue white spaces)
# # models.Model means the Post is a Django model (knows to save it in the database)
# # model fields and how to define things: https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types
class Post(models.Model):
    # 	# link to another model
    author = models.ForeignKey('auth.User')
    # 	# text with limited number of characters
    title = models.CharField(max_length=200)
    # 	# text without limits
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    # 	# def - means its a fucntion/method
# 	# publish - name of the method (should use lowercase and _ in names)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
