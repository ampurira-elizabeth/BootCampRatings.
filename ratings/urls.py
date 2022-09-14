from django.urls import path


from . import views


urlpatterns=[
    path("register/",views.register_students, name="registration"),
    path("student/",views.list_students,name="liststudents"),
    
    path("facilitator/",views.register_learningfacilitators, name="facilitatorregistration"),
    path("facilitators/",views.list_facilitators,name="listsfacilitators")
    

]

