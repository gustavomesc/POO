from templates.manterclassUI import ManterClienteUI
from templates.manterservicoUI import ManterservicoUI
from templates.manterhorarioUI import ManterHorarioUI
import streamlit as st

class IndexUI:
    def menu_admin():
        op= st.sidebar.selectbox("Menu", ["Cadastro de Clientes","Cadastro de Serviços", "Cadastro de Horários"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterservicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
    def sidebar():
        IndexUI.menu_admin()
    def main():
        IndexUI.sidebar()

IndexUI.main()