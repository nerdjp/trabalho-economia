from collections import defaultdict
def rec_dd(): 
    return defaultdict(rec_dd)

class Tabela:
    def __init__(self, name) -> None:
        self.name = name
        self.parcelas: int = 0
        self.prestacao = rec_dd()
        self.amorizacao = rec_dd()
        self.juros = rec_dd()
        self.saldo_devedor = rec_dd()
        self.prestacao_final: float = 0
        self.amorizacao_final: float = 0
        self.juros_final: float = 0


    def print(self, ano):
        print()
        print("#### " + self.name + ": ")
        print("* Parcelas: " + str(round(self.parcelas, 2)))
        print()
        if ano:
            print("| Ano | Prestação | Amortização | Juros | Saldo Devedor |")
        else:
            print("| Mes | Prestação | Amortização | Juros | Saldo Devedor |")
        print("|-----|-----------|-------------|-------|---------------|")
        for i in range(1, self.parcelas + 1):
            print("| " + str(i) + " | " + str(round(self.prestacao[i], 2)) + " | " + str(round(self.amorizacao[i], 2)) + " | " + str(round(self.juros[i], 2)) + " | " + str(round(self.saldo_devedor[i], 2)) + " |")
        print("|-----|-----------|-------------|-------|---------------|")
        print("| Total | " + str(round(self.prestacao_final, 2)) + " | " + str(round(self.amorizacao_final, 2)) + " | " + str(round(self.juros_final, 2)) + " | " + str(0) + " |")
        print()

class MetaTabela:
    def __init__(self, emprestimo: float, taxa: float, parcela: int, ano: bool) -> None:
        self.sistemas: list[Tabela] = []
        self.emprestimo: float = 0
        self.taxa: float = 0
        self.parcela: int = 0
        self.ano: bool = ano

        self.emprestimo = emprestimo
        self.taxa = taxa
        self.parcela = parcela
        self.sistemas.append(sac(emprestimo, taxa, parcela))
        self.sistemas.append(price(emprestimo, taxa, parcela))
        self.sistemas.append(americano(emprestimo, taxa, parcela))
        self.sistemas.append(pag_unico(emprestimo, taxa, parcela))
        self.sistemas.append(sam(emprestimo, taxa, parcela))
        self.sistemas.append(alemao(emprestimo, taxa, parcela))
        self.sistemas.append(variaveis(emprestimo, taxa, parcela))

    def menos_juros(self):
        nome: str = self.sistemas[0].name
        menor_juros_pagos: float = self.sistemas[0].juros_final
        print("### Menor juros: ")
        for sistema in self.sistemas:
            print("* " + sistema.name + ": " + str(round(sistema.juros_final, 2)))
            if sistema.juros_final < menor_juros_pagos:
                nome = sistema.name
                menor_juros_pagos = sistema.juros_final

        print()
        print("O sistema com menor juros é: " + nome + " com " + str(round(menor_juros_pagos, 2)) + " reais de juros")

    def menor_prestacao(self):
        nome: str = self.sistemas[0].name
        prestacao: float = self.sistemas[0].prestacao[1]
        print("### Menor prestação inicial: ")
        for sistema in self.sistemas:
            print("* " + sistema.name + ": " + str(round(sistema.prestacao[1], 2)))
            if sistema.prestacao[1] < prestacao:
                nome = sistema.name
                prestacao = sistema.prestacao[1]
        print()
        print("O sistema com menor prestacao no inico é: " + nome + " com " + str(round(prestacao, 2)) + " reais no primeiro mês")

    def familiar_amorozo(self):
        nome: str = self.sistemas[0].name
        tempo: int = round(self.parcela / 4)
        menor_saldo_devedor: float = self.sistemas[0].saldo_devedor[tempo]
        print("### Menor saldo em 25%")
        for sistema in self.sistemas:
            print("* " + sistema.name + ": " + str(round(sistema.saldo_devedor[tempo], 2)))
            if sistema.saldo_devedor[tempo] < menor_saldo_devedor:
                nome = sistema.name
                menor_saldo_devedor = sistema.saldo_devedor[tempo]
        print()
        print("O menor saldo devedor é do sistema: " + nome + " com saldo devedor de " + str(round(menor_saldo_devedor, 2)) + " reais")

    ## Decisao extra: caso a pessoa esteja a emprestar dinheiro, e quer saber qual o sistema que ira gerar mais lucro
    def lucro(self, p: bool) -> float:
        nome: str = self.sistemas[0].name
        lucro: float = self.sistemas[0].prestacao_final
        if p:
            print("### Na perspectiva de um banco, qual sistema geraria mais lucro")
        for sistema in self.sistemas:
            if p:
                print("* " + sistema.name + ": " + str(round(sistema.prestacao_final, 2)))
            if sistema.prestacao_final > lucro:
                nome = sistema.name
                lucro = sistema.prestacao_final

        if p:
            print()
            print("O sistema que geraria mais lucro é: " + nome + " com um total de " + str(round(lucro, 2)) + " reais")
        return lucro

    def maior_liquidez(self):
        nome: str = self.sistemas[0].name
        tbl = MetaTabela(self.emprestimo, self.taxa + 0.03, self.parcela - 1, self.ano)
        lucro = tbl.lucro(False)
        diff = 0
        mesano = ""
        if self.ano:
            mesano = "ano"
        else:
            mesano = "mês"
        print("### Maior Liquidez ")
        print("O investimento foi um emprestimo, usando o valor do fananciamento, com a data de recebimento a 1 " + mesano + " antes do pagamento do financiamento original.")
        print()
        for sistema in self.sistemas:
            print("* " + sistema.name + ": " + str(round(lucro - sistema.prestacao_final, 2)))
            if lucro - sistema.prestacao_final > diff:
                nome = sistema.name
                diff = lucro - sistema.prestacao_final
        print()
        print("O sistema que mais gerou lucro a partir da liquidez própria foi o: " + nome + " com um lucro de " + str(round(diff, 2)) + " reais")

    def print_variaveis(self):
        print("#### Variaveis")
        print("* Valor Financiado: " + str(round(self.emprestimo, 2)) + " reais")
        print("* Tempo de Financiamento: " + str(round(self.parcela, 2)) + " meses")
        print("* Taxa de Financiamento: " + str(round(self.taxa * 100, 2)) + "%")
        print()

        for sistema in self.sistemas:
            print("#### " + sistema.name)
            print("* Total a pagar: " + str(round(sistema.prestacao_final, 2)))
            print("* Juros a pagar: " + str(round(sistema.juros_final, 2)))
            print("* Amortização a pagar: " + str(round(sistema.amorizacao_final, 2)))
            print()

    def print_all(self):
        for sistema in self.sistemas:
            sistema.print(self.ano)

        
def sac(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl = Tabela("SAC - Sistema de Amortização Constante")
    saldo_devedor = emprestimo
    amortizacao_fixa = saldo_devedor / parcelas
    juros_totais = 0
    prestacao_total = 0
    tbl.parcelas = parcelas
    for i in range(1, parcelas + 1):
        juros = saldo_devedor * taxa
        prestacao = amortizacao_fixa + juros

        saldo_devedor -= amortizacao_fixa

        tbl.saldo_devedor[i] = saldo_devedor
        tbl.amorizacao[i] = amortizacao_fixa
        tbl.juros[i] = juros
        tbl.prestacao[i] = prestacao
        
        juros_totais += juros
        prestacao_total += prestacao
        
    tbl.prestacao_final = emprestimo + juros_totais
    tbl.juros_final = juros_totais
    tbl.amorizacao_final = emprestimo
    return tbl

def price(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl = Tabela("PRICE")
    saldo_devedor = emprestimo
    taxa_p = (1 + taxa) ** parcelas
    valor_prestacao = emprestimo * ((taxa_p * taxa) / (taxa_p - 1))
    tbl.parcelas = parcelas

    juros_totais = 0
    prestacao_total = 0

    for i in range(1, parcelas + 1):
        juros = saldo_devedor * taxa
        amortizacao = valor_prestacao - juros
        saldo_devedor -= amortizacao
        if saldo_devedor < 0:
            saldo_devedor = 0

        prestacao_total += valor_prestacao
        tbl.prestacao[i] = valor_prestacao
        juros_totais += juros
        tbl.juros[i] = juros
        tbl.amorizacao[i] = amortizacao
        tbl.saldo_devedor[i] = saldo_devedor
        
    tbl.prestacao_final = emprestimo + juros_totais
    tbl.juros_final = juros_totais
    tbl.amorizacao_final = emprestimo

    return tbl

def americano(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl = Tabela("Sistema Americano")
    tbl.parcelas = parcelas
    saldo_devedor = emprestimo
    juros = emprestimo * taxa
    juros_final = 0
    prestacao_final = 0
    for i in range(1, parcelas):
        juros_final += juros
        prestacao_final += juros
        tbl.saldo_devedor[i] = saldo_devedor
        tbl.juros[i] = juros
        tbl.prestacao[i] = juros
        tbl.amorizacao[i] = 0

    prestacao_final += saldo_devedor + juros
    juros_final += juros
    tbl.amorizacao[parcelas] = saldo_devedor
    tbl.saldo_devedor[parcelas] = 0
    tbl.prestacao[parcelas] = saldo_devedor + juros
    tbl.juros[parcelas] = juros

    tbl.prestacao_final = emprestimo + juros_final
    tbl.juros_final = juros_final
    tbl.amorizacao_final = emprestimo

    return tbl

#FIXME: amortização quebrada
def pag_unico(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl = Tabela("Pagamento Único")
    tbl.parcelas = parcelas
    juros_final = 0
    amortizacao_final = 0
    parcela_final = 0
    juros = 0
    saldo_devedor = emprestimo

    for i in range(1, parcelas):
        juros = saldo_devedor * taxa
        saldo_devedor += juros
        tbl.prestacao[i] = 0
        tbl.amorizacao[i] = 0
        tbl.juros[i] = juros
        tbl.saldo_devedor[i] = saldo_devedor
        juros_final += juros

    tbl.amorizacao[parcelas] = saldo_devedor
    tbl.prestacao[parcelas] = saldo_devedor + juros
    tbl.saldo_devedor[parcelas] = 0
    tbl.juros[parcelas] = juros
    juros_final += juros
    tbl.juros_final = juros_final
    tbl.amorizacao_final = emprestimo
    tbl.prestacao_final = saldo_devedor + juros
    
    return tbl
    

def sam(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl_sac = sac(emprestimo, taxa, parcelas)
    tbl_price = price(emprestimo, taxa, parcelas)
    tbl = Tabela("SAM - Sistema de Amortização Misto")
    tbl.parcelas = parcelas

    for i in range(1, parcelas + 1):
        tbl.prestacao[i] = (tbl_price.prestacao[i] + tbl_sac.prestacao[i]) / 2
        tbl.amorizacao[i] = (tbl_price.amorizacao[i] + tbl_sac.amorizacao[i]) / 2
        tbl.juros[i] = (tbl_price.juros[i] + tbl_sac.juros[i]) / 2
        tbl.saldo_devedor[i] = (tbl_price.saldo_devedor[i] + tbl_sac.saldo_devedor[i]) / 2
        
    tbl.prestacao_final = (tbl_price.prestacao_final + tbl_sac.prestacao_final) / 2
    tbl.amorizacao_final = (tbl_price.amorizacao_final + tbl_sac.amorizacao_final) / 2
    tbl.juros_final = (tbl_price.juros_final + tbl_sac.juros_final) / 2
    return tbl

def alemao(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl = Tabela("Sistema Alemão")
    tbl.parcelas = parcelas
    saldo_devedor = emprestimo
    prestacao = saldo_devedor * taxa / (1 - (1 - taxa) ** parcelas)

    primeira_amortizacao = prestacao * ((1 - taxa) ** (parcelas - 1))

    for i in range(1, parcelas + 1):
        tbl.prestacao_final += prestacao
        tbl.prestacao[i] = prestacao
        amortizacao = primeira_amortizacao / ((1 - taxa) ** (i - 1))
        tbl.amorizacao[i] = amortizacao
        tbl.amorizacao_final += amortizacao
        juros = prestacao - amortizacao
        tbl.juros[i] = juros
        tbl.juros_final += juros
        tbl.saldo_devedor[i] = saldo_devedor - amortizacao
    tbl.juros_final += emprestimo * taxa

    return tbl

def variaveis(emprestimo: float, taxa: float, parcelas: int) -> Tabela:
    tbl = Tabela("Pagamentos Variáveis")
    tbl.parcelas = parcelas
    saldo_devedor = emprestimo
    am = 0
    for i in range(1, parcelas):
        if saldo_devedor > 100000:
            am = 100000
        if saldo_devedor > 50000:
            am = 50000
        if saldo_devedor > 1000:
            am = 1000
        if saldo_devedor > 500:
            am = 500
        if saldo_devedor > 1:
            am = 1
        juros = saldo_devedor * taxa
        saldo_devedor -= am
        tbl.amorizacao[i] = am
        tbl.juros[i] = juros
        tbl.prestacao[i] = am + juros
        tbl.saldo_devedor[i] = saldo_devedor
        tbl.amorizacao_final += am
        tbl.juros_final += juros
        tbl.prestacao_final += am + juros
    if saldo_devedor != 0:
        am = saldo_devedor
        juros = saldo_devedor * taxa
        saldo_devedor -= am
        tbl.amorizacao[parcelas] = am
        tbl.juros[parcelas] = juros
        tbl.prestacao[parcelas] = am + juros
        tbl.saldo_devedor[parcelas] = saldo_devedor
        tbl.amorizacao_final += am
        tbl.juros_final += juros
        tbl.prestacao_final += am + juros
    
    return tbl

def main():
    #price(30000, 0.015, 12).print()
    #americano(50000, 0.03, 10).print()
    #pag_unico(100000, 0.01, 3).print()
    #sam(100000, 0.01, 100).print()
    #alemao(300000, 0.04, 5).print()

    print("# João Pedro Figueiredo Gomes - 29223512")
    print("## Codigo usado para o trabalho: https://github.com/nerdjp/trabalho-economia")
    print()
    print("# Sistemas de Amortização")
    print("Os sistemas de amortização neste trabalho foram calculados usando uma implementação em Python.")
    print()

    print("# Teste de funcionalidade do Sistema")
    print("## Financiamento de um imóvel")
    print("Para um imóvel foi simulado um emprestimo de 500.000 reais, com juros de 1% ao mês, por 10 anos")
    print()

    imovel = MetaTabela(500000, 0.01, 10, True)
    imovel.print_variaveis()
    print()
    imovel.menos_juros()
    print()
    imovel.menor_prestacao()
    print()
    imovel.maior_liquidez()
    print()
    imovel.familiar_amorozo()
    print()
    imovel.lucro(True)
    print()
    print("### Tabelas por sistema: ")
    imovel.print_all()
    print()

    print("## Financiamento de um automóvel")
    print("Para um automóvel foi simulado um emprestimo de 30.000 reais, com juros de 2% ao mês, por 24 meses")
    print()

    automovel = MetaTabela(30000, 0.02, 24, False)
    automovel.print_variaveis()
    print()
    automovel.menos_juros()
    print()
    automovel.menor_prestacao()
    print()
    automovel.maior_liquidez()
    print()
    automovel.familiar_amorozo()
    print()
    automovel.lucro(True)
    print()
    print("### Tabelas por sistema: ")
    imovel.print_all()
    print()

    print("## Financiamento de um eletrodoméstico")
    print("Para um eletrodoméstico foi simulado um emprestimo de 3.000 reais, com juros de 3% ao mês, por 6 meses")
    print()

    eletrodomestico = MetaTabela(3000, 0.03, 6, False)
    eletrodomestico.print_variaveis()
    print()
    eletrodomestico.menos_juros()
    print()
    eletrodomestico.menor_prestacao()
    print()
    eletrodomestico.maior_liquidez()
    print()
    eletrodomestico.familiar_amorozo()
    print()
    eletrodomestico.lucro(True)
    print()
    print("### Tabelas por sistema: ")
    imovel.print_all()
    print()

    print("## Financiamento de um Jato (Bonús para criteiro E)")
    print("Para um Jato foi simulado um emprestimo de 1.000.000 reais, com juros de 3% ao ano, por 15 anos")
    print()

    jato = MetaTabela(1000000, 0.03, 15, True)
    jato.print_variaveis()
    print()
    jato.menos_juros()
    print()
    jato.menor_prestacao()
    print()
    jato.maior_liquidez()
    print()
    jato.familiar_amorozo()
    print()
    jato.lucro(True)
    print()
    print("### Tabelas por sistema: ")
    imovel.print_all()
    print()


if __name__ == "__main__":
    main()
