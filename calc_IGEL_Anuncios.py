print("-" * 20)
print(" IGEL DISTRIBUIDORA")
print("-" * 20)

#5 reais serão do custo fixo do ML
#45% é a margem de lucro ideal
#11% é a tributação por venda
#18% é a tarifa do ML
#15% é o custo fixo da IGEL, cálculo feito com base no ticket médio e total de vendas por mês

#Cálculo Markup:
    #Markup = 100/100 - (Despesas fixas + Despesas variáveis + Margem de lucro)


while True:
    custo_peca=float(input("Qual o custo da peça?\n"))

    #Markup com base nas tarifas do ML
    markup_ML_nf = 100/(100-(15+29+10))

    preco_venda_ML_nf = markup_ML_nf * custo_peca

    #Markup com base nas tarifas do ML(S/ nota fiscal)

    markup_ML = 100/(100-(15+18+10))
    preco_venda_ML = markup_ML * custo_peca

    #Markup com base nas tarifas do shopee:
    markup_Shopee = 100/(100-(15+12+10))
    preco_venda_Shopee = markup_Shopee * custo_peca

    #Markup com base nas tarifas do site:
    markup_site = 100/(100-(15+16+10))
    preco_venda_site = markup_site * custo_peca

    #Preço de venda ML com nota fiscal:
    if preco_venda_ML_nf >= 79:
        preco_venda_ML_nf = preco_venda_ML_nf + 20
        print("O preço de venda no ML(C/ NF) será: " + str("%.2f" % preco_venda_ML_nf))
    else:
        preco_venda_ML_nf = preco_venda_ML_nf + 5
        print("O preço de venda será no ML(C/ NF) será: " + str("%.2f" % preco_venda_ML_nf))
    #Preço de venda ML sem nota fiscal:
    if preco_venda_ML >= 79:
        preco_venda_ML = preco_venda_ML + 20
        print("O preço de venda no ML(S/ NF) será: " + str("%.2f" % preco_venda_ML))
    else:
        preco_venda_ML = preco_venda_ML + 5
        print("O preço de venda será no ML(S/ NF) será: " + str("%.2f" % preco_venda_ML))
    #Preço de venda Shopee sem nota:    
    print("O preço de venda no Shopee (S/ NF) será: " + str("%.2f" % preco_venda_Shopee))
    #Preço de venda site com nota:
    print("O preço de venda no site (C/ NF) será: " + str("%.2f" % preco_venda_site))
        
    yn = input('Aperte "ENTER" para calcular mais um custo ou digite "n" para sair\n')
    if yn == "y":
        continue
    elif yn == "n":
        break