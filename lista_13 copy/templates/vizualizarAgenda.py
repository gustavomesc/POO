import streamlit as st
from viwe import View
import pandas as pd
class VizualizarAgendaUI:
    def main():
        st.header("Minha Agenda")
        horarios= []
        for horario in View.horario_listar():
            if horario.get_id_profissional() == st.session_state["usuario_id"]:
                horarios.append(horario)
        if len (horarios) ==0: 
            st.write("Nenhum horário cadastrado")
        else:
            dic= []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico= View.servico_listar_id(obj.get_id_servico())
                profissional=View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: 
                    cliente= cliente.get_nome()
                if servico != None: 
                    servico = servico.get_descricao()
                if profissional != None: 
                    profissional = profissional.get_nome()
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                "serviço" : servico,"profissional":profissional})
            df= pd.DataFrame(dic)
            st.dataframe(df)