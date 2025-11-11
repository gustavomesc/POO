import streamlit as st
from viwe import View
import time
class AdminSenhaUI:
    def main():
        st.header("alterar Senha do Administrador")
        senha = st.text_input("Informe a nova senha", type="password")
        if st.button("Alterar Senha"):
            try:
                View.admin_alterar_senha(senha)
                st.success("Senha alterada com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
            
