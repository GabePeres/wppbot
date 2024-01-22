from botmessage import Replies
from twilio.twiml.messaging_response import MessagingResponse

class Usuario:
    def __init__(self, nome, numero, descricao, sistema):
        self.nome = nome
        self.numero = numero
        self.descricao = descricao
        self.sistema   = sistema

class BotOptions:
    SUPORTE    = '1'
    FINANCEIRO = '2'
    ORCAMENTO  = '3'
    TUTORIAL   = '4'

class BotDispatcher:
    #QUIZZ_FLOW = 7777

    def __init__(self, lang='br') -> None:
        self.lang = lang
    
    def reply(self, usermessage, NivelConversa):
           message = usermessage.lower()
           #if message[0] in BotOptions.SUPORTE:
           #    return BotDispatcher.SUPORTE       
           if (NivelConversa == 0):                
             if message == BotOptions.SUPORTE:
               NivelConversa = NivelConversa + 1                         
               return Replies.SUPORTE, NivelConversa
             elif message == BotOptions.FINANCEIRO:
               #NivelConversa = NivelConversa + 1 
               return Replies.FINANCEIRO
             elif message == BotOptions.ORCAMENTO:
               #NivelConversa = NivelConversa + 1 
               return Replies.ORCAMENTO
             elif message == BotOptions.TUTORIAL:
               #NivelConversa = NivelConversa + 1 
               return Replies.TUTORIAL
           elif (NivelConvesrsa == 1):               
             if   message == '1':
               #NivelConversa = NivelConversa + 1                
               Usuario.sistema = 'Folha_Win'
             elif message == '2':
               #NivelConversa = NivelConversa + 1                
               Usuario.sistema = 'Fiscal_New'
             elif message == '3':
               #NivelConversa = NivelConversa + 1                
               Usuario.sistema = 'Contabil'
             elif message == '4':
               #NivelConversa = NivelConversa + 1
               Usuario.sistema = 'Nfe'
             elif message == '5':
               Usuario.sistema = 'Outro (Recibos, caixa, nfe.....)' 
           elif (NivelConversa == 2):   
             #NivelConversa = NivelConversa + 1
             return Replies.SUP_NOME 
           elif (NivelConversa == 3):   
             #NivelConversa = NivelConversa + 1
             return Replies.SUP_NUMERO
           elif (NivelConversa == 4):   
             #NivelConversa = NivelConversa + 1
             return Replies.SUP_DESC    
           elif (NivelConversa == 5):   
             #NivelConversa = NivelConversa + 1
             return Replies.SUP_FIM                        
           else:
             #NivelConversa = NivelConversa + 1    
             return Replies.DEFAULT