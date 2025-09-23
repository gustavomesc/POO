from models.clienteDAO import Cliente,ClienteDAO
from models.serviçoDAO import Serviço, ServiçoDAO
class View:
        def cliente_listar():
            return ClienteDAO.listar()
        def cliente_inserir(nome, email, fone):
            cliente = Cliente(0, nome, email, fone)
            ClienteDAO.inserir(cliente)
        def cliente_atualizar(id, nome, email, fone):
            cliente = Cliente(id, nome, email, fone)
            ClienteDAO.atualizar(cliente)
        def cliente_excluir(id):
            cliente = Cliente(id, "", "", "")
            ClienteDAO.excluir(cliente)
        def serviço_listar():
            return ServiçoDAO.listar()
        def serviço_inserir(descricao,valor):
            servico = Serviço(0,descricao,valor)
            ServiçoDAO.inserir(servico)
        def serviço_atualizar(id,descricao,valor):
            servico = Serviço(id,descricao,valor)
            ServiçoDAO.atualizar(servico)
        def serviço_excluir(id):
            servico = Serviço(id,"","",)
            ServiçoDAO.excluir(servico)
