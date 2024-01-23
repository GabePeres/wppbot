from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dispatch import BotDispatcher

app = Flask(__name__)

NivelConversa = -1

@app.route('/bot', methods=['POST'])
def bot():
    global NivelConversa 
 
    if (NivelConversa == 6):
      NivelConversa = -1
      

    #print(request.values.get('Body', ''))  # Se quiser ver os parâmetros recebidos
    original_msg = request.values.get('Body', '')

    dispatch = BotDispatcher()
    botresponse = dispatch.reply(original_msg, NivelConversa)

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
