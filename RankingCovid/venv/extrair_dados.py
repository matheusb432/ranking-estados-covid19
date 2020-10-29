def extrair(sheet):
    sheet_matrix = []
    for row in range(2, 29):
        estado = sheet.cell(row, 1)
        casos = sheet.cell(row, 2)
        novos_casos = sheet.cell(row, 3)
        obitos = sheet.cell(row, 4)
        sheet_matrix.append([estado.value, casos.value, novos_casos.value, obitos.value])
    print("Dados extraidos com sucesso!")
    return sheet_matrix
