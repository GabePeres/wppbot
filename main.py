from flask import Flask, request
from botmessage import Replies
from twilio.twiml.messaging_response import MessagingResponse
from dispatch import BotDispatcher

app = Flask(__name__)

NivelConversa = -1
firstChoice = None

@app.route('/bot', methods=['POST'])
def bot():
    global NivelConversa 
    global firstChoice
 
    #print(request.values.get('Body', ''))  # Se quiser ver os parâmetros recebidos
    original_msg = request.values.get('Body', '')

    dispatch = BotDispatcher()
    botresponse = dispatch.reply(original_msg, NivelConversa)
      
    if (NivelConversa == 6) or (original_msg == 's'):
      NivelConversa = -2
      #firstChoice = -1

    NivelConversa += 1
    
    
    #if (firstChoice == 1):
    #  NivelConversa = 1

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(botresponse)

    if (botresponse != Replies.SUPORTE) and (botresponse != None):
      #firstChoice = -1
      NivelConversa = 0

    return str(resp)

@app.route('/')
def index():
    return "se quiser sim mano"

if __name__ == '__main__':
    app.run()
