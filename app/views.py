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
        return Response({'message':'false'})
