# %%
#NOME: Davi Caetano da Silva Junior
#DATA: 22/11/2021
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.palettes import color_palette
from seaborn.rcmod import plotting_context

covid_c = pd.read_csv('covid_19_clean_complete.csv')

#PARA A ATIVIDADE DE LINE CHARTS, IREMOS LIMPAR O BD PARA O QUE PRECISAMOS, APÓS IREMOS PLOTAR O GRÁFICO
covid_c = covid_c.loc[(covid_c['WHO Region'] == 'Europe') | (covid_c['WHO Region'] == 'Eastern Mediterranean') | (covid_c['WHO Region'] == 'Americas')]
covid_c = covid_c.loc[:,['Date', 'WHO Region', 'Deaths']].groupby(['Date', 'WHO Region']).sum().reset_index(level='Date')

#FAZENDO CONFIGURAÇÕES EM RELAÇÃO AO GRÁFICO A SER PLOTADO
sns.set_style('dark')
sns.set(font_scale=5)
plt.figure(figsize=(180,40))
plt.xticks(rotation=90)
px = plt.subplot()
plt.grid(visible=True, axis='both', color='black', linestyle='-', linewidth = 2)

#ADICIONANDO AS LEGENDAS E AS INFORMAÇÕES ADICIONAIS
plt.legend()
plt.title('RELAÇÃO ENTRE MORTE X DIA', fontweight='bold', fontsize=150)
plt.ylabel('Mortes', fontweight='bold', fontsize=100)
plt.xlabel('Dias', fontweight = 'bold', fontsize=100)

#PLOTANDO O GRÁFICO
px.plot('Date', 'Deaths', label='Europa', linewidth = 7, color = 'black', data=covid_c.loc[(covid_c.index == 'Europe')])
px.plot('Date', 'Deaths', label = 'Mediterrâneo', linewidth = 7, color = 'red', data=covid_c.loc[(covid_c.index == 'Eastern Mediterranean')])
px.plot('Date', 'Deaths', label= 'Américas', linewidth = 7, color = 'blue', data=covid_c.loc[(covid_c.index == 'Americas')])

#RESPONDENDO AS PEGUNTAS FEITAS NO EXERCICIO:
#(A) A região que mais teve mortes foi a região das Américas
#(B) O momento em que a progressão na Europa começou  a subir foi entre os dias 11 e 12/03/2020 e nas Américas foram entre 22-23/03/2020.
# Já no Mediterrâneo tivemos uma subida mais leve entre os periodos dos meses 3 e 4.
#(C) A taxa de crescimento na Europa e nas Américas são crescentes, no Mediterrâneo há um crescimento, mas ainda pequeno comparado com os demais



#PARA A ATIVIDADE DE BAR CHARTS
#COMO ESTOU EM UM SCRIPT NOVO OPTEI POR SALVAR UM CSV DO EXERCICIO 4 DA ATIVIDADE DO PANDAS
#SENDO ASSIM IREI CARREGAR ELE AQUI
covid_ranking = pd.read_csv('covid_19_clean_EX4_pandas.csv')

#FAZENDO AS CONFIGURAÇÕES PARA PLOTAR
sns.set(font_scale=10)
plt.figure(figsize=(100,60))
plt.ticklabel_format(style='plain', axis='y')

#PLOTANDO O GRÁFICO
sns.barplot(data=covid_ranking, x= 'Continent',y='Deaths')

#SETAR OS VALORES DOS AXIS E O TITULO
plt.title('RELAÇÃO DE MORTE X CONTINENTE', fontweight='bold', fontsize=150)
plt.xlabel('Continentes', fontweight='bold', fontsize=100)
plt.ylabel('Mortes', fontweight='bold', fontsize=100)

#RESPONDENDO AS PERGUNTAS FEITAS NO EXERCICIO:
#(A) Os dois continentes com maior número de mortes são: Europa e America do Sul
#(B) O menor continente com número de mortes é Austrália e Oceania
#(C) A analise de como se lidou com a pandemia no inicio dela ainda, além do sistema de saúde ser de alta qualidade.



#PARA A ATIVIDADE DE SCATTER PLOT
world_m = pd.read_csv('worldometer_data.csv')
world_m = world_m.loc[:,['Continent', 'Deaths/1M pop']].groupby('Continent').mean().sort_values(by=['Deaths/1M pop'], ascending=False)
world_m = world_m.iloc[0:3]

#CONFIGURANDO O VISUAL DO GRÁFICO A SER PLOTADO
sns.set_style('whitegrid')
plt.figure(figsize=(100,20))

#SETAR OS VALORES DOS AXIS E O TITULO
plt.title('RELAÇÃO DE MORTES POR MILHÃO X CONTINENTE', fontweight='bold', fontsize=150)
plt.ylabel('Continentes', fontweight='bold', fontsize=100)
plt.xlabel('Mortes por Milhão', fontweight='bold', fontsize=100)

#PLOTANDO O GRÁFICO
sns.scatterplot(x='Deaths/1M pop', y='Continent', hue='Continent', data=world_m, s=2300)

#RESPONDENDO AS PERGUNTAS RELATIVAS AO SCATTERPLOT:
#(A) Acima da média de 200 mortes por milhão com a Europa e América do Sul
#(B) Que apesar de que a Europa possuí um territorio pequeno em relação com os outros 2, temos uma população
#maior que a que se encontra em primeiro lugar.
#(C) Que em determinados locais mesmo com suas áreas menores possuem uma maior quantidade de pessoas



#FAZENDO A ATIVIDADE DO HEATMAP
world_m_corr = pd.read_csv('worldometer_data.csv').corr()

#SETANDO INFORMAÇÕES PARA O GRÁFICO
plt.figure(figsize=(100,50))
plt.title('HEATMAP: DADOS MUNDIAIS', fontweight='bold', fontsize=150)

#HEATMAP COMPLETO
sns.heatmap(data=world_m_corr,annot=True)

#HEATMAP COM DUAS COLUNAS APENAS
plt.figure(figsize=(100,50))
plt.title('HEATMAP: DUAS COLUNAS', fontweight='bold', fontsize=150)
sns.heatmap(data=world_m_corr.loc[:,['Population', 'Deaths/1M pop']],annot=True)
# %%