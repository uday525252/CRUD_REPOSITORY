from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Movie
from django.urls import reverse_lazy
# Create your views here.




class MovieListView(ListView):
    model=Movie
    template_name="testapp/home.html"
    #context_variable_name="hello"
    #Default template/HTML=model_list.html////////movie_list.html
    #default context variable======model_list/////////movie_list


class MovieDetailView(DetailView):
    model=Movie
    #Default template/HTML=movie_detail.html
    #default context variable=movie


class MovieCreateView(CreateView):
    model=Movie
    fields=('title','hero','heroine','releasedate')



class MovieUpdateView(UpdateView):
    model=Movie
    fields=('title','hero','heroine','releasedate')



class MovieDeleteView(DeleteView):
    model=Movie
    success_url=reverse_lazy("detail")
