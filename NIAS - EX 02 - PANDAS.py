#NOME: Davi Caetano da Silva Junior
#DATA: 15/11/2021
#EXERCICIO PANDAS

#Importando a biblioteca pandas
import pandas as pd

####################### NÚMERO 01 ###################
covid_c = pd.read_csv('covid_19_clean_complete.csv')

# (a) Quantidades de colunas e linhas
line = len(covid_c.count(axis=1))
columns = len(covid_c.count(axis=0))

# (b) O nome das colunas:
name_columns = covid_c.columns

# (c) Tipo de dados ns colunas
covid_c.dtypes

# (d) Formato da tabela pós conversão da coluna Date para datetime64
covid_c.Date = pd.to_datetime(covid_c.Date)

# (e) Informações estatisticas sobre o banco de dados.')
covid_c.describe

# (g) A(s) coluna(s) que apresenta(m) NaN e quanto(s) valor(es) é(são)
covid_c[name_columns].isnull().sum()


########################## NÚMERO 2 ##########################
# (a) Descobrindo o nome das provincias
china_cov = covid_c.loc[covid_c[name_columns[1]] == 'China'].sort_values(by = 'Confirmed', ascending = False).drop_duplicates(subset = 'Province/State')
china_cov = china_cov.reset_index().drop(columns = ['Country/Region', 'index'])
china_cov['Province/State']

# (b) Retirando do banco de dados as infos (Optei por fazer direto nas duas primeiras linhas dessa questão)
china_cov

# (c) Tomando apenas os dados de: Active, Confirmed, Deaths e Recovered
china_cov.loc[:, ['Confirmed', 'Deaths', 'Recovered', 'Active']]

# (e) DataFrame que contém as 5 regiões com maior número de casos
china_cov.loc[:4, ['Province/State', 'Confirmed', 'Deaths', 'Recovered', 'Active']]


########################## NÚMERO 3 ########################
# (a) Juntar o nome das regiões com o nome dos países

def putting_together(covid):
    if covid.notna()['Province/State'] == True:
        covid['Country/Region'] = covid['Country/Region'] + '_' + covid['Province/State']
    return covid

# (b) Copiando o BD para um novo
covid_c_new = covid_c.copy()

# (c) Aplicando o método .apply
covid_c_new = covid_c_new.apply(putting_together, axis = 1)

# (d) Removendo a coluna Provinces/State do novo DF
covid_c_new = covid_c_new.drop(columns = ['Province/State'])


########################## NÚMERO 4 ########################
# (a) Importando o novo CSV
world_meter = pd.read_csv('worldometer_data.csv')

# (b) Tomando apenas as informações de população, país e continentes
world_meter.loc[:,['Population', 'Country/Region', 'Continent']]

# (c) Agrupando o covi_19_clean por países e por mortes (Motivo enunciado quer que eu faça mortes por milhão de hab)
covid_clean = covid_c[['Country/Region', 'Deaths']].groupby('Country/Region').sum()

# (d) Juntando os dois DF pelo país
world_m_cov_c = covid_clean.merge(world_meter.loc[:,['Country/Region', 'Population', 'Continent']], how = 'right', on = 'Country/Region')

# (e) Juntando os dois DF pelo continente
world_m_cov_c = world_m_cov_c.groupby('Continent').sum().reset_index()

# (f) Criando uma nova coluna
world_m_cov_c['Deaths/Million'] = (world_m_cov_c.Deaths/world_m_cov_c.Population)*(10**(6))

# (g) Rankeando as linhas
world_m_cov_c = world_m_cov_c.sort_values('Deaths/Million',ascending = False).reset_index().drop(columns = ['index'])
world_m_cov_c['Ranking'] = world_m_cov_c['Deaths/Million'].rank(ascending = False)
world_m_cov_c['Ranking'] = world_m_cov_c['Ranking'].astype('int64')

