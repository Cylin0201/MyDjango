from django.shortcuts import render
 
def post_list(request):
    return render(request, 'poems/자화상.html', {})
