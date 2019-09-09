from django.contrib import admin
from basicapp.model import note_model,user_model
# Register your models here.

admin.site.register(user_model.UserProfileInfo)
admin.site.register(note_model.Note)