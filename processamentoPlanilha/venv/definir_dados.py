import openpyxl as xl


def definir(relevant_sheet, sheet_matrix):
    # Salvando os dados relevantes numa nova sheet
    # quant_uf sera 27
    quant_uf = len(sheet_matrix)
    # quant_colunas sera 4
    quant_colunas = len(sheet_matrix[0])
    # loop ira de 1 a 5
    for col in range(1, quant_colunas + 1):
        # loop ira de 2 a 28
        for row in range(2, quant_uf + 2):
            cell = relevant_sheet.cell(row, col)
            # Para acessar o indice valido da linha, é necessário usar row - 2 e col - 1
            # sheet_matrix[0 - 26][0 - 4]
            cell.value = sheet_matrix[row - 2][col - 1]
    print("Dados definidos na nova sheet com sucesso!")