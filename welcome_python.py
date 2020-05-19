# Importar biblioteca NumPy
import numpy as np
import matplotlib.pyplot as plt

# S&P 100
names = np.array(['Apple Inc', 'Abbvie Inc', 'Abbott Laboratories', 'Accenture Plc', 'Allergan Plc', 'American International Group', 'Allstate Corp', 'Amgen', 'Amazon.Com Inc.', 'American Express Company', 'Boeing Company', 'Bank of America Corp', 'Biogen Inc', 'Bank of New York Mellon Corp', 'Blackrock', 'Bristol-Myers Squibb Company', 'Berkshire Hath Hld B', 'Citigroup Inc', 'Caterpillar Inc', 'Celgene Corp', 'Charter Communicatio', 'Colgate-Palmolive Company', 'Comcast Corp A', 'Capital One Financial Corp', 'Conocophillips', 'Costco Wholesale', 'Cisco Systems Inc', 'CVS Corp', 'Chevron Corp', 'Danaher Corp', 'Walt Disney Company', 'Duke Energy Corp', 'Dowdupont Inc.', 'Emerson Electric Company', 'Exelon Corp', 'Ford Motor Company', 'Facebook Inc', 'Fedex Corp', '21st Centry Fox Class B', '21st Centry Fox Class A', 'General Dynamics Corp', 'General Electric Company', 'Gilead Sciences Inc', 'General Motors Company', 'Alphabet Class C', 'Alphabet Class A', 'Goldman Sachs Group', 'Halliburton Company', 'Home Depot', 'Honeywell International Inc', 'International Business Machines', 'Intel Corp', 'Johnson & Johnson', 'JP Morgan Chase & Co', 'Kraft Heinz Co', 'Kinder Morgan', 'Coca-Cola Company', 'Eli Lilly and Company', 'Lockheed Martin Corp', "Lowe's Companies", 'Mastercard Inc', "McDonald's Corp", 'Mondelez Intl Cmn A', 'Medtronic Inc', 'Metlife Inc', '3M Company', 'Altria Group', 'Monsanto Company', 'Merck & Company', 'Morgan Stanley', 'Microsoft Corp', 'Nextera Energy', 'Nike Inc', 'Oracle Corp', 'Occidental Petroleum Corp', 'Priceline Group', 'Pepsico Inc', 'Pfizer Inc', 'Procter & Gamble Company', 'Philip Morris International Inc', 'Paypal Holdings', 'Qualcomm Inc', 'Raytheon Company', 'Starbucks Corp', 'Schlumberger N.V.', 'Southern Company', 'Simon Property Group', 'AT&T Inc', 'Target Corp', 'Time Warner Inc', 'Texas Instruments', 'Unitedhealth Group Inc', 'Union Pacific Corp', 'United Parcel Service', 'U.S. Bancorp', 'United Technologies Corp', 'Visa Inc', 'Wells Fargo & Company', 'Wal-Mart Stores', 'Exxon Mobil Corp'])
prices = np.array([170.12, 93.29, 55.28, 145.3, 171.81, 59.5, 100.5, 168.93, 1126.82, 93.92, 265.04, 26.7, 311.92, 52.73, 474.05, 60.48, 181.27, 71.87, 137.37, 102.88, 346.2, 72.16, 36.13, 88.26, 49.89, 171.22, 36.38, 70.18, 114.84, 93.45, 103.02, 88.61, 71.12, 60.14, 41.32, 12.11, 179.14, 217.75, 30.42, 31.14, 198.7, 17.91, 71.63, 44.74, 1018.48, 1034.09, 238.05, 41.57, 170.13, 148.04, 151.4, 44.88, 138.54, 98.58, 80.59, 17.04, 45.6, 82.97, 312.93, 81.43, 149.93, 167.01, 42.49, 79.52, 51.85, 232.49, 66.51, 118.19, 53.74, 49.06, 82.49, 155.7, 59.46, 48.97, 68.17, 1762.23, 115.5, 35.38, 88.33, 103.35, 76.55, 66.83, 184.22, 56.83, 61.53, 51.12, 159.25, 34.59, 57.77, 88.62, 98.59, 209.75, 115.58, 113.2, 51.88, 117.05, 110.27, 54.02, 96.08, 80.31])
earnings = np.array([9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79, 12.58, 3.94, 5.22, 9.75, 1.75, 21.59, 3.47, 21.55, 2.96, 6.29, 5.19, 5.55, 6.4, 1.61, 2.87, 2.02, 7.58, 0.02, 5.82, 2.17, 5.71, 3.57, 3.89, 5.7, 4.45, 3.66, 2.58, 2.48, 1.68, 5.19, 11.91, 1.92, 1.92, 10.07, 1.24, 9.58, 6.19, 29.87, 29.87, 19.2, 0.73, 6.96, 6.95, 13.66, 3.18, 7.14, 6.94, 3.56, 0.65, 1.89, 4.09, 12.72, 4.34, 4.31, 6.4, 2.05, 4.69, 5.2, 8.95, 3.16, 5.53, 3.89, 3.61, 3.38, 6.67, 2.35, 2.55, 0.35, 74.45, 5.12, 2.5, 3.98, 4.49, 1.4, 3.78, 7.56, 2.07, 1.29, 2.75, 6.05, 2.93, 4.93, 6.06, 4.06, 9.6, 5.66, 5.98, 3.37, 6.62, 3.48, 4.14, 4.36, 3.56])
sectors = np.array(['Information Technology', 'Health Care', 'Health Care', 'Information Technology', 'Health Care', 'Financials', 'Financials', 'Health Care', 'Consumer Discretionary', 'Financials', 'Industrials', 'Financials', 'Health Care', 'Financials', 'Financials', 'Health Care', 'Financials', 'Financials', 'Industrials', 'Health Care', 'Consumer Discretionary', 'Consumer Staples', 'Consumer Discretionary', 'Financials', 'Energy', 'Consumer Staples', 'Information Technology', 'Consumer Staples', 'Energy', 'Health Care', 'Consumer Discretionary', 'Utilities', 'Materials', 'Industrials', 'Utilities', 'Consumer Discretionary', 'Information Technology', 'Industrials', 'Consumer Discretionary', 'Consumer Discretionary', 'Industrials', 'Industrials', 'Health Care', 'Consumer Discretionary', 'Information Technology', 'Information Technology', 'Financials', 'Energy', 'Consumer Discretionary', 'Industrials', 'Information Technology', 'Information Technology', 'Health Care', 'Financials', 'Consumer Staples', 'Energy', 'Consumer Staples', 'Health Care', 'Industrials', 'Consumer Discretionary', 'Information Technology', 'Consumer Discretionary', 'Consumer Staples', 'Health Care', 'Financials', 'Industrials', 'Consumer Staples', 'Materials', 'Health Care', 'Financials', 'Information Technology', 'Utilities', 'Consumer Discretionary', 'Information Technology', 'Energy', 'Consumer Discretionary', 'Consumer Staples', 'Health Care', 'Consumer Staples', 'Consumer Staples', 'Information Technology', 'Information Technology', 'Industrials', 'Consumer Discretionary', 'Energy', 'Utilities', 'Real Estate', 'Telecommunications', 'Consumer Discretionary', 'Consumer Discretionary', 'Information Technology', 'Health Care', 'Industrials', 'Industrials', 'Financials', 'Industrials', 'Information Technology', 'Financials', 'Consumer Staples', 'Energy'])

# Visualizar os três primeiros elementos de cada lista
print(names[:3])
print(prices[:3])
print(earnings[:3])
print(sectors[:3])


# Análise da expectativa de crescimento das empresas

# Calcular índice P/L
pe = prices/earnings

# Visualizar o índices P/L de corte das top 10 
pe_ordenado = np.sort(pe) 
top_10 = x = np.percentile(pe_ordenado, 90)
print(top_10) # Retorna: 34.13901640570927

# Criar matriz de booleanos para filtragem
boolean_array = (pe >= top_10)

# Selecionar os nomes e setores das top 10
top_nomes = names[boolean_array]
top_setores = sectors[boolean_array]

# Visualizar
print(top_nomes)
print(top_setores)

# Filtrar as empresas por setor
cd_boolean_array = (sectors == 'Consumer Discretionary') & (pe >= top_10)
en_boolean_array = (sectors == 'Energy') & (pe >= top_10)
it_boolean_array = (sectors == 'Information Technology') & (pe >= top_10)

# Selecionar os nomes das empresas
cd_nomes = names[cd_boolean_array]
en_nomes = names[en_boolean_array]
it_nomes = names[it_boolean_array]

# Selecionar os índices das empresas
cd_pe = pe[cd_boolean_array]
en_pe = pe[en_boolean_array]
it_pe = pe[it_boolean_array]

"""
# Criar gráfico de dispersão
plt.scatter(cd_nomes, cd_pe, color='red', label='CD')
plt.scatter(en_nomes, en_pe, color='green', label='EN')
plt.scatter(it_nomes, it_pe, color='blue', label='IT')

# Adicionar legendas
plt.legend()

# Adicionar títulos dos eixos
plt.xlabel('Company Name')
plt.ylabel('P/E Ratio')
plt.xticks(rotation=45)

"""

#Visualizar tendências

# Separar empresas por setor
cd_boolean_array = (sectors == 'Consumer Discretionary')
cs_boolean_array = (sectors == 'Consumer Staples')
en_boolean_array = (sectors == 'Energy')
fi_boolean_array = (sectors == 'Financials')
hc_boolean_array = (sectors == 'Health Care')
in_boolean_array = (sectors == 'Industrials')
it_boolean_array = (sectors == 'Information Technology')
mt_boolean_array = (sectors == 'Materials')
re_boolean_array = (sectors == 'Real Estate')
tc_boolean_array = (sectors == 'Telecommunications')
ut_boolean_array = (sectors == 'Utilities')

# Selecionar os índices das empresas
cd_pe = pe[cd_boolean_array]
cs_pe = pe[cs_boolean_array]
en_pe = pe[en_boolean_array]
fi_pe = pe[fi_boolean_array]
hc_pe = pe[hc_boolean_array]
in_pe = pe[in_boolean_array]
it_pe = pe[it_boolean_array]
mt_pe = pe[mt_boolean_array]
re_pe = pe[re_boolean_array]
tc_pe = pe[tc_boolean_array]
ut_pe = pe[ut_boolean_array]

# Visualizar média e desvio padrão das empresas

empresas = [cd_pe, cs_pe, en_pe, fi_pe, hc_pe, in_pe, it_pe, mt_pe, re_pe, tc_pe, ut_pe]
for empresa in empresas:
    print("")
    print(f"Empresa: {empresa}")
    print(f"Média: {np.mean(empresa)}")
    print(f"Desvio padrão: {np.std(empresa)}")
    print("")

# Plotar os histogramas 
x_multi = [cs_pe, in_pe, it_pe]
colors = ['red', 'blue', 'green']
labels = ['CS', 'IN', 'IT']
plt.hist(x_multi, 15, density=True, histtype='bar', color=colors, label=labels, alpha=0.5)

plt.legend(prop={'size': 15})
plt.xlabel('P/E ratio')
plt.ylabel('Frequency')

plt.show()

# Identificar o índice P/L em it_pe que foi > 50
outlier_price = it_pe[it_pe > 50]

# Identificar a empresa com o índice P/L > 50
it_names = names[it_boolean_array]
outlier_name = it_names[it_pe > 50]

# Mostrar resultado
print("Em 2017, o índice P/L da empresa " + str(outlier_name[0]) + " foi de " + str(round(outlier_price[0], 2)) + ".")