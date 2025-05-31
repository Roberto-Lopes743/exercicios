import pandas as pd
#reading excel file
planilha = pd.read_excel('planilha_exemplo.xlsx')

#writing excel files
print(planilha.head())
print('-=-'*30)
#what is more old?
yearOld = planilha["Idade"].shape
print(f'A pessoa mais velha tem {sorted(yearOld)[-1]} anos')