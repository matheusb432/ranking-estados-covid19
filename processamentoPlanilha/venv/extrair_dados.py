import openpyxl as xl


def extrair(raw_sheet, sheet_matrix):
    # Extraindo os dados relevantes da sheet principal
    row = 483
    while row < 6751:
        # 2 = B, 10 = J, 11 = K, 12 = L, 13 = M, 14 = N
        estado = raw_sheet.cell(row, 2)
        casos = raw_sheet.cell(row, 11)
        novos_casos = raw_sheet.cell(row, 12)
        obitos = raw_sheet.cell(row, 13)
        sheet_matrix.append([estado.value, casos.value, novos_casos.value, obitos.value])
        row += 241 if row != 6509 else 240
    print("Dados extraidos com sucesso!")
    # return sheet_matrix
