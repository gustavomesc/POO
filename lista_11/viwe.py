from models.clienteDAO import Cliente,ClienteDAO
from models.serviçoDAO import Serviço, ServiçoDAO
from models.horarioDAO import Horario,HorarioDAO
from models.profissionalDAO import Profissional,ProfissionalDAO
class View:
        def cliente_autenticar(email, senha):
            for c in View.cliente_listar():
                if c.get_email() == email and c.get_senha() == senha:
                    return {"id": c.get_id(), "nome": c.get_nome()}
            return None
        def cliente_criar_admin():
            for c in View.cliente_listar():
                if c.get_email() == "admin": 
                    return None
            View.cliente_inserir("admin", "admin", "fone", "1234")
        def cliente_listar():
            return ClienteDAO.listar()
        def cliente_inserir(nome, email, fone,senha):
            cliente = Cliente(0, nome, email, fone,senha)
            ClienteDAO.inserir(cliente)
        def cliente_atualizar(id, nome, email, fone,senha):
            cliente = Cliente(id, nome, email, fone,senha)
            ClienteDAO.atualizar(cliente)
        def cliente_excluir(id):
            cliente = Cliente(id, "", "", "","")
            ClienteDAO.excluir(cliente)
        def cliente_listar_id(id):
            return ClienteDAO.listar_id(id)

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
            return ServiçoDAO.listar_id(id)

        def horario_inserir(data, confirmado, id_cliente, id_servico,id_profissional):
            c = Horario(0, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            c.set_id_profissional(id_profissional)
            HorarioDAO.inserir(c)
        def horario_listar():
            return HorarioDAO.listar()
        def horario_atualizar(id, data, confirmado, id_cliente, id_servico,id_profissional):
            c= Horario(id, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            c.set_id_profissional(id_profissional)
            HorarioDAO.atualizar(c)
        def horario_excluir(id):
            c= Horario(id, None)
            return HorarioDAO.excluir(c)
        
        def profissional_autenticar(email, senha):
            for c in View.profissional_listar():
                if c.get_email() == email and c.get_senha() == senha:
                    return {"id": c.get_id(), "nome": c.get_nome()}
        def profissional_listar():
            return ProfissionalDAO.listar()
        def profissional_inserir(nome,especialidade,conselho, email,senha):
            profissional = Profissional(0, nome,especialidade,conselho, email,senha)
            ProfissionalDAO.inserir(profissional)
        def profissional_atualizar(id, nome,especialide,conselho, email,senha):
            profissional = Profissional(id, nome,especialide,conselho ,email,senha)
            ProfissionalDAO.atualizar(profissional)
        def profissional_excluir(id):
            profissional = Profissional(id, "", "", "","")
            ProfissionalDAO.excluir(profissional)
        def profissional_listar_id(id):
            return ProfissionalDAO.listar_id(id)
