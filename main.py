from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dispatch import BotDispatcher

app = Flask(__name__)

# Inicializa a variável com -1 fora da função
NivelConversa = -1

@app.route('/bot', methods=['POST'])
def bot():
    global NivelConversa  # Permite o acesso à variável global

    #print(request.values.get('Body', ''))  # Se quiser ver os parâmetros recebidos
    original_msg = request.values.get('Body', '')

    dispatch = BotDispatcher()
    botresponse = dispatch.reply(original_msg, NivelConversa)

    # Incrementa a variável
    NivelConversa += 1

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(botresponse)

    return str(resp)

@app.route('/')
def index():
    return "se quiser sim mano"

if __name__ == '__main__':
    app.run()
