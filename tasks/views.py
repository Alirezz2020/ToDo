from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5  # Number of tasks per page

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)  # Filter by logged-in user
        completed_filter = self.request.GET.get('completed')

        # Apply filtering based on completed status
        if completed_filter == 'true':
            queryset = queryset.filter(completed=True)
        elif completed_filter == 'false':
            queryset = queryset.filter(completed=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the filtered tasks
        tasks = self.get_queryset()
        page_number = self.request.GET.get('page', 1)  # Get current page, default to 1
        paginator = Paginator(tasks, self.paginate_by)  # Paginate the filtered tasks
        current_page = paginator.get_page(page_number)

        # Calculate offset for forloop.counter
        offset = (current_page.number - 1) * self.paginate_by

        context['tasks'] = current_page.object_list
        context['offset'] = offset
        context['current_page'] = current_page.number
        context['total_pages'] = paginator.num_pages
        context['completed'] = self.request.GET.get('completed', '')  # Preserve the completed filter value
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskSearchView(ListView):
    model = Task
    template_name = "tasks/task_search_results.html"
    context_object_name = "tasks"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query), user=self.request.user)
        return Task.objects.none()