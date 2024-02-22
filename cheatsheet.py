import streamlit as st
import pandas as pd 

def app():
    # Título
    st.title('Cheatsheet')

    # Cargar Dataframe
    cheatsheet_df = pd.read_excel('.\\files\\cheatsheet_streamlit.xlsx')

    # Secciones
    sections = cheatsheet_df['Tipo'].unique().tolist()

    # Funcion para filtrar tabla en base a su secciones
    def mostar_tabla(df, section):
        filtered_df = df[df['Tipo'] == section]
        return st.table(filtered_df.drop(columns=['Tipo']).style.set_table_styles([dict(selector="th", props=[("display", "none")])]))

    # Bucle para mostar el contenido del archivo cheatsheet_streamlit.xlsx
    for section in sections:
        st.subheader(section)
        mostar_tabla(cheatsheet_df, section)