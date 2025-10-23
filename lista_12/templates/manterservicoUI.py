import streamlit as st
import pandas as pd
import time
from viwe import View
class ManterservicoUI():
    def main():
        st.header("Cadastro de Serviço")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar","Excluir"])
        with tab1: ManterservicoUI.listar()
        with tab2: ManterservicoUI.inserir()
        with tab3: ManterservicoUI.atualizar()
        with tab4: ManterservicoUI.excluir()
    def listar():
        servicos = View.serviço_listar()
        if len(servicos) == 0: 
            st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos: 
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        descricao= st.text_input("Informe a descrição")
        valor= st.text_input("Informe o valor")
        if st.button("inserir"):
            View.serviço_inserir(descricao,valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        serviços= View.serviço_listar()
        if len(serviços) == 0: 
            st.write("Nenhum serviço cadastrado")
        else:
            op= st.selectbox("Atualização de Serviço", serviços)
            descricao = st.text_input("Novo descricao", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            if st.button("Atualizar"):
                id= op.get_id()
                View.serviço_atualizar(id,descricao,valor)
                st.success("Serviço atualizado com sucesso")   
    def excluir():
        serviços= View.serviço_listar()
        if len(serviços) ==0: 
            st.write("Nenhum serviço cadastrado")
        else:
            op= st.selectbox("Exclusão de Serviço", serviços)
            if st.button("Excluir"):
                id= op.get_id()
                View.serviço_excluir(id)
                st.success("Serviço excluído com sucesso")