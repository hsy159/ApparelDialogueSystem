import sys
from wit import Wit

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
access_token = sys.argv[1]

# Wit.ai의 Quickstart example 코드를 참조했습니다
# 원본: https://wit.ai/ar7hur/Quickstart

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value'] # text에서 변수 값을 추출해 저장합니다.
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response): #대답을 보내는 함수입니다.
    print(response['text'])
    context ={}
    #이전의 context가 남아있으면 엉뚱한 대답을 하기 때문에 초기화를 해줍니다.


def service_center(request): #
    request['context'] = {} 
    #이전의 context가 남아있으면 엉뚱한 대답을 하기 때문에 초기화를 해줍니다.
    context = request['context']
    entities = request['entities']

    context['service_center'] = 'phone number : 010-4734-6869\nE-mail : 061354@naver.com'
    return context

def ask_reason(request): #환불 방법에 대해 물으면 환불 이유를 되묻는 함수입니다.
    request['context'] = {} 
    #이전의 context가 남아있으면 엉뚱한 대답을 하기 때문에 초기화를 해줍니다.
    context = request['context']
    entities = request['entities']

    context['ask'] = 'What is the reason of refund?'
    return context

def delivery_ask(request): #배송조회를 하면 배송번호를 묻는 함수입니다.
    request['context'] = {} 
    #이전의 context가 남아있으면 엉뚱한 대답을 하기 때문에 초기화를 해줍니다.
    context = request['context']
    entities = request['entities']

    context['delivery_ask'] = 'Please enter valid invoice or tracking number.' # 배송 조회번호를 입력하라고 대답합니다.
    return context


def refund(request): #환불의 이유에 대한 반응을 결정하는 함수입니다.
    request['context'] = {} 
    #이전의 context가 남아있으면 엉뚱한 대답을 하기 때문에 초기화를 해줍니다.
    context = request['context']
    entities = request['entities']
    
    reason = first_entity_value(entities,'intent_reason') #환불 이유를 저장합니다.
    if reason == 'size':
        context['size'] = 'size'
    elif reason == 'change of my mind':
        context['change of my mind'] = 'change of my mind'
    return context

def delivery_answer(request): # 배송 조회번호가 1234거나 5678이면 2시에 도착한다하고 아니면 잘못됐다고 출력합니다.
    request['context'] = {}
    context = request['context']
    entities = request['entities']
    
    delivery_num = first_entity_value(entities,'intent_tracking_number') 
    
    if (delivery_num == '1234') | (delivery_num == '5678'):
        context['delivery_check'] = 'It will be arrival at 2pm today!'
    else:
        context['delivery_check'] = 'Tracking Numbers are not valid.'
    return context

actions = {
    'send': send,
    'service_center': service_center,
    'refund': refund,
    'ask_reason': ask_reason,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()
