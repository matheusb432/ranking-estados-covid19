import openpyxl as xl
from extrair_dados import extrair
from definir_dados import definir

def processar(filename):
    wb = xl.load_workbook(filename)
    raw_sheet = wb['Covid Dados']
    relevant_sheet = wb['Dados Relevantes']
    sheet_matrix = []
    extrair(raw_sheet, sheet_matrix) # extraindo os dados para a matriz

    definir(relevant_sheet, sheet_matrix) # definido os dados na nova sheet

    # Apagando a sheet original e salvando o arquivo apenas com a nova sheet
    wb.remove(raw_sheet)
    print("Sheet original apagada com sucesso!")

    wb.save('dados_relevantes.xlsx')
    print("Arquivo gravado com sucesso!")


#process_workbook('covid_painel.xlsx')