import markdown
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    # 文章标题
    title = models.CharField(max_length=70)
    # 正文
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 改动时间
    modified_time = models.DateTimeField()
    # 摘要，允许为空
    excerpt = models.CharField(max_length=200, blank=True)
    # 字段记录阅读量
    views = models.PositiveIntegerField(default=0)
    # 分类和标签
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post, self).save(*args, **kwargs)