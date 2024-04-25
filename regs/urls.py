from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/",home),
    path("add-regs/",regs_add),
    path("delete-regs/<int:pid>",delete_regs),
    path("update-regs/<int:pid>",update_regs),
    path("do-update-regs/<int:pid>",do_update_regs),
]