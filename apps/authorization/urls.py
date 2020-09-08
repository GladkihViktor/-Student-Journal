from django.urls import path

from authorization.views import LoginWithToken, LogoutView, SigInView

urlpatterns = [
    path(route='login/', view=LoginWithToken.as_view(),
         name='login-with-token'),
    path(route='sigin/', view=SigInView.as_view(), name='sig-in'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
]
