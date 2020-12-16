from django.db import models
from datetime import date

# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.photo)


class PhotoFolder(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    photos = models.ManyToManyField(Photo, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def getDateFormat(self):
        today = date.today()
        yearToday = today.strftime('%y')
        monthToday = today.strftime('%m')
        dayToday = today.strftime('%d')
        year = self.date.strftime('%y')
        month = self.date.strftime('%m')
        day = self.date.strftime('%d')

        if yearToday != year:
            return f"{month}/{day}/{year}"
        if monthToday != month:
            return f"{month}/{day}"
        if dayToday != day:
            return f"{month}/{day}"
        return self.date.strftime('%I:%M %p ')

    # def limitView(self):

    #     if len(self.photos.filter()) > 1:
    #         return [self.photos.filter()[0]]
    #     return self.photos
