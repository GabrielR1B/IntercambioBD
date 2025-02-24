import pandas as pd
import streamlit as st

# Importando os dados
dados = pd.read_csv('Universidades_Geral.csv')

# Título da página
st.title('Banco de Dados: Intercâmbio-UFMG ✈️')
st.write('Banco de Dados Criado para facilitar a procura e pesquisa de informações envolvendo intercâmbios pela UFMG.')

# Seleção de colunas para ocultar
st.write("### Escolha as colunas que deseja ocultar:")
colunas_disponiveis = list(dados.columns)
colunas_ocultas = st.multiselect("Ocultar colunas:", colunas_disponiveis, default=[])

# Filtro por país (seleção apenas dos países desejados)
st.write("### Escolha os países que deseja visualizar:")
paises = sorted(dados['País'].dropna().unique())
pais_selecionado = st.multiselect("Selecione um ou mais países:", paises)

# Filtro por língua de competência
st.write("### Escolha as línguas de competência desejadas:")
linguas_disponiveis = sorted(dados['Linguas_Competencia'].dropna().unique())
linguas_selecionadas = st.multiselect("Selecione uma ou mais línguas:", linguas_disponiveis)

# Opção para incluir universidades sem informação de Línguas de Competência
incluir_sem_lingua = st.checkbox("Incluir universidades sem informação de Línguas de Competência", value=False)

# Filtro por cursos em inglês (agora começa vazio)
st.write("### Escolha as opções de cursos em inglês desejadas:")
opcoes_cursos = ['Sim', 'Parcial/Condicional', 'Não']
cursos_ingles_selecionados = st.multiselect("Selecione as opções desejadas:", opcoes_cursos)

# Ordenação pelo ranking internacional
st.write("### Ordenar pelo Ranking Internacional")
ordenar_ranking = st.checkbox("Sim", value=False)

# Aplicando os filtros
if pais_selecionado:
    df_filtrado = dados[dados['País'].isin(pais_selecionado)]
else:
    df_filtrado = dados  # Se nenhum país for selecionado, mostra todos

# Filtro por Línguas de Competência
if linguas_selecionadas:
    if incluir_sem_lingua:
        df_filtrado = df_filtrado[df_filtrado['Linguas_Competencia'].isin(linguas_selecionadas) | df_filtrado['Linguas_Competencia'].isna()]
    else:
        df_filtrado = df_filtrado[df_filtrado['Linguas_Competencia'].isin(linguas_selecionadas)]
elif incluir_sem_lingua:
    df_filtrado = df_filtrado[df_filtrado['Linguas_Competencia'].isna()]

# Filtro por cursos em inglês
if cursos_ingles_selecionados:
    df_filtrado = df_filtrado[df_filtrado['Cursos_em_Ingles'].isin(cursos_ingles_selecionados)]

# Ordenação opcional pelo ranking internacional
if ordenar_ranking:
    df_filtrado = df_filtrado.sort_values(by='Ranking_Internacional', ascending=True)

# Removendo as colunas selecionadas para ocultar
df_exibido = df_filtrado.drop(columns=colunas_ocultas)

# Exibir tabela filtrada
st.write("### Dados Filtrados")
st.dataframe(df_exibido)

# Botão para baixar os dados filtrados
st.download_button(
    label="Baixar Dados Filtrados",
    data=df_exibido.to_csv(index=False),
    file_name="Universidades_Filtradas.csv",
    mime="text/csv"
)
