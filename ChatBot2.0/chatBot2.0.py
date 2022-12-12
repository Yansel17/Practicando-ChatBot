import re
import random

nombre = input("Para empezar, dame tu nombre? :")
print("muy bien " +nombre +", voy hacerte variar preguntas con respecto a tu ciclo menstrual, para que puedas saber cuando será tu proximo ciclo en que etapa te encuentras y si hay dias de retraso.")

x = 0
print(isinstance(x,int))
cicloMenstr = input("Escribe cuando es tu proximo periodo? 'RESPONDE CON UN NUMERO' :")
print(len(cicloMenstr)) 
u = len(cicloMenstr)
print('')


for i in range(u):
    a= (cicloMenstr[i])
    print(a)
    y= ord(a)
    if ( y >=48 and y<=57):
      x = x + 1
        
        
  
if (x == u) :
      print('Es un entero')
else: 
      print ('no es entero')
        
      



 
#nombre = input("Para empezar, dame tu nombre? :")


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola '+nombre, ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('En que te puedo ayudar?', ['Necesito', 'ayuda', 'escuchame', 'dime'], single_response = True)
        #response('', ['quiero', 'saber', 'cuando', 'ciclo', 'menstrual', 'periodo', 'baja'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('Tu nombre es : '+nombre, ['nombre', 'mi', 'cual'], single_response = True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)


        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))