from models import *
from django.views import View

class BoardListView(View):
    def get(self,request):