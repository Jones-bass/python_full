import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'X-men'
    },
    {
        'id': 3,
        'name': 'Superman'
    },
]
    
def show_movies():
    st.write('Lista de Filmes:')
    
    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )

