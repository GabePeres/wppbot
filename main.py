import sys
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

    original_msg.lower()

    if firstChoice is None and original_msg == '1':
        #NivelConversa += 1
        firstChoice = original_msg
    
    if firstChoice == '1':
      NivelConversa += 1
    
    if (NivelConversa == 6) or (original_msg in 'sim'):
        NivelConversa = -2
        firstChoice = None

    if (botresponse != Replies.SUPORTE) and (botresponse is not None) and (firstChoice is not '1'):
        NivelConversa = 0
        #firstChoice = None
    
    if Replies.SUP_FIM in botresponse or Replies.ENCERRA in botresponse or Replies.TUTORIAL in botresponse:
        NivelConversa = -1
        firstChoice = None
        #botresponse = dispatch.reply(original_msg, NivelConversa)
        #sys.exit()

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(botresponse)


    return str(resp)

@app.route('/')
def index():
    return "se quiser sim mano"

if __name__ == '__main__':
    app.run()