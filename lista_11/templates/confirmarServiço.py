import streamlit as st
from viwe import View
import time
class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")
        horarios= []
        for horario in View.horario_listar():
            if not horario.get_confirmado():
                if horario.get_id_profissional() == st.session_state["usuario_id"]:
                    if View.cliente_listar_id(horario.get_id_cliente()) is not None:
                        horarios.append(horario)
        if len(horarios) == 0: 
            st.write("Nenhum Horário cadastrado")
        else:
            horario = st.selectbox("Selecione o horário para confirmar o serviço", horarios)
            if st.button("Confirmar Serviço"): 
                View.horario_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico(), horario.get_id_profissional())
                st.success("Serviço confirmado com sucesso")
                time.sleep(2)
                st.rerun()