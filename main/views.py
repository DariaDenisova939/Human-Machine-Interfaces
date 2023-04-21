from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from main.forms import RegisterUserForm, LoginUserForm, AuthorsForm, ComplaintsForm, CourseForm, ApplicationForm, \
    TimetableForm
from main.models import Authors, Courses, Timetable, UsersCourses, Applications, Complaints


def index(request):
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    return render(request, 'main/index.html', {'count': len(Applications.objects.all()), 'rol': get_rol(request),
                                               'author': author})


def admin(request):
    return render(request, 'main/admin/')


def timetable(request):
    t_table = Timetable.objects.filter(id_user_id=request.user.id)
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    if not t_table.exists():
        t_table = 0
    return render(request, 'main/timetable.html/', {'t_table': t_table, 'rol': get_rol(request),
                                                    'author': author})


def complaint(request, pk):
    Complaints.objects.get(id=pk).delete()
    return output(request, 4)


def create_favorite_course(request, pk):
    UsersCourses.objects.create(id_user_id=request.user.id, id_course_id=pk)
    return course(request, pk)


def output_author_course(request):
    name = 'Мои курсы'
    description = 'У вас пока нет опубликованных курсов'
    courses = Courses.objects.all().filter(id_author=get_author(request).id)
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    if not courses.exists():
        courses = 0
    return render(request, 'main/favorite_courses.html', {'favorite_courses': courses, 'rol': get_rol(request),
                                                          'author': author, 'name': name, 'description': description})


def output_favorite_course(request):
    name = 'Избранные курсы'
    description = 'У вас нет избранных курсов'
    favorite_courses = Courses.objects.all().filter(userscourses__id_user_id=request.user.id)
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    if not favorite_courses.exists():
        favorite_courses = 0
    return render(request, 'main/favorite_courses.html', {'favorite_courses': favorite_courses, 'rol': get_rol(request),
                                                          'author': author, 'name': name, 'description': description})


def course(request, pk):
    flag = False
    crs = Courses.objects.all().filter(userscourses__id_user_id=request.user.id).filter(id=pk)
    if not crs.exists():
        flag = True
    obj_course = Courses.objects.get(id=pk)
    obj_author = Authors.objects.get(id=obj_course.id_author_id)
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    return render(request, 'main/course.html', {'obj_course': obj_course, 'obj_author': obj_author, 'flag': flag,
                                                'rol': get_rol(request), 'author': author})


def output_course(request):
    attributes = Courses.objects.all()
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    return render(request, 'main/courses.html', {'attributes': attributes, 'rol': get_rol(request),
                                                 'author': author})


def output(request, idx):
    names = ['Авторы', 'Курсы', 'Расписание', 'Заявки на авторство', 'Жалобы']
    paths = ['Authors/authors.html', 'courses.html', 'timetable.html',
             'authorship.html', 'complaint_output.html']
    models = [Authors, Courses, Timetable, Applications, Complaints]
    attributes = models[idx].objects.all()
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    data = {
        'attributes': attributes,
        'name': names[idx],
        'count': len(Applications.objects.all()),
        'count_complaints': len(Complaints.objects.all()),
        'rol': get_rol(request),
        'author': author
    }
    return render(request, 'main/' + paths[idx], data)


def update(request, pk, idx):
    paths = ['Authors/authors_create.html', 'course_create.html', 'Authors/author_update.html', 'deadline_create.html']
    forms = [AuthorsForm, CourseForm, AuthorsForm, TimetableForm]
    models = [Authors, Courses, Authors, Timetable]
    obj = models[idx].objects.get(id=pk)
    if request.method == 'POST':
        form = forms[idx](request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            if idx == 1:
                return output_author_course(request)
            if idx == 0:
                return output(request, 0)
            if idx == 2:
                return index(request)
            if idx == 3:
                return timetable(request)
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
        pk = get_author(request).id
    if idx == 2:
        pk = request.user.id
    data = {
        'form': forms[idx](instance=obj),
        'pk': pk,
        'rol': get_rol(request),
        'author': author,
        'operation': 'Изменить'
    }
    return render(request, 'main/' + paths[idx], data)


def authorship(request, flag, pk):
    obj = Applications.objects.get(id_user_id=pk)
    if flag == 'True':
        Authors.objects.create(id_user_id=User.objects.get(id=pk).id, name=obj.name, surname=obj.surname,
                               patronymic=obj.patronymic)
    obj.delete()
    return redirect('output', idx=3)


def delete(request, idx, pk):
    models = [Authors, Courses, Authors, UsersCourses, Courses, Timetable]
    paths = ['Authors/authors.html', 'courses.html', 'complaint_output.html',
             'users_courses.html']
    obj = models[idx].objects.get(id=pk)
    obj.delete()
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    if idx == 4:
        return output_author_course(request)
    if idx == 2 or idx == 1:
        return output(request, 4)
    if idx == 5:
        return timetable(request)
    else:
        attributes = models[idx].objects.all()
    return render(request, 'main/' + paths[idx], {'attributes': attributes,
                                                  'rol': get_rol(request), 'author': author})


def delete_check(request, idx, pk):
    author = 0
    if get_rol(request) == 'author':
        author = get_author(request)
    data = {
        'idx_tmp': idx,
        'pk_tmp': pk,
        'rol': get_rol(request),
        'author': author
    }
    return render(request, 'main/delete-entry.html', data)


def application_check(request):
    app = Applications.objects.filter(id_user_id=request.user.id)
    if app.exists():
        return 'Вы уже отправили заявку на авторство, подождите пока администратор рассмотрит ее'
    else:
        return 0


def create(request, idx, pk):
    names = ['Авторы', 'Жалоба', 'Курс', 'Заявка на авторство', 'Дедлайн']
    paths = ['Authors/authors_create.html', 'complaints.html', 'course_create.html', 'application_create.html',
             'deadline_create.html']
    forms = [AuthorsForm, ComplaintsForm, CourseForm, ApplicationForm, TimetableForm]
    error = ''
    if request.method == 'POST':
        form = forms[idx](request.POST)
        if form.is_valid():
            form.save()
        else:
            error = form.errors.get_json_data(escape_html=False)
    form = forms[idx]()
    author = 0
    user_message = 0
    rol = get_rol(request)
    if rol == 'author':
        author = get_author(request)
    if rol == 'user':
        user_message = application_check(request)
    data = {
        'form': form,
        'error': error,
        'name': names[idx],
        'pk': pk,
        'rol': get_rol(request),
        'author': author,
        'operation': 'Создать',
        'user_message': user_message
    }
    return render(request, 'main/' + paths[idx], data)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def get_rol(request):
    if request.user.is_superuser:
        rol = 'admin'
        return rol
    if Authors.objects.filter(id_user_id=request.user.id).exists():
        rol = 'author'
        return rol
    else:
        rol = 'user'
        return rol


def get_author(request):
    author = Authors.objects.get(id_user_id=request.user.id)
    return author
