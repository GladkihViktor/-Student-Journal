from django.urls import path

from authorization.views import LoginWithToken, SigInView

urlpatterns = [
    path(route='login/', view=LoginWithToken.as_view(),
         name='login-with-token'),
    path(route='sigin/', view=SigInView.as_view(), name='sig-in'),
]
