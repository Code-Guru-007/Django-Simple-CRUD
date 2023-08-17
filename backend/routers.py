from rest_framework import routers
from account.views import UserViewSets

router = routers.SimpleRouter()
router.register(r'user', UserViewSets, basename="user")