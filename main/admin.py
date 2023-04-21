from django.contrib import admin
from .models import Courses
from .models import Timetable
from .models import Authors
from .models import UsersCourses
from .models import Applications
from .models import Complaints

admin.site.register(Courses)
admin.site.register(Timetable)
admin.site.register(Authors)
admin.site.register(UsersCourses)
admin.site.register(Applications)
admin.site.register(Complaints)



