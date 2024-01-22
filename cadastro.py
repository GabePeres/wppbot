from twilio.twiml.messaging_response import MessagingResponse

class Usuario:
    def __init__(self, nome, numero, descricao, sistema):
        self.nome = nome
        self.numero = numero
        self.descricao = descricao
        self.sistema   = sistema

def cad(userMessage):
    original_msg = userMessage.lower()
    if original_msg == '1':
        Usuario.sistema = 'Folha_Win'
    elif original_msg == '2':
        Usuario.sistema = 'Fiscal_New'
    elif original_msg == '3':
        Usuario.sistema = 'Contabil'
    elif original_msg == '4':
        Usuario.sistema = 'Nfe'
    elif original_msg == '5':
        Usuario.sistema = 'Outro (Recibos, caixa, nfe.....)'                
    else:
        MessagingResponse.message.body('Opção inválida!')

    MessagingResponse.message.body('Digite o seu nome:')
    original_msg = userMessage.lower()
    Usuario.nome = original_msg

    MessagingResponse.message.body('Digite o seu número para contato:')
    original_msg = userMessage.lower()
    Usuario.numero = original_msg

    MessagingResponse.message.body('Relate seu problema:')
    original_msg = userMessage.lower()
    Usuario.descricao = original_msg

    MessagingResponse.message.body('Chamado: \nSistema: {usuario.sistema}\nnome: {usuario.nome}\nnúmero: {usuario.numero}\ndescrição: {usuario.descricao}')

    return 'GabeGay'