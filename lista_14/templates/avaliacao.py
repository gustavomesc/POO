import streamlit as st
from viwe import View
import time
class AvaliacaoUI:
    def main():
        st.header("Avalição dos profissionais")
        profs= View.profissional_listar()
        if len(profs) == 0: 
            st.write("Nenhum profissional cadastrado")
        else:
            profissional= st.selectbox("Informe o profissional", profs)
            nota = st.selectbox("Informe a nota de 1 a 10",[1,2,3,4,5,6,7,8,9,10])
            if st.button("Avaliar"):
                try:
                    View.avaliar_profissional(profissional,nota)
                    st.success("Agenda aberta com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
            
            