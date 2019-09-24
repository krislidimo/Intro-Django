from django.contrib import admin
from .models import Note
from .models import PersonalNote

class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified') # shows read only fields in the admin panel

# Register your models here.

admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)