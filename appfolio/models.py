from django.db import models

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# The blog get some posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('PostCategory', null=True, blank=True, on_delete=models.DO_NOTHING)
    published = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# The blog can get comments from visitor
class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'visible'),
        (STATUS_HIDDEN, 'hidden'),
        (STATUS_MODERATED, 'moderated'),
    )

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(max_length=50, blank=True, default=STATUS_HIDDEN)
    text = models.TextField()
    status = models.CharField(max_length=20, default=STATUS_VISIBLE, choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} - {} (status={})'.format(self.author_name, self.author_email, self.text[:20], self.status)

