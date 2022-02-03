from winreg import REG_QWORD
from django.shortcuts import render


def index(request): 

    return render(request, 'index.html')