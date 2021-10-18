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

    #Markup para produtos pagos a vista:
    markup_avis = 100/(100-(15+0+10))
    preco_venda_avis = markup_avis * custo_peca

    #Markup para produtos pagos no débito:
    markup_debito = 100/(100-(15+2+10))
    preco_venda_deb = markup_debito * custo_peca

    #Markup para produtos pagos no crédito a vista na máquininha do MP:
    markup_avis_cred = 100/(100-(15+5+10))
    preco_venda_avis_cred = markup_avis_cred * custo_peca

    #Markup para produtos pagos no crédito a vista na máquininha da rede:
    markup_avis_cred_rede = 100/(100-(15+3.78+10))
    preco_venda_avis_cred_rede = markup_avis_cred_rede * custo_peca

    #Markup para produtos parcelados pela maquininha do MP:
    markup_parc_MP = 100/(100-(15+11.29+10))
    preco_venda_parc_MP = markup_parc_MP * custo_peca

    #Markup para produtos parcelados pela rede:
    markup_parc_rede = 100/(100-(15+6.59+10))
    preco_venda_parc_rede = markup_parc_rede * custo_peca

    
    #Preço de venda Shopee sem nota:    
    print("O preço mínimo de venda a vista será: " + str("%.2f" %preco_venda_avis ))
    print("O preço mínimo de venda no débito será: " + str("%.2f" %preco_venda_deb ))
    print("O preço mínimo de venda crédito a vista(MP) será: " + str("%.2f" %preco_venda_avis_cred))
    print("O preço mínimo de venda crédito a vista(rede) será: " + str("%.2f" %preco_venda_avis_cred_rede ))
    print("O preço mínimo de venda parcelado(MP) será: " + str("%.2f" %preco_venda_parc_MP ))
    print("O preço mínimo de venda parcelado(rede) será: " + str("%.2f" %preco_venda_parc_rede ))
    

    
        
    yn = input('Aperte "ENTER" para calcular mais um custo ou digite "n" para sair\n')
    if yn == "y":
        continue
    elif yn == "n":
        break