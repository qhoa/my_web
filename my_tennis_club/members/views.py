from django.http import HttpResponse
from django.shortcuts import render
from . models import Member
from . form import Registerform

def members(request):
    allmember = Member.objects.all().values()
    return render(request, 'all_member.html', {'allmember': allmember})

def details(request, id):
    detailmember = Member.objects.get(id=id)
    return render(request, 'detail_member.html', {'detailmember': detailmember})

def main(request):
    return render(request,'main.html')

def register(request):
    if request.method == 'POST':
        form = Registerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'register_member.html', {'form': form,'img_obj':img_obj})
    else:
        form = Registerform()
    return render(request, 'register_member.html', {'form':form})