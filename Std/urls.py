from django.urls import path,include
# from .views import StudentDetailAPIView
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api', views.StudentViewSet,basename='student')

urlpatterns = [

    path('api/get',views.get),
    path('api/post',views.post),
    path('api/update/<int:id>',views.update),
    path('api/delete/<int:id>',views.delete_api),
    path('api/',include(router.urls)),
    path('',views.student_form,name="form"),
    path('studentdetails/',views.student_list,name="studentdetails"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>',views.update_record,name='update'),
  
]