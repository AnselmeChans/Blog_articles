from django.db import models

# Create your models here.
class PostCategory(models.Model): 
    name = models.CharField(max_length=50)

    def __str__(self) : 
        return self.name 

class Post(models.Model) : 
    title = models.CharField(max_length=100)
    category = models.ForeignKey('PostCategory', 
                                null=True, 
                                blank=True, 
                                on_delete= models.DO_NOTHING)
    published = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) : 
        return self.title

class Comment(models.Model) : 
    STATUS_VISIBLE  = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERTED = 'moderated'

    STATUS_CHOICE = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_MODERTED, 'Moderated'),
    )
    
    post = models.ForeignKey("Post", 
                            on_delete=models.CASCADE
                            )
    author = models.CharField(max_length=50)
    text = models.TextField()
    status= models.CharField(max_length=50, 
                            default=STATUS_VISIBLE, 
                            choices=STATUS_CHOICE)

    moderation_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    
