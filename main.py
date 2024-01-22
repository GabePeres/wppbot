from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dispatch import BotDispatcher


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
     
     print(request.values.get('Body', '')) #- se quiser ver os parâmetros recebidos
     original_msg = request.values.get('Body', '')

     dispatch = BotDispatcher()
     botresponse = dispatch.reply(original_msg, botresponse[1])
     #NivelConversa = NivelConversa + 1  #erro aqui                       

     resp = MessagingResponse()
     msg = resp.message()
     msg.body(botresponse[0])
    # msg.body('Funcionou!')

     return str(resp)

@app.route('/')
def index():
    return "eu tenho que me decidir"

if __name__ == '__main__':
     app.run()