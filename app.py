import pandas as pd
import streamlit as st

# Importando os dados
dados = pd.read_csv('Universidades_Geral.csv')

# Título da página
st.title('Banco de Dados: Intercâmbio-UFMG ✈️')
st.write('Banco de Dados Criado para facilitar a procura e pesquisa de informações envolvendo intercâmbios pela UFMG.')
st.write('Esse Banco de Dados contém informações sobre todas as universidades que ofereceram vagas para intercâmbio pela UFMG desde 2024. O intuito desse banco é auxiliar no processo de pesquisa de uma universidade ideal para os alunos.')
st.write("## ⚠️ ATENÇÃO: Esse não é um Banco de Dados de vagas que estão sendo oferecidas mas de universidades que ne algum momento ja ofereceram vagas, para encontrar o quadro de vagas de intercambio atual consulte o site da DRI, o intuito aqui é somente agrupar informaçoes uteis para facilitar pesquisas.")
st.write("## ⚠️ ATENÇÃO: Esse foi um esforço voluntário de uma pessoa, e a qualidade de acesso às informações sobre as universidades pode variar muito. Portanto, sempre faça checagem dos fatos depois da sua pesquisa.")

# Seção: Dicionário de Dados
st.write("## 📖 Dicionário de Dados")
with st.expander("Clique aqui para visualizar a descrição das colunas 📚"):
    st.markdown("""
    - **Nome**: Nome da universidade.  
    - **País**: País onde a universidade está localizada.  
    - **Cidade**: Cidade onde a universidade está localizada.  
    - **Ranking_Internacional**: Posição da universidade no "QS World University Rankings". Caso não haja informação sobre a universidade no ranking, o campo estará vazio. É possível que múltiplas universidades ocupem a mesma posição, pois algumas são classificadas dentro de intervalos, como 1200-1400.  
    - **Linguas_Competencia**: Nível de proficiência em línguas exigido pela universidade para admissão. Caso esteja vazio, não há exigências linguísticas. || Significa Ou. 
    - **Taxas_Extras**: Informações sobre taxas adicionais cobradas pela universidade. Isso inclui apenas custos específicos da instituição, como "tuition fees" ou impostos regionais. Não cobre custos de vida, viagem ou vistos. "VRC" indica que o valor pode variar conforme o curso ou o semestre.  
    - **Cursos_em_Ingles**: Indica se a universidade oferece cursos em inglês. "Sim" significa que todos os cursos disponíveis para intercambistas são ministrados em inglês. "Parcial/Condicional" significa que apenas alguns cursos são oferecidos nesse idioma ou estão disponíveis apenas em determinados períodos do ano. "Não" indica que a universidade não oferece cursos em inglês.  
    - **Auxilio_Monetario**: Informações sobre bolsas ou auxílios financeiros disponíveis. "Sim" significa que há auxílio garantido e em valor suficiente. "Parcial/Condicional" significa que há algum auxílio, mas ele pode ser insuficiente ou estar sujeito a condições, como bolsas de estudo específicas. "Não" indica que a universidade não oferece nenhum tipo de auxílio financeiro. **Atenção**: Este campo se refere apenas a auxílios e bolsas oferecidos diretamente pela universidade. Programas de apoio do país não são considerados aqui.  
    - **Auxilio_Moradia**: Informações sobre apoio e assistência com moradia. "Sim" significa que há moradias gratuitas e garantidas para intercambistas. "Parcial/Condicional" indica que a universidade oferece moradia, mas em quantidade limitada (portanto, não garantida) ou que pode não ser gratuita, mas com descontos para intercambistas. "Não" significa que não há qualquer tipo de auxílio, sendo responsabilidade do aluno encontrar moradia por conta própria.  
    - **Data_Inspecao**: Última data de inspeção ou atualização das informações.  
    - **Link_Universidade**: Link para o site oficial da universidade. Sempre que possível, o link leva diretamente à página relacionada à internacionalização. Caso essa informação não esteja disponível, um link genérico para o site da instituição é fornecido.  
    """)


# Seção: Filtros

# Seleção de colunas para ocultar
st.write("### Escolha as colunas que deseja ocultar:")
colunas_disponiveis = list(dados.columns)
colunas_ocultas = st.multiselect("Ocultar colunas:", colunas_disponiveis, default=[], key="filtro_colunas")

# Filtro por país
st.write("### Escolha os países que deseja visualizar:")
paises = sorted(dados['País'].dropna().unique())
pais_selecionado = st.multiselect("Selecione um ou mais países:", paises, key="filtro_paises")

# Filtro por língua de competência
st.write("### Escolha as línguas de competência desejadas:")
linguas_disponiveis = sorted(dados['Linguas_Competencia'].dropna().unique())
linguas_selecionadas = st.multiselect("Selecione uma ou mais línguas:", linguas_disponiveis, key="filtro_linguas")

# Opção para incluir universidades sem informação de Línguas de Competência
incluir_sem_lingua = st.checkbox("Incluir universidades sem informação de Línguas de Competência", value=False, key="filtro_sem_lingua")

# Filtro por cursos em inglês
st.write("### Escolha as opções de cursos em inglês desejadas:")
opcoes_cursos = ['Sim', 'Parcial/Condicional', 'Não']
cursos_ingles_selecionados = st.multiselect("Selecione as opções desejadas:", opcoes_cursos, key="filtro_cursos_ingles")

# Filtro por Auxílio Monetário
st.write("### Escolha as opções de auxílio monetário desejadas:")
opcoes_auxilio_monetario = ['Sim', 'Parcial/Condicional', 'Não']
auxilio_monetario_selecionado = st.multiselect("Selecione as opções desejadas:", opcoes_auxilio_monetario, key="filtro_auxilio_monetario")

# Filtro por Auxílio Moradia
st.write("### Escolha as opções de auxílio moradia desejadas:")
opcoes_auxilio_moradia = ['Sim', 'Parcial/Condicional', 'Não']
auxilio_moradia_selecionado = st.multiselect("Selecione as opções desejadas:", opcoes_auxilio_moradia, key="filtro_auxilio_moradia")

# Ordenação pelo ranking internacional
st.write("### Ordenar pelo Ranking Internacional")
ordenar_ranking = st.checkbox("Sim", value=False, key="filtro_ranking")

# Aplicando os filtros
df_filtrado = dados

if pais_selecionado:
    df_filtrado = df_filtrado[df_filtrado['País'].isin(pais_selecionado)]

if linguas_selecionadas:
    if incluir_sem_lingua:
        df_filtrado = df_filtrado[df_filtrado['Linguas_Competencia'].isin(linguas_selecionadas) | df_filtrado['Linguas_Competencia'].isna()]
    else:
        df_filtrado = df_filtrado[df_filtrado['Linguas_Competencia'].isin(linguas_selecionadas)]
elif incluir_sem_lingua:
    df_filtrado = df_filtrado[df_filtrado['Linguas_Competencia'].isna()]

if cursos_ingles_selecionados:
    df_filtrado = df_filtrado[df_filtrado['Cursos_em_Ingles'].isin(cursos_ingles_selecionados)]

if auxilio_monetario_selecionado:
    df_filtrado = df_filtrado[df_filtrado['Auxilio_Monetario'].isin(auxilio_monetario_selecionado)]

if auxilio_moradia_selecionado:
    df_filtrado = df_filtrado[df_filtrado['Auxilio_Moradia'].isin(auxilio_moradia_selecionado)]

if ordenar_ranking:
    df_filtrado = df_filtrado.sort_values(by='Ranking_Internacional', ascending=True)

# Removendo as colunas selecionadas para ocultar
df_exibido = df_filtrado.drop(columns=colunas_ocultas)

# Exibir tabela filtrada (agora única e dinâmica)
st.write("### Dados Filtrados")
st.dataframe(df_exibido)

# Botão para baixar os dados filtrados
st.download_button(
    label="Baixar Dados Filtrados",
    data=df_exibido.to_csv(index=False),
    file_name="Universidades_Filtradas.csv",
    mime="text/csv"
)
