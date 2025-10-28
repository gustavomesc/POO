import streamlit as st
from viwe import View
class AdminSenhaUI:
    def main():
        st.header("alterar Senha do Administrador")
        senha = st.text_input("Informe a nova senha", type="password")
        if st.button("Alterar Senha"):
            View.admin_alterar_senha(senha)
            st.success("Senha alterada com sucesso")