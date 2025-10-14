import streamlit as st
from viwe import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        tab1,tab2 = st.tabs(["Cliente","Profissional"])
        with tab1: LoginUI.login_cliente()
        with tab2: LoginUI.login_profissional()
    def login_profissional():
        email = st.text_input("Informe o e-mail", key="login_email")
        senha = st.text_input("Informe a senha", type="password", key="login_senha")
        if st.button("Entrar", key="login_entrar"):
            c = View.profissional_autenticar(email, senha)
            if c is None:
                st.error("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["categoria_usuario"] = "profissional"
                st.rerun()
    def login_cliente():
        email = st.text_input("Informe o e-mail", key="login_email_cliente")
        senha = st.text_input("Informe a senha", type="password", key="login_senha_cliente")
        if st.button("Entrar", key="login_entrar_cliente"):
            c = View.cliente_autenticar(email, senha)
            if c is None:
                st.error("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["categoria_usuario"] = "cliente"
                st.rerun()
