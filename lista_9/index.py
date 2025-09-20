from templates.manterclassUI import ManterClienteUI
from templates.manterservicoUI import ManterservicoUI
import streamlit as st
class IndexUI:
    def main():
        st.header("Sistema de agendamento")
        tab1,tab2= st.tabs(["Cliente", "Serviço"])
        with tab1: ManterClienteUI.main()
        with tab2: ManterservicoUI.main()
IndexUI.main()