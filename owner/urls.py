from django.urls import path
from .views import NewOwnerView, DogView
# . 은 내가 현재지금 있는 폴더 (owner) dhk views 는 형제 관계 

urlpatterns = [
    path('/ownerinfo', NewOwnerView.as_view()), # /owner 은 mydog url에서 처리, 빈스트링으로 남겨둠, as_view는 get,post 등을 불러줌
    path('/dog', DogView.as_view())
     ]
# localhost:8000/owner/owner
# localhost:8000/owner/dog
