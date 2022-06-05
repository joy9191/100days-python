# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from models import BlogMsg
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

# @login_required
def get_list(request):
    data=BlogMsg.objects.all().values('id','title','content')
    return render(request, "bloglist.html", {"data":data})

# @login_required
def get_blog(request):
    bid = request.GET.get('id')
    data=BlogMsg.objects.get(id=bid)
    print(data)
    return render(request, "blog.html",{"data":data})

@csrf_exempt    
def add_blog(request):
    if request.method == 'GET':
        return render(request, "addblog.html")
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            b = BlogMsg.objects.create(title=title, content=content)
            print('提交成功')
            return redirect('/list')
        else:
            print('空')
            msg = '文章标题内容不能为空'
            return render(request, 'addblog.html',{'msg':msg})

@csrf_exempt
def edit_blog(request):
    if request.method == 'GET':
        bid = request.GET.get('id')
        data=BlogMsg.objects.filter(id=bid)
        return render(request, 'editblog.html',{'data':data})
    elif request.method == 'POST':
        bid = request.GET.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        d=BlogMsg.objects.filter(id=bid).update(title=title, content=content)
        print('修改成功')
        return redirect('/list')

@csrf_exempt
def del_blog(request):
    if request.method == 'POST':
        bid = request.POST.get('bid')
        d = BlogMsg.objects.filter(id=bid).delete()
        print(d)
        return redirect('/list')
        # if d:
        #     msg = '删除成功'
        # else:
        #     msg = '删除失败'
        # return render(request, '/list',{'msg':msg})

@csrf_exempt
def search(request):
    q = request.GET.get('q')
    if q:
        result_list = BlogMsg.objects.filter(title__icontains=q)
        print(result_list)
        return render(request, 'search.html',{'result_list':result_list})
    else:
        msg = '请输入关键词'

@csrf_exempt    
def crawler(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = request.POST.get('date')
        author = request.POST.get('author')
        print(title)
        print(content)
        if title and content:
            b = BlogMsg.objects.create(title=title, content=content, date=date, author=author)
            b.save()
            print('提交成功')
            response_data = str({'msg':'success'})
            return HttpResponse(response_data)
        else:
            response_data = str({'error':'文章标题内容不能为空'})
            return HttpResponse(response_data)

@csrf_exempt
def loginl(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        if next is None:
            next='/list'
        return render(request, 'login.html',{'nexturl':next})
    elif request.method == 'POST':
        nexturl=request.POST.get('nexturl')
        #接受 html name 是user和pwd的标签
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd', None)
        # 验证用户，验证成功返回User对象，失败返回None
        user_obj = auth.authenticate(username=user,password=pwd)
        if user_obj :
            auth.login(request,user_obj)
            if nexturl:
                return redirect(nexturl)
            else:
                pass
        elif user is None or pwd is None:
            msg = '用户名密码不能为空'
            return render(request, 'login.html',{'msg':msg})
        else:
            msg = '用户名密码错'
            return render(request, 'login.html',{'msg':msg})
    return  render(request, 'login.html',{'msg':'请登录'}) 

@csrf_exempt
def login(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        if next is None:
            next='/list'
        nexturl = '/login?next='+next
        return render(request, 'login.html',{'nexturl':nexturl})
    elif request.method == 'POST':
        nexturl=request.GET.get('next')
        #接受 html name 是user和pwd的标签
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd', None)
        # 验证用户，验证成功返回User对象，失败返回None
        user_obj = auth.authenticate(username=user,password=pwd)
        if user_obj :
            auth.login(request,user_obj)
            return redirect(nexturl)
        elif user is None or pwd is None:
            msg = '用户名密码不能为空'
            return render(request, 'login.html',{'msg':msg})
        else:
            msg = '用户名密码错'
            return render(request, 'login.html',{'msg':msg})
    return  render(request, 'login.html',{'msg':'请登录'}) 