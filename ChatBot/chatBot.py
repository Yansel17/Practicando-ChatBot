from chatterbot import ChatBot
from chatterbot.trainer import ChatterBotCorpusTrainer
triner = ChatterBotCorpusTrainer(chat)
triner.train("chatterbot.corpus.spanish.greetings")
chat = ChatBot('cctmx')
while True:
    peticion = input('Tú: ')
    respuesta = chat.get_response(peticion)
    print('Bot: ', respuesta)