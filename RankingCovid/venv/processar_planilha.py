import openpyxl as xl
from extrair_dados import extrair


def processar(filename):
    wb = xl.load_workbook(filename)
    sheet = wb['Dados Relevantes']
    sheet_matrix = extrair(sheet)
    return sheet_matrix
