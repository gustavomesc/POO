import streamlit as st
import pandas as pd
import time
from viwe import View
class ManterProfissionalUI():
    def main():
        st.header("Cadastro de Profissional")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar","Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()
    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum Profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: 
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome= st.text_input("Informe o nome")
        especialidade= st.text_input("Informe a especialidade")
        conselho= st.text_input("Informe o conselho")
        email= st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, conselho,email,senha)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        profissionais= View.profissional_listar()
        if len(profissionais) == 0: 
            st.write("Nenhum Profissional cadastrado")
        else:
            op= st.selectbox("Atualização de Profissional", profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            especialidade = st.text_input("Novo especialidade", op.get_especialidade())
            conselho= st.text_input("Novo conselho", op.get_conselho())
            email = st.text_input("Novo e-mail", op.get_email())
            senha = st.text_input("Nova senha", op.get_senha(),type="password")
            if st.button("Atualizar"):
                id= op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho,email,senha)
                st.success("Profissional atualizado com sucesso")   
    def excluir():
        profissionais= View.profissional_listar()
        if len(profissionais) ==0: 
            st.write("Nenhum Profissional cadastrado")
        else:
            op= st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                id= op.get_id()
                View.profissionail_excluir(id)
                st.success("Profissional excluído com sucesso")   