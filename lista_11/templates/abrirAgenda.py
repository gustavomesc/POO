import streamlit as st
from viwe import View
import time
class PerfilClienteUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        horario_inicial = st.text_input("Informe o horário inicial no formato hh:mm")
        horario_final = st.text_input("Informe o horário final no formato hh:mm")
        intervalo = st.number_input("Informe o intervalo em minutos")
        if st.button("Abrir Agenda"):
            # Aqui você pode adicionar a lógica para abrir a agenda
            st.success("Agenda aberta com sucesso")
            time.sleep(2)
            st.rerun()