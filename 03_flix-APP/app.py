import streamlit as st


def main():
    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    if menu_option == 'Início':
        st.write('Inicio')

    if menu_option == 'Gêneros':
        st.write('Gêneros')

    if menu_option == 'Atores/Atrizes':
        st.write('Atores/Atrizes')

    if menu_option == 'Filmes':
        st.write('Filmes')

    if menu_option == 'Avaliações':
        st.write('Avaliações')

if __name__ == '__main__':
    main()
