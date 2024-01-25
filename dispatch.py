from botmessage import Replies

class Cliente:
  def __init__(self, nome, numero, descricao, sistema, empresa):
    self.nome      = nome
    self.numero    = numero
    self.descricao = descricao
    self.sistema   = sistema
    self.empresa   = empresa

class BotOptions:
    SUPORTE    = '1- suporte'
    FINANCEIRO = '2- financeiro'
    ORCAMENTO  = '3- orçamento'
    TUTORIAL   = '4- tutorial'

class BotDispatcher:    
    def __init__(self, lang='br') -> None:
        self.lang = lang
    
    def reply(self, usermessage, Nconv):
           message = usermessage.lower()     
           if (Nconv == 0):                
             if message in BotOptions.SUPORTE:                    
               return Replies.SUPORTE
             
             elif message in BotOptions.FINANCEIRO:
               return Replies.FINANCEIRO
             
             elif message in 'sim':
                return Replies.SUP_FIM
 
             elif message in 'nao':
                return Replies.ENCERRA
             
             elif message in BotOptions.ORCAMENTO:
               return Replies.TUTORIAL#Replies.ORCAMENTO
             
             elif message in BotOptions.TUTORIAL:
               return Replies.TUTORIAL
             
           elif (Nconv == 1):               
             if   message in '1- folha_Win':           
               Cliente.sistema = 'Folha_Win'

             elif message in '2- fiscal_New':           
               Cliente.sistema = 'Fiscal_New'

             elif message in '3- contabil':           
               Cliente.sistema = 'Contabil'

             elif message in '4- Nfe':
               Cliente.sistema = 'Nfe'

             elif message in '5- Outro':
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