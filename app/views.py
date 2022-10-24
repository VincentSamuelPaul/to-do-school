from re import L
from django.shortcuts import render
from .signup import signUp
import os, csv

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    api_urls = {
        'index':'index'
    }
    return Response(api_urls)


@api_view(['POST'])
def signUp(request):
    username = str(request.data['username'])
    password = str(request.data['password'])
    
    cwd = os.getcwd()

    def sign(user):
        file1 = open(f'{cwd}/app/creds.csv','a',newline='')
        wr1 = csv.writer(file1)
        wr1.writerow([username,password])
        file = open(f'{cwd}/app/files/{user}.csv','w',newline='')
        wr = csv.writer(file)
        wr.writerow(['taskname','schedule','completed'])
        file.close()
        file1.close()
    file2 = open(f'{cwd}/app/creds.csv','r')
    rd = csv.reader(file2)
    found = False
    for i in rd:
        if username == i[0]:
            found = False
            break
        else:
            found = True
    file2.close()
    if found:
        sign(username)
        return Response({'message':'true'})
    else:
        return Response({'message':'username already exists'})


@api_view(['POST'])
def logIn(request):
    username = str(request.data['username'])
    password = str(request.data['password'])
    
    cwd = os.getcwd()
    # print([username,password])
    file1 = open(f'{cwd}/app/creds.csv','r')
    rd = csv.reader(file1)
    found = False
    for i in rd:
        if i == [username, password]:
            found = True
            break
    file1.close()
    if found:
        return Response({'message':'true'})
    else:
        return Response({'message':'Wrong username or password'})

@api_view(['POST'])
def getTasks(request):
    username = str(request.data['username'])
    cwd = os.getcwd()
    file1 = open(f'{cwd}/app/files/{username}.csv', 'r')
    rd = csv.reader(file1)
    tasks = []
    for i in rd:
        if i != ['taskname','schedule','completed']:
            tasks.append(i)
    return Response({'tasks':tasks})


@api_view(['POST'])
def addTask(request):
    username = str(request.data['user'])
    taskname = str(request.data['taskname'])
    day = str(request.data['day'])
    cwd = os.getcwd()
    file1 = open(f'{cwd}/app/files/{username}.csv', 'a')
    wr = csv.writer(file1)
    wr.writerow([taskname, day, 0])
    return Response('none')


@api_view(['POST'])
def deleteTask(request):
    username = str(request.data['username'])
    task = str(request.data['task'])
    cwd = os.getcwd()
    allTasks = []
    file1 = open(f'{cwd}/app/files/{username}.csv', 'r')
    rd = csv.reader(file1)
    for i in rd:
        if i[0] != task:
            allTasks.append(i)
    file1.close()
    file2 = open(f'{cwd}/app/files/{username}.csv', 'w')
    wr = csv.writer(file2)
    wr.writerows(allTasks)
    file2.close()
    return Response('hello')


@api_view(['POST'])
def completed(request):
    username = str(request.data['username'])
    task = str(request.data['task'])
    cwd = os.getcwd()
    allTasks = []
    file1 = open(f'{cwd}/app/files/{username}.csv', 'r')
    rd = csv.reader(file1)
    for i in rd:
        allTasks.append(i)
    for j in allTasks:
        if j[0] == task:
            j[2] = 1
    print(allTasks)
    file1.close()
    file2 = open(f'{cwd}/app/files/{username}.csv', 'w')
    wr = csv.writer(file2)
    wr.writerows(allTasks)
    file2.close()
    return Response('hello')