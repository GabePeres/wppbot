from botmessage import Replies
from twilio.twiml.messaging_response import MessagingResponse

class Usuario:
    def __init__(self, nome, numero, descricao, sistema, empresa):
        self.nome = nome
        self.numero = numero
        self.descricao = descricao
        self.sistema   = sistema
        self.empresa   = empresa

class BotOptions:
    SUPORTE    = '1'
    FINANCEIRO = '2'
    ORCAMENTO  = '3'
    TUTORIAL   = '4'

class BotDispatcher:
    #QUIZZ_FLOW = 7777
    
    def __init__(self, lang='br') -> None:
        self.lang = lang
    
    def reply(self, usermessage, Nconv):
           message = usermessage.lower()
           #if message[0] in BotOptions.SUPORTE:
           #    return BotDispatcher.SUPORTE       
           if (Nconv == 0):                
             if message == BotOptions.SUPORTE:
               #Nconv = Nconv + 1                         
               return Replies.SUPORTE
             elif message == BotOptions.FINANCEIRO:
               #Nconv = Nconv + 1 
               Nconv = -1
               return Replies.FINANCEIRO
             elif message == BotOptions.ORCAMENTO:
               #Nconv = Nconv + 1 
               Nconv = -1
               return Replies.ORCAMENTO
             elif message == BotOptions.TUTORIAL:
               #Nconv = Nconv + 1 
               Nconv = -1
               return Replies.TUTORIAL
           elif (Nconv == 1):               
             if   message == '1':
               #Nconv = Nconv + 1                
               Usuario.sistema = 'Folha_Win'
             elif message == '2':
               #Nconv = Nconv + 1                
               Usuario.sistema = 'Fiscal_New'
             elif message == '3':
               #Nconv = Nconv + 1                
               Usuario.sistema = 'Contabil'
             elif message == '4':
               #Nconv = Nconv + 1
               Usuario.sistema = 'Nfe'
             elif message == '5':
               Usuario.sistema = 'Outro (Recibos, caixa, nfe.....)' 
             return Replies.SUP_NOME   
           elif (Nconv == 2):   
             #Nconv = Nconv + 1
             Usuario.nome = message
             return Replies.SUP_NUMERO
           elif (Nconv == 3):   
             #Nconv = Nconv + 1
             Usuario.numero = message
             return Replies.SUP_EMPRESA   
           elif (Nconv == 4):   
             #Nconv = Nconv + 1
             Usuario.empresa = message
             return Replies.SUP_DESC   
           elif (Nconv == 5):   
             #Nconv = Nconv + 1
             Usuario.descricao = message
             Nconv = -1
             return f'*Obrigado pelo contato {Usuario.nome} seu chamado foi cadastrado!*'+f'\n\n  Sistema: {Usuario.sistema}\n  Nome: {Usuario.nome}\n  Número: {Usuario.numero}\n  Empresa: {Usuario.empresa}\n  Descrição: {Usuario.descricao}\n'+Replies.SUP_FIM
             #return Replies.SUP_FIM+Usuario.numero+Usuario.nome+Usuario.descricao                        
           else:
             #Nconv = Nconv + 1    
             return Replies.DEFAULT