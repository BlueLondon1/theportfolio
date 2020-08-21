from django.db import models

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nom")

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['name']

    def __str__(self):
        return self.name

# The portfolio get some posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey('PostCategory', null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="Catégorie")
    published = models.BooleanField(default=False)
    article_image = models.ImageField(blank=True, null= True)
    text = models.TextField(blank=True)
    goal = models.CharField(max_length=100, null=True)
    goalText = models.TextField(blank=True)
    languages = models.CharField(max_length=100, blank=True, null = True)
    languagesText =  models.TextField(blank=True)
    softwares = models.CharField(max_length=100, blank=True)
    softwaresText =  models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



