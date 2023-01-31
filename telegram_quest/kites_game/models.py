from django.db import models

# Create your models here.


"""

RELATIONSHIP_CHOICES = [
    ('Good', 'Вы в хороших отношениях с '),
    ('Neutral', 'Вы в нейтральных отношениях с '),
    ('Bad', 'Вы повздорили с '),
    ('Unknown', 'Вы еще не знакомы с '),
]

LOCATION_STATE = [
    (0, 'not yet'),
    (1, 'here'),
    (2, 'have_been'),
]

"""

class Player(models.Model):
    chat_id = models.IntegerField()
    chapter_on = models.ForeignKey('Thread', on_delete=models.CASCADE, default=1)
    next_chapter = models.IntegerField(blank=True, default=0)

class Thread(models.Model):
    name = models.CharField(max_length=50, default='message', verbose_name='Наз')
    text = models.TextField()
    trigger = models.ManyToManyField('self', through='Thread_Trigger')

    def __str__(self):
        return self.name

    
class Thread_Trigger(models.Model):
    from_thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='from_thread')
    to_thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='to_thread')
    action = models.CharField(max_length=100)
    



