from django.urls import path

from .views.CommandeView import create_commande
from .views.CommandeView import get_commande
from .views.CommandeView import get_commandes

from .views.LoginView import login
from .views.LoginView import getAll
from .views.LoginView import create_user
from .views.LoginView import logout_user


urlpatterns = [
    path('getOne/<commande_id>', get_commande, name="get_commande"),
    path('getAll', get_commandes, name="get_commandes"),
    path('create_commande', create_commande, name='create_commande'),
    path('loginUser', login , name='login_user'),
    path('getAllUsers', getAll, name='readall'),
    path('create', create_user, name='create_user'),
    path('logout/<str:username>', logout_user , name="logout"),
    ###path('delete/<int:user_id/', delete_user, name='delete_user'),

]
