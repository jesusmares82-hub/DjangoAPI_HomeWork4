from rest_framework.routers import DefaultRouter

from students.views import StudentViewset

router = DefaultRouter()
router.register('student', StudentViewset)

urlpatterns = router.urls
