import json #post 에서 필요 (request)
from django.views import View
from django.http import JsonResponse
from .models import Owner
from .models import Dog
#from .models import Dog


# Create your views here.
class NewOwnerView(View) :

    def post(self, request) : #request 는 post 의 요청 , body 에 요청객체가 담겨있음
        try :
            # data = json.loads(request.body) # JSON -> python 변경필요 json.loads 잘들어왔는지 확인하려면 print
            # #print(data) #python dict 형태로 출력됨 , {'name' : '카드'}
            # data['name'] # 카드만 가져오려면 딕셔너리를 풀어줘야함
            # #name = data['name']
            # Owner.objects.create(name=data['name'], email=['email'], age = data['age']) # create

            #request 안에 body 가 있음/ but 바로 쓸 수 없는 형태로 존재
            #json 을 python으로 변경해주는 내장모듈(json.loads) 사용
            data = json.loads(request.body)
            # print(data['name'])
            # print(data['email'])
            # print(data['age'])
            Owner.objects.create(name=data['name'],email=data['email'],age=data['age'])
            
            
            
            return JsonResponse({'message':'SUCCESS!'}, status=201) #성공적으로 데이터베이스에 추가되었을 때 201
        
        except KeyError:
            
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)



class DogView(View) :
    def post(self, request) :

        try : 
            data = json.loads(request.body)

            owners = Owner.objects.get(email=data['owner']) #주인 이메일을 fk 물겠다
            
            
            Dog.objects.create(name=data['name'], age=data['age'], owner=owners)

            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError :
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)






