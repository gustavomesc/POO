import streamlit as st
from viwe import View
import pandas as pd
class AvaliacoesUI:
    def main():
        st.header("Avaliações dos profissionais")
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic=[]
            for p in profissionais:
                notas = p.get_notas()
                if len(notas) == 0:
                    pass
                else:
                    media_nota = sum(notas)/len(notas)
                    maior_nota = max(notas)
                    menor_nota = min(notas)
                    dic.append({"nome":p.get_nome(),"media":media_nota,"maior nota":maior_nota,"menor nota":menor_nota})
            df= pd.DataFrame(dic)
            st.dataframe(df)