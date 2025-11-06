from models.clienteDAO import Cliente,ClienteDAO
from models.serviçoDAO import Serviço, ServiçoDAO
from models.horarioDAO import Horario,HorarioDAO
from models.profissionalDAO import Profissional,ProfissionalDAO
from datetime import datetime
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
        def admin_alterar_senha(nova_senha):
            for c in View.cliente_listar():
                if c.get_email() == "admin":
                    View.cliente_atualizar(c.get_id(), c.get_nome(), c.get_email(), c.get_fone(), nova_senha)
                    return None
        def cliente_listar():
            list = ClienteDAO.listar()
            list.sort(key=lambda x: x.get_nome().lower())
            return list
        def cliente_inserir(nome, email, fone,senha):
            emails = []
            for obj in View.cliente_listar():
                emails.append(obj.get_email())
            for obj in View.profissional_listar():
                emails.append(obj.get_email())
            print(emails)
            for e in emails:
                if email == e:
                    raise ValueError("Email já cadastrado em outro usuario")
            cliente = Cliente(0, nome, email, fone,senha)
            ClienteDAO.inserir(cliente)
        def cliente_atualizar(id, nome, email, fone,senha):
            emails = []
            for obj in View.cliente_listar():
                emails.append(obj.get_email())
            for obj in View.profissional_listar():
                emails.append(obj.get_email())
            for e in emails:
                if email == e:
                    raise ValueError("Email já cadastrado em outro usuario")
            cliente = Cliente(id, nome, email, fone,senha)
            ClienteDAO.atualizar(cliente)
        def cliente_excluir(id):
            for obj in View.horario_listar():
                if obj.get_id_cliente() == id:
                    raise ValueError("Cliente possui agendamentos: não é possível excluir")
            cliente = Cliente(id, None, None,None,None)
            ClienteDAO.excluir(cliente)
        def cliente_listar_id(id):
            return ClienteDAO.listar_id(id)

        def serviço_listar():
            list = ServiçoDAO.listar()
            list.sort(key=lambda x: x.get_descricao().lower())
            return list
        def serviço_inserir(descricao,valor):
            servico = Serviço(0,descricao,valor)
            ServiçoDAO.inserir(servico)
        def serviço_atualizar(id,descricao,valor):
            for obj in View.serviço_listar():
                if obj.get_id() != id and obj.get_descricao() == descricao:
                    raise ValueError("Descriçao já cadastrada em outro serviço")
            servico = Serviço(id,descricao,valor)
            ServiçoDAO.atualizar(servico)
        def serviço_excluir(id):
            for obj in View.horario_listar():
                if obj.get_id_servico() == id:
                    raise ValueError("Serviço já agendado: não é possível excluir")
            servico = Serviço(id,None,1)
            ServiçoDAO.excluir(servico)
        def servico_listar_id(id):
            return ServiçoDAO.listar_id(id)

        def horario_inserir(data, confirmado, id_cliente, id_servico,id_profissional):
            datas = []
            for obj in View.horario_listar():
                datas.append(obj.get_data())
            for d in datas:
                print(d)
                print(data)
                if data == d:
                    raise ValueError("Horario já cadastrado")
            c = Horario(0, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            c.set_id_profissional(id_profissional)
            HorarioDAO.inserir(c)
        def horario_listar():
            list = HorarioDAO.listar()
            list.sort(key=lambda x: x.get_data())
            return list
        def horario_atualizar(id, data, confirmado, id_cliente, id_servico,id_profissional):
            datas = []
            for obj in View.horario_listar():
                datas.append(obj.get_data())
            for d in datas:
                if data == d:
                    raise ValueError("Horario já cadastrado")
        def agendar_servico(id, data, confirmado, id_cliente, id_servico,id_profissional):
            c= Horario(id, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            c.set_id_profissional(id_profissional)
            HorarioDAO.atualizar(c)
        def horario_excluir(id):
            for h in View.horario_listar():
                if h.get_id() == id:
                    if h.get_id_cliente() != None:
                        raise ValueError("Horario já agendado: não é possível excluir")
            c= Horario(id, datetime.strptime("01/01/2025 00:00","%d/%m/%Y %H:%M"))
            return HorarioDAO.excluir(c)
        def horario_agendar_horario(id_profissional):
                r= []
                agora= datetime.now()
                for h in View.horario_listar():
                    if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                        r.append(h)
                r.sort(key= lambda h :h.get_data())
                return r
        
        def profissional_autenticar(email, senha):
            for c in View.profissional_listar():
                if c.get_email() == email and c.get_senha() == senha:
                    return {"id": c.get_id(), "nome": c.get_nome()}
        def profissional_listar():
            list = ProfissionalDAO.listar()
            list.sort(key=lambda x: x.get_nome().lower())
            return list
        def profissional_inserir(nome,especialidade,conselho, email,senha):
            emails = []
            for obj in View.cliente_listar():
                emails.append(obj.get_email())
            for obj in View.profissional_listar():
                emails.append(obj.get_email())
            for e in emails:
                if email == e:
                    raise ValueError("Email já cadastrado em outro usuario")
            profissional = Profissional(0, nome,especialidade,conselho, email,senha)
            ProfissionalDAO.inserir(profissional)
        def profissional_atualizar(id, nome,especialide,conselho, email,senha):
            emails = []
            for obj in View.cliente_listar():
                emails.append(obj.get_email())
            for obj in View.profissional_listar():
                emails.append(obj.get_email())
            for e in emails:
                if email == e:
                    raise ValueError("Email já cadastrado em outro usuario")
            profissional = Profissional(id, nome,especialide,conselho ,email,senha)
            ProfissionalDAO.atualizar(profissional)
        def profissional_excluir(id):
            for obj in View.horario_listar():
                if obj.get_id_profissional() == id:
                    raise ValueError("Profissional possui agendamentos: não é possível excluir")
            profissional = Profissional(id, None, None,None,None,None)
            ProfissionalDAO.excluir(profissional)
        def profissional_listar_id(id):
            return ProfissionalDAO.listar_id(id)
        def avaliar_profissional(profissional,nota):
            profissional.adicionar_nota(nota)
        def avaliacoes_profissional(profissional):
            return profissional.get_notas()

        def abrir_agenda(id_profissional, data, horario_inicial):
            horarios = HorarioDAO.listar()
            dataHorario = datetime.strptime(data+" "+horario_inicial, "%d/%m/%Y %H:%M")  
            View.horario_inserir(dataHorario, False, None, None, id_profissional)
        
