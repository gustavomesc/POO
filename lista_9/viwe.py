from models.clienteDAO import Cliente,ClienteDAO
from models.serviçoDAO import Serviço, ServiçoDAO
from models.horarioDAO import Horario,HorarioDAO
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
        def cliente_listar_id(id):
            ClienteDAO.listar_id(id)

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
        def servico_listar_id(id):
            ServiçoDAO.listar_id(id)

        def horario_inserir(data, confirmado, id_cliente, id_servico):
            c = Horario(0, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            HorarioDAO.inserir(c)

        def horario_listar():
            return HorarioDAO.listar()
        def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
            c= Horario(id, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            HorarioDAO.atualizar(c)
        def horario_excluir(id):
            c= Horario(id, None)
            HorarioDAO.excluir(c)
