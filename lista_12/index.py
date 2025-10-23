from templates.manterclassUI import ManterClienteUI
from templates.manterservicoUI import ManterservicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from viwe import View
from templates.login import LoginUI
from templates.cadastro import AbrirContaUI
from templates.perfilCliente import PerfilClienteUI
from templates.perfilProfissional import PerfilProfissionalUI
from templates.agendarServiço import AgendarServicoUI
from templates.abrirAgenda import AbrirAgendaUI
from templates.vizualizarAgenda import VizualizarAgendaUI
from templates.meusServiços import MeusSerivicosUI
from templates.confirmarServiço import ConfirmarServicoUI
from templates.AdminSenha import AdminSenhaUI

import streamlit as st

class IndexUI:
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
    def menu_admin():
        op= st.sidebar.selectbox("Menu", ["Cadastro de Clientes","Cadastro de Serviços", "Cadastro de Horários","Cadastro de Profissionais","Alterar Senha do Administrador"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterservicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha do Administrador": AdminSenhaUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema","Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados","agendar Serviço","Meus serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "agendar Serviço": AgendarServicoUI.main()
        if op == "Meus serviços": MeusSerivicosUI.main()
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados","Abrir Agenda","Minha Agenda","Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Agenda": AbrirAgendaUI.main()
        if op == "Minha Agenda": VizualizarAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " +
            st.session_state["usuario_nome"])
            if admin: 
                IndexUI.menu_admin()
            elif st.session_state["categoria_usuario"] == "profissional": 
                IndexUI.menu_profissional()
            else: 
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()