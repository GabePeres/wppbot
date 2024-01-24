from botmessage import Replies

class Cliente:
  def __init__(self, nome, numero, descricao, sistema, empresa):
    self.nome      = nome
    self.numero    = numero
    self.descricao = descricao
    self.sistema   = sistema
    self.empresa   = empresa

class BotOptions:
    SUPORTE    = '1'
    FINANCEIRO = '2'
    ORCAMENTO  = '3'
    TUTORIAL   = '4'

class BotDispatcher:    
    def __init__(self, lang='br') -> None:
        self.lang = lang
    
    def reply(self, usermessage, Nconv):
           message = usermessage.lower()     
           if (Nconv == 0):                
             if message == BotOptions.SUPORTE:                    
               return Replies.SUPORTE
             
             elif message == BotOptions.FINANCEIRO:
               return Replies.FINANCEIRO
             
             elif message == 's':
                return Replies.SUP_FIM
             
             elif message == BotOptions.ORCAMENTO:
               return Replies.ORCAMENTO
             
             elif message == BotOptions.TUTORIAL:
               return Replies.TUTORIAL
             
           elif (Nconv == 1):               
             if   message == '1':           
               Cliente.sistema = 'Folha_Win'

             elif message == '2':           
               Cliente.sistema = 'Fiscal_New'

             elif message == '3':           
               Cliente.sistema = 'Contabil'

             elif message == '4':
               Cliente.sistema = 'Nfe'

             elif message == '5':
               Cliente.sistema = 'Outro (Recibos, caixa, nfe...)' 

             return Replies.SUP_NOME   
           
           elif (Nconv == 2):   
             Cliente.nome = message
             return Replies.SUP_NUMERO
           
           elif (Nconv == 3):   
             Cliente.numero = message
             return Replies.SUP_EMPRESA   
           
           elif (Nconv == 4):   
             Cliente.empresa = message
             return Replies.SUP_DESC   
           
           elif (Nconv == 5):   
             Cliente.descricao = message
             return f'*Obrigado pelo contato {Cliente.nome} seu chamado foi cadastrado!*'+f'\n\n  Sistema: {Cliente.sistema}\n  Nome: {Cliente.nome}\n  Número: {Cliente.numero}\n  Empresa: {Cliente.empresa}\n  Descrição: {Cliente.descricao}\n'+Replies.SUP_FIM                    
          
           else:   
             return Replies.DEFAULT