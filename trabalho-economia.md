# João Pedro Figueiredo Gomes - 29223512
## Codigo usado para o trabalho: https://github.com/nerdjp/trabalho-economia

# Sistemas de Amortização
Os sistemas de amortização neste trabalho foram calculados usando uma implementação em Python.

# Teste de funcionalidade do Sistema
## Financiamento de um imóvel
Para um imóvel foi simulado um emprestimo de 500.000 reais, com juros de 1% ao mês, por 10 anos

#### Variaveis
* Valor Financiado: 500000 reais
* Tempo de Financiamento: 10 meses
* Taxa de Financiamento: 1.0%

#### SAC - Sistema de Amortização Constante
* Total a pagar: 527500.0
* Juros a pagar: 27500.0
* Amortização a pagar: 500000

#### PRICE
* Total a pagar: 527910.38
* Juros a pagar: 27910.38
* Amortização a pagar: 500000

#### Sistema Americano
* Total a pagar: 550000.0
* Juros a pagar: 50000.0
* Amortização a pagar: 500000

#### Pagamento Único
* Total a pagar: 552256.92
* Juros a pagar: 52256.92
* Amortização a pagar: 500000

#### SAM - Sistema de Amortização Misto
* Total a pagar: 527705.19
* Juros a pagar: 27705.19
* Amortização a pagar: 500000.0

#### Sistema Alemão
* Total a pagar: 522914.51
* Juros a pagar: 27914.51
* Amortização a pagar: 500000.0

#### Pagamentos Variáveis
* Total a pagar: 549999.55
* Juros a pagar: 49999.55
* Amortização a pagar: 500000


### Menor juros: 
* SAC - Sistema de Amortização Constante: 27500.0
* PRICE: 27910.38
* Sistema Americano: 50000.0
* Pagamento Único: 52256.92
* SAM - Sistema de Amortização Misto: 27705.19
* Sistema Alemão: 27914.51
* Pagamentos Variáveis: 49999.55

O sistema com menor juros é: SAC - Sistema de Amortização Constante com 27500.0 reais de juros

### Menor prestação inicial: 
* SAC - Sistema de Amortização Constante: 55000.0
* PRICE: 52791.04
* Sistema Americano: 5000.0
* Pagamento Único: 0
* SAM - Sistema de Amortização Misto: 53895.52
* Sistema Alemão: 52291.45
* Pagamentos Variáveis: 5001.0

O sistema com menor prestacao no inico é: Pagamento Único com 0 reais no primeiro mês

### Maior Liquidez 
O investimento foi um emprestimo, usando o valor do fananciamento, com a data de recebimento a 1 ano antes do pagamento do financiamento original.

* SAC - Sistema de Amortização Constante: 183103.16
* PRICE: 182692.78
* Sistema Americano: 160603.16
* Pagamento Único: 158346.24
* SAM - Sistema de Amortização Misto: 182897.97
* Sistema Alemão: 187688.65
* Pagamentos Variáveis: 160603.61

O sistema que mais gerou lucro a partir da liquidez própria foi o: Sistema Alemão com um lucro de 187688.65 reais

### Menor saldo em 25%
* SAC - Sistema de Amortização Constante: 400000.0
* PRICE: 403940.01
* Sistema Americano: 500000
* Pagamento Único: 510050.0
* SAM - Sistema de Amortização Misto: 401970.01
* Sistema Alemão: 451748.34
* Pagamentos Variáveis: 499998

O menor saldo devedor é do sistema: SAC - Sistema de Amortização Constante com saldo devedor de 400000.0 reais

### Na perspectiva de um banco, qual sistema geraria mais lucro
* SAC - Sistema de Amortização Constante: 527500.0
* PRICE: 527910.38
* Sistema Americano: 550000.0
* Pagamento Único: 552256.92
* SAM - Sistema de Amortização Misto: 527705.19
* Sistema Alemão: 522914.51
* Pagamentos Variáveis: 549999.55

O sistema que geraria mais lucro é: Pagamento Único com um total de 552256.92 reais

### Tabelas por sistema: 

#### SAC - Sistema de Amortização Constante: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 55000.0 | 50000.0 | 5000.0 | 450000.0 |
| 2 | 54500.0 | 50000.0 | 4500.0 | 400000.0 |
| 3 | 54000.0 | 50000.0 | 4000.0 | 350000.0 |
| 4 | 53500.0 | 50000.0 | 3500.0 | 300000.0 |
| 5 | 53000.0 | 50000.0 | 3000.0 | 250000.0 |
| 6 | 52500.0 | 50000.0 | 2500.0 | 200000.0 |
| 7 | 52000.0 | 50000.0 | 2000.0 | 150000.0 |
| 8 | 51500.0 | 50000.0 | 1500.0 | 100000.0 |
| 9 | 51000.0 | 50000.0 | 1000.0 | 50000.0 |
| 10 | 50500.0 | 50000.0 | 500.0 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 527500.0 | 500000 | 27500.0 | 0 |


#### PRICE: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 52791.04 | 47791.04 | 5000.0 | 452208.96 |
| 2 | 52791.04 | 48268.95 | 4522.09 | 403940.01 |
| 3 | 52791.04 | 48751.64 | 4039.4 | 355188.37 |
| 4 | 52791.04 | 49239.15 | 3551.88 | 305949.22 |
| 5 | 52791.04 | 49731.55 | 3059.49 | 256217.67 |
| 6 | 52791.04 | 50228.86 | 2562.18 | 205988.81 |
| 7 | 52791.04 | 50731.15 | 2059.89 | 155257.66 |
| 8 | 52791.04 | 51238.46 | 1552.58 | 104019.2 |
| 9 | 52791.04 | 51750.85 | 1040.19 | 52268.35 |
| 10 | 52791.04 | 52268.35 | 522.68 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 527910.38 | 500000 | 27910.38 | 0 |


#### Sistema Americano: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 5000.0 | 0 | 5000.0 | 500000 |
| 2 | 5000.0 | 0 | 5000.0 | 500000 |
| 3 | 5000.0 | 0 | 5000.0 | 500000 |
| 4 | 5000.0 | 0 | 5000.0 | 500000 |
| 5 | 5000.0 | 0 | 5000.0 | 500000 |
| 6 | 5000.0 | 0 | 5000.0 | 500000 |
| 7 | 5000.0 | 0 | 5000.0 | 500000 |
| 8 | 5000.0 | 0 | 5000.0 | 500000 |
| 9 | 5000.0 | 0 | 5000.0 | 500000 |
| 10 | 505000.0 | 500000 | 5000.0 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 550000.0 | 500000 | 50000.0 | 0 |


#### Pagamento Único: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 0 | 0 | 5000.0 | 505000.0 |
| 2 | 0 | 0 | 5050.0 | 510050.0 |
| 3 | 0 | 0 | 5100.5 | 515150.5 |
| 4 | 0 | 0 | 5151.51 | 520302.01 |
| 5 | 0 | 0 | 5203.02 | 525505.03 |
| 6 | 0 | 0 | 5255.05 | 530760.08 |
| 7 | 0 | 0 | 5307.6 | 536067.68 |
| 8 | 0 | 0 | 5360.68 | 541428.35 |
| 9 | 0 | 0 | 5414.28 | 546842.64 |
| 10 | 552256.92 | 546842.64 | 5414.28 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 552256.92 | 500000 | 52256.92 | 0 |


#### SAM - Sistema de Amortização Misto: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 53895.52 | 48895.52 | 5000.0 | 451104.48 |
| 2 | 53645.52 | 49134.47 | 4511.04 | 401970.01 |
| 3 | 53395.52 | 49375.82 | 4019.7 | 352594.19 |
| 4 | 53145.52 | 49619.58 | 3525.94 | 302974.61 |
| 5 | 52895.52 | 49865.77 | 3029.75 | 253108.84 |
| 6 | 52645.52 | 50114.43 | 2531.09 | 202994.41 |
| 7 | 52395.52 | 50365.58 | 2029.94 | 152628.83 |
| 8 | 52145.52 | 50619.23 | 1526.29 | 102009.6 |
| 9 | 51895.52 | 50875.42 | 1020.1 | 51134.18 |
| 10 | 51645.52 | 51134.18 | 511.34 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 527705.19 | 500000.0 | 27705.19 | 0 |


#### Sistema Alemão: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 52291.45 | 47769.14 | 4522.31 | 452230.86 |
| 2 | 52291.45 | 48251.66 | 4039.79 | 451748.34 |
| 3 | 52291.45 | 48739.05 | 3552.4 | 451260.95 |
| 4 | 52291.45 | 49231.36 | 3060.09 | 450768.64 |
| 5 | 52291.45 | 49728.65 | 2562.8 | 450271.35 |
| 6 | 52291.45 | 50230.96 | 2060.49 | 449769.04 |
| 7 | 52291.45 | 50738.34 | 1553.11 | 449261.66 |
| 8 | 52291.45 | 51250.85 | 1040.6 | 448749.15 |
| 9 | 52291.45 | 51768.54 | 522.91 | 448231.46 |
| 10 | 52291.45 | 52291.45 | 0.0 | 447708.55 |
|-----|-----------|-------------|-------|---------------|
| Total | 522914.51 | 500000.0 | 27914.51 | 0 |


#### Pagamentos Variáveis: 
* Parcelas: 10

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 5001.0 | 1 | 5000.0 | 499999 |
| 2 | 5000.99 | 1 | 4999.99 | 499998 |
| 3 | 5000.98 | 1 | 4999.98 | 499997 |
| 4 | 5000.97 | 1 | 4999.97 | 499996 |
| 5 | 5000.96 | 1 | 4999.96 | 499995 |
| 6 | 5000.95 | 1 | 4999.95 | 499994 |
| 7 | 5000.94 | 1 | 4999.94 | 499993 |
| 8 | 5000.93 | 1 | 4999.93 | 499992 |
| 9 | 5000.92 | 1 | 4999.92 | 499991 |
| 10 | 504990.91 | 499991 | 4999.91 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 549999.55 | 500000 | 49999.55 | 0 |


## Financiamento de um automóvel
Para um automóvel foi simulado um emprestimo de 30.000 reais, com juros de 2% ao mês, por 24 meses

#### Variaveis
* Valor Financiado: 30000 reais
* Tempo de Financiamento: 24 meses
* Taxa de Financiamento: 2.0%

#### SAC - Sistema de Amortização Constante
* Total a pagar: 37500.0
* Juros a pagar: 7500.0
* Amortização a pagar: 30000

#### PRICE
* Total a pagar: 38067.19
* Juros a pagar: 8067.19
* Amortização a pagar: 30000

#### Sistema Americano
* Total a pagar: 44400.0
* Juros a pagar: 14400.0
* Amortização a pagar: 30000

#### Pagamento Único
* Total a pagar: 48234.57
* Juros a pagar: 18234.57
* Amortização a pagar: 30000

#### SAM - Sistema de Amortização Misto
* Total a pagar: 37783.6
* Juros a pagar: 7783.6
* Amortização a pagar: 30000.0

#### Sistema Alemão
* Total a pagar: 37478.56
* Juros a pagar: 8078.56
* Amortização a pagar: 30000.0

#### Pagamentos Variáveis
* Total a pagar: 44394.48
* Juros a pagar: 14394.48
* Amortização a pagar: 30000


### Menor juros: 
* SAC - Sistema de Amortização Constante: 7500.0
* PRICE: 8067.19
* Sistema Americano: 14400.0
* Pagamento Único: 18234.57
* SAM - Sistema de Amortização Misto: 7783.6
* Sistema Alemão: 8078.56
* Pagamentos Variáveis: 14394.48

O sistema com menor juros é: SAC - Sistema de Amortização Constante com 7500.0 reais de juros

### Menor prestação inicial: 
* SAC - Sistema de Amortização Constante: 1850.0
* PRICE: 1586.13
* Sistema Americano: 600.0
* Pagamento Único: 0
* SAM - Sistema de Amortização Misto: 1718.07
* Sistema Alemão: 1561.61
* Pagamentos Variáveis: 601.0

O sistema com menor prestacao no inico é: Pagamento Único com 0 reais no primeiro mês

### Maior Liquidez 
O investimento foi um emprestimo, usando o valor do fananciamento, com a data de recebimento a 1 mês antes do pagamento do financiamento original.

* SAC - Sistema de Amortização Constante: 54436.77
* PRICE: 53869.58
* Sistema Americano: 47536.77
* Pagamento Único: 43702.2
* SAM - Sistema de Amortização Misto: 54153.17
* Sistema Alemão: 54458.2
* Pagamentos Variáveis: 47542.29

O sistema que mais gerou lucro a partir da liquidez própria foi o: Sistema Alemão com um lucro de 54458.2 reais

### Menor saldo em 25%
* SAC - Sistema de Amortização Constante: 22500.0
* PRICE: 23779.35
* Sistema Americano: 30000
* Pagamento Único: 33784.87
* SAM - Sistema de Amortização Misto: 23139.68
* Sistema Alemão: 28914.47
* Pagamentos Variáveis: 29994

O menor saldo devedor é do sistema: SAC - Sistema de Amortização Constante com saldo devedor de 22500.0 reais

### Na perspectiva de um banco, qual sistema geraria mais lucro
* SAC - Sistema de Amortização Constante: 37500.0
* PRICE: 38067.19
* Sistema Americano: 44400.0
* Pagamento Único: 48234.57
* SAM - Sistema de Amortização Misto: 37783.6
* Sistema Alemão: 37478.56
* Pagamentos Variáveis: 44394.48

O sistema que geraria mais lucro é: Pagamento Único com um total de 48234.57 reais

### Tabelas por sistema: 

#### SAC - Sistema de Amortização Constante: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 1850.0 | 1250.0 | 600.0 | 28750.0 |
| 2 | 1825.0 | 1250.0 | 575.0 | 27500.0 |
| 3 | 1800.0 | 1250.0 | 550.0 | 26250.0 |
| 4 | 1775.0 | 1250.0 | 525.0 | 25000.0 |
| 5 | 1750.0 | 1250.0 | 500.0 | 23750.0 |
| 6 | 1725.0 | 1250.0 | 475.0 | 22500.0 |
| 7 | 1700.0 | 1250.0 | 450.0 | 21250.0 |
| 8 | 1675.0 | 1250.0 | 425.0 | 20000.0 |
| 9 | 1650.0 | 1250.0 | 400.0 | 18750.0 |
| 10 | 1625.0 | 1250.0 | 375.0 | 17500.0 |
| 11 | 1600.0 | 1250.0 | 350.0 | 16250.0 |
| 12 | 1575.0 | 1250.0 | 325.0 | 15000.0 |
| 13 | 1550.0 | 1250.0 | 300.0 | 13750.0 |
| 14 | 1525.0 | 1250.0 | 275.0 | 12500.0 |
| 15 | 1500.0 | 1250.0 | 250.0 | 11250.0 |
| 16 | 1475.0 | 1250.0 | 225.0 | 10000.0 |
| 17 | 1450.0 | 1250.0 | 200.0 | 8750.0 |
| 18 | 1425.0 | 1250.0 | 175.0 | 7500.0 |
| 19 | 1400.0 | 1250.0 | 150.0 | 6250.0 |
| 20 | 1375.0 | 1250.0 | 125.0 | 5000.0 |
| 21 | 1350.0 | 1250.0 | 100.0 | 3750.0 |
| 22 | 1325.0 | 1250.0 | 75.0 | 2500.0 |
| 23 | 1300.0 | 1250.0 | 50.0 | 1250.0 |
| 24 | 1275.0 | 1250.0 | 25.0 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 37500.0 | 30000 | 7500.0 | 0 |


#### PRICE: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 1586.13 | 986.13 | 600.0 | 29013.87 |
| 2 | 1586.13 | 1005.86 | 580.28 | 28008.01 |
| 3 | 1586.13 | 1025.97 | 560.16 | 26982.04 |
| 4 | 1586.13 | 1046.49 | 539.64 | 25935.55 |
| 5 | 1586.13 | 1067.42 | 518.71 | 24868.12 |
| 6 | 1586.13 | 1088.77 | 497.36 | 23779.35 |
| 7 | 1586.13 | 1110.55 | 475.59 | 22668.81 |
| 8 | 1586.13 | 1132.76 | 453.38 | 21536.05 |
| 9 | 1586.13 | 1155.41 | 430.72 | 20380.64 |
| 10 | 1586.13 | 1178.52 | 407.61 | 19202.12 |
| 11 | 1586.13 | 1202.09 | 384.04 | 18000.03 |
| 12 | 1586.13 | 1226.13 | 360.0 | 16773.9 |
| 13 | 1586.13 | 1250.65 | 335.48 | 15523.24 |
| 14 | 1586.13 | 1275.67 | 310.46 | 14247.57 |
| 15 | 1586.13 | 1301.18 | 284.95 | 12946.39 |
| 16 | 1586.13 | 1327.21 | 258.93 | 11619.19 |
| 17 | 1586.13 | 1353.75 | 232.38 | 10265.44 |
| 18 | 1586.13 | 1380.82 | 205.31 | 8884.61 |
| 19 | 1586.13 | 1408.44 | 177.69 | 7476.17 |
| 20 | 1586.13 | 1436.61 | 149.52 | 6039.56 |
| 21 | 1586.13 | 1465.34 | 120.79 | 4574.22 |
| 22 | 1586.13 | 1494.65 | 91.48 | 3079.57 |
| 23 | 1586.13 | 1524.54 | 61.59 | 1555.03 |
| 24 | 1586.13 | 1555.03 | 31.1 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 38067.19 | 30000 | 8067.19 | 0 |


#### Sistema Americano: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 600.0 | 0 | 600.0 | 30000 |
| 2 | 600.0 | 0 | 600.0 | 30000 |
| 3 | 600.0 | 0 | 600.0 | 30000 |
| 4 | 600.0 | 0 | 600.0 | 30000 |
| 5 | 600.0 | 0 | 600.0 | 30000 |
| 6 | 600.0 | 0 | 600.0 | 30000 |
| 7 | 600.0 | 0 | 600.0 | 30000 |
| 8 | 600.0 | 0 | 600.0 | 30000 |
| 9 | 600.0 | 0 | 600.0 | 30000 |
| 10 | 600.0 | 0 | 600.0 | 30000 |
| 11 | 600.0 | 0 | 600.0 | 30000 |
| 12 | 600.0 | 0 | 600.0 | 30000 |
| 13 | 600.0 | 0 | 600.0 | 30000 |
| 14 | 600.0 | 0 | 600.0 | 30000 |
| 15 | 600.0 | 0 | 600.0 | 30000 |
| 16 | 600.0 | 0 | 600.0 | 30000 |
| 17 | 600.0 | 0 | 600.0 | 30000 |
| 18 | 600.0 | 0 | 600.0 | 30000 |
| 19 | 600.0 | 0 | 600.0 | 30000 |
| 20 | 600.0 | 0 | 600.0 | 30000 |
| 21 | 600.0 | 0 | 600.0 | 30000 |
| 22 | 600.0 | 0 | 600.0 | 30000 |
| 23 | 600.0 | 0 | 600.0 | 30000 |
| 24 | 30600.0 | 30000 | 600.0 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 44400.0 | 30000 | 14400.0 | 0 |


#### Pagamento Único: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 0 | 0 | 600.0 | 30600.0 |
| 2 | 0 | 0 | 612.0 | 31212.0 |
| 3 | 0 | 0 | 624.24 | 31836.24 |
| 4 | 0 | 0 | 636.72 | 32472.96 |
| 5 | 0 | 0 | 649.46 | 33122.42 |
| 6 | 0 | 0 | 662.45 | 33784.87 |
| 7 | 0 | 0 | 675.7 | 34460.57 |
| 8 | 0 | 0 | 689.21 | 35149.78 |
| 9 | 0 | 0 | 703.0 | 35852.78 |
| 10 | 0 | 0 | 717.06 | 36569.83 |
| 11 | 0 | 0 | 731.4 | 37301.23 |
| 12 | 0 | 0 | 746.02 | 38047.25 |
| 13 | 0 | 0 | 760.95 | 38808.2 |
| 14 | 0 | 0 | 776.16 | 39584.36 |
| 15 | 0 | 0 | 791.69 | 40376.05 |
| 16 | 0 | 0 | 807.52 | 41183.57 |
| 17 | 0 | 0 | 823.67 | 42007.24 |
| 18 | 0 | 0 | 840.14 | 42847.39 |
| 19 | 0 | 0 | 856.95 | 43704.34 |
| 20 | 0 | 0 | 874.09 | 44578.42 |
| 21 | 0 | 0 | 891.57 | 45469.99 |
| 22 | 0 | 0 | 909.4 | 46379.39 |
| 23 | 0 | 0 | 927.59 | 47306.98 |
| 24 | 48234.57 | 47306.98 | 927.59 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 48234.57 | 30000 | 18234.57 | 0 |


#### SAM - Sistema de Amortização Misto: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 1718.07 | 1118.07 | 600.0 | 28881.93 |
| 2 | 1705.57 | 1127.93 | 577.64 | 27754.01 |
| 3 | 1693.07 | 1137.99 | 555.08 | 26616.02 |
| 4 | 1680.57 | 1148.25 | 532.32 | 25467.77 |
| 5 | 1668.07 | 1158.71 | 509.36 | 24309.06 |
| 6 | 1655.57 | 1169.39 | 486.18 | 23139.68 |
| 7 | 1643.07 | 1180.27 | 462.79 | 21959.4 |
| 8 | 1630.57 | 1191.38 | 439.19 | 20768.03 |
| 9 | 1618.07 | 1202.71 | 415.36 | 19565.32 |
| 10 | 1605.57 | 1214.26 | 391.31 | 18351.06 |
| 11 | 1593.07 | 1226.05 | 367.02 | 17125.01 |
| 12 | 1580.57 | 1238.07 | 342.5 | 15886.95 |
| 13 | 1568.07 | 1250.33 | 317.74 | 14636.62 |
| 14 | 1555.57 | 1262.83 | 292.73 | 13373.79 |
| 15 | 1543.07 | 1275.59 | 267.48 | 12098.2 |
| 16 | 1530.57 | 1288.6 | 241.96 | 10809.59 |
| 17 | 1518.07 | 1301.87 | 216.19 | 9507.72 |
| 18 | 1505.57 | 1315.41 | 190.15 | 8192.31 |
| 19 | 1493.07 | 1329.22 | 163.85 | 6863.09 |
| 20 | 1480.57 | 1343.3 | 137.26 | 5519.78 |
| 21 | 1468.07 | 1357.67 | 110.4 | 4162.11 |
| 22 | 1455.57 | 1372.32 | 83.24 | 2789.79 |
| 23 | 1443.07 | 1387.27 | 55.8 | 1402.52 |
| 24 | 1430.57 | 1402.52 | 28.05 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 37783.6 | 30000.0 | 7783.6 | 0 |


#### Sistema Alemão: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 1561.61 | 981.23 | 580.38 | 29018.77 |
| 2 | 1561.61 | 1001.26 | 560.35 | 28998.74 |
| 3 | 1561.61 | 1021.69 | 539.92 | 28978.31 |
| 4 | 1561.61 | 1042.54 | 519.07 | 28957.46 |
| 5 | 1561.61 | 1063.82 | 497.79 | 28936.18 |
| 6 | 1561.61 | 1085.53 | 476.08 | 28914.47 |
| 7 | 1561.61 | 1107.68 | 453.93 | 28892.32 |
| 8 | 1561.61 | 1130.29 | 431.32 | 28869.71 |
| 9 | 1561.61 | 1153.35 | 408.25 | 28846.65 |
| 10 | 1561.61 | 1176.89 | 384.71 | 28823.11 |
| 11 | 1561.61 | 1200.91 | 360.7 | 28799.09 |
| 12 | 1561.61 | 1225.42 | 336.19 | 28774.58 |
| 13 | 1561.61 | 1250.43 | 311.18 | 28749.57 |
| 14 | 1561.61 | 1275.95 | 285.66 | 28724.05 |
| 15 | 1561.61 | 1301.99 | 259.62 | 28698.01 |
| 16 | 1561.61 | 1328.56 | 233.05 | 28671.44 |
| 17 | 1561.61 | 1355.67 | 205.94 | 28644.33 |
| 18 | 1561.61 | 1383.34 | 178.27 | 28616.66 |
| 19 | 1561.61 | 1411.57 | 150.04 | 28588.43 |
| 20 | 1561.61 | 1440.38 | 121.23 | 28559.62 |
| 21 | 1561.61 | 1469.77 | 91.83 | 28530.23 |
| 22 | 1561.61 | 1499.77 | 61.84 | 28500.23 |
| 23 | 1561.61 | 1530.37 | 31.23 | 28469.63 |
| 24 | 1561.61 | 1561.61 | 0.0 | 28438.39 |
|-----|-----------|-------------|-------|---------------|
| Total | 37478.56 | 30000.0 | 8078.56 | 0 |


#### Pagamentos Variáveis: 
* Parcelas: 24

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 601.0 | 1 | 600.0 | 29999 |
| 2 | 600.98 | 1 | 599.98 | 29998 |
| 3 | 600.96 | 1 | 599.96 | 29997 |
| 4 | 600.94 | 1 | 599.94 | 29996 |
| 5 | 600.92 | 1 | 599.92 | 29995 |
| 6 | 600.9 | 1 | 599.9 | 29994 |
| 7 | 600.88 | 1 | 599.88 | 29993 |
| 8 | 600.86 | 1 | 599.86 | 29992 |
| 9 | 600.84 | 1 | 599.84 | 29991 |
| 10 | 600.82 | 1 | 599.82 | 29990 |
| 11 | 600.8 | 1 | 599.8 | 29989 |
| 12 | 600.78 | 1 | 599.78 | 29988 |
| 13 | 600.76 | 1 | 599.76 | 29987 |
| 14 | 600.74 | 1 | 599.74 | 29986 |
| 15 | 600.72 | 1 | 599.72 | 29985 |
| 16 | 600.7 | 1 | 599.7 | 29984 |
| 17 | 600.68 | 1 | 599.68 | 29983 |
| 18 | 600.66 | 1 | 599.66 | 29982 |
| 19 | 600.64 | 1 | 599.64 | 29981 |
| 20 | 600.62 | 1 | 599.62 | 29980 |
| 21 | 600.6 | 1 | 599.6 | 29979 |
| 22 | 600.58 | 1 | 599.58 | 29978 |
| 23 | 600.56 | 1 | 599.56 | 29977 |
| 24 | 30576.54 | 29977 | 599.54 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 44394.48 | 30000 | 14394.48 | 0 |


## Financiamento de um eletrodoméstico
Para um eletrodoméstico foi simulado um emprestimo de 3.000 reais, com juros de 3% ao mês, por 6 meses

#### Variaveis
* Valor Financiado: 3000 reais
* Tempo de Financiamento: 6 meses
* Taxa de Financiamento: 3.0%

#### SAC - Sistema de Amortização Constante
* Total a pagar: 3315.0
* Juros a pagar: 315.0
* Amortização a pagar: 3000

#### PRICE
* Total a pagar: 3322.76
* Juros a pagar: 322.76
* Amortização a pagar: 3000

#### Sistema Americano
* Total a pagar: 3540.0
* Juros a pagar: 540.0
* Amortização a pagar: 3000

#### Pagamento Único
* Total a pagar: 3579.12
* Juros a pagar: 579.12
* Amortização a pagar: 3000

#### SAM - Sistema de Amortização Misto
* Total a pagar: 3318.88
* Juros a pagar: 318.88
* Amortização a pagar: 3000.0

#### Sistema Alemão
* Total a pagar: 3232.99
* Juros a pagar: 322.99
* Amortização a pagar: 3000.0

#### Pagamentos Variáveis
* Total a pagar: 3539.55
* Juros a pagar: 539.55
* Amortização a pagar: 3000


### Menor juros: 
* SAC - Sistema de Amortização Constante: 315.0
* PRICE: 322.76
* Sistema Americano: 540.0
* Pagamento Único: 579.12
* SAM - Sistema de Amortização Misto: 318.88
* Sistema Alemão: 322.99
* Pagamentos Variáveis: 539.55

O sistema com menor juros é: SAC - Sistema de Amortização Constante com 315.0 reais de juros

### Menor prestação inicial: 
* SAC - Sistema de Amortização Constante: 590.0
* PRICE: 553.79
* Sistema Americano: 90.0
* Pagamento Único: 0
* SAM - Sistema de Amortização Misto: 571.9
* Sistema Alemão: 538.83
* Pagamentos Variáveis: 91.0

O sistema com menor prestacao no inico é: Pagamento Único com 0 reais no primeiro mês

### Maior Liquidez 
O investimento foi um emprestimo, usando o valor do fananciamento, com a data de recebimento a 1 mês antes do pagamento do financiamento original.

* SAC - Sistema de Amortização Constante: 686.81
* PRICE: 679.06
* Sistema Americano: 461.81
* Pagamento Único: 422.7
* SAM - Sistema de Amortização Misto: 682.94
* Sistema Alemão: 768.82
* Pagamentos Variáveis: 462.26

O sistema que mais gerou lucro a partir da liquidez própria foi o: Sistema Alemão com um lucro de 768.82 reais

### Menor saldo em 25%
* SAC - Sistema de Amortização Constante: 2000.0
* PRICE: 2058.5
* Sistema Americano: 3000
* Pagamento Único: 3182.7
* SAM - Sistema de Amortização Misto: 2029.25
* Sistema Alemão: 2522.98
* Pagamentos Variáveis: 2998

O menor saldo devedor é do sistema: SAC - Sistema de Amortização Constante com saldo devedor de 2000.0 reais

### Na perspectiva de um banco, qual sistema geraria mais lucro
* SAC - Sistema de Amortização Constante: 3315.0
* PRICE: 3322.76
* Sistema Americano: 3540.0
* Pagamento Único: 3579.12
* SAM - Sistema de Amortização Misto: 3318.88
* Sistema Alemão: 3232.99
* Pagamentos Variáveis: 3539.55

O sistema que geraria mais lucro é: Pagamento Único com um total de 3579.12 reais

### Tabelas por sistema: 

#### SAC - Sistema de Amortização Constante: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 590.0 | 500.0 | 90.0 | 2500.0 |
| 2 | 575.0 | 500.0 | 75.0 | 2000.0 |
| 3 | 560.0 | 500.0 | 60.0 | 1500.0 |
| 4 | 545.0 | 500.0 | 45.0 | 1000.0 |
| 5 | 530.0 | 500.0 | 30.0 | 500.0 |
| 6 | 515.0 | 500.0 | 15.0 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 3315.0 | 3000 | 315.0 | 0 |


#### PRICE: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 553.79 | 463.79 | 90.0 | 2536.21 |
| 2 | 553.79 | 477.71 | 76.09 | 2058.5 |
| 3 | 553.79 | 492.04 | 61.76 | 1566.46 |
| 4 | 553.79 | 506.8 | 46.99 | 1059.67 |
| 5 | 553.79 | 522.0 | 31.79 | 537.66 |
| 6 | 553.79 | 537.66 | 16.13 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 3322.76 | 3000 | 322.76 | 0 |


#### Sistema Americano: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 90.0 | 0 | 90.0 | 3000 |
| 2 | 90.0 | 0 | 90.0 | 3000 |
| 3 | 90.0 | 0 | 90.0 | 3000 |
| 4 | 90.0 | 0 | 90.0 | 3000 |
| 5 | 90.0 | 0 | 90.0 | 3000 |
| 6 | 3090.0 | 3000 | 90.0 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 3540.0 | 3000 | 540.0 | 0 |


#### Pagamento Único: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 0 | 0 | 90.0 | 3090.0 |
| 2 | 0 | 0 | 92.7 | 3182.7 |
| 3 | 0 | 0 | 95.48 | 3278.18 |
| 4 | 0 | 0 | 98.35 | 3376.53 |
| 5 | 0 | 0 | 101.3 | 3477.82 |
| 6 | 3579.12 | 3477.82 | 101.3 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 3579.12 | 3000 | 579.12 | 0 |


#### SAM - Sistema de Amortização Misto: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 571.9 | 481.9 | 90.0 | 2518.1 |
| 2 | 564.4 | 488.85 | 75.54 | 2029.25 |
| 3 | 556.9 | 496.02 | 60.88 | 1533.23 |
| 4 | 549.4 | 503.4 | 46.0 | 1029.83 |
| 5 | 541.9 | 511.0 | 30.89 | 518.83 |
| 6 | 534.4 | 518.83 | 15.56 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 3318.88 | 3000.0 | 318.88 | 0 |


#### Sistema Alemão: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 538.83 | 462.71 | 76.12 | 2537.29 |
| 2 | 538.83 | 477.02 | 61.81 | 2522.98 |
| 3 | 538.83 | 491.78 | 47.05 | 2508.22 |
| 4 | 538.83 | 506.99 | 31.84 | 2493.01 |
| 5 | 538.83 | 522.67 | 16.16 | 2477.33 |
| 6 | 538.83 | 538.83 | 0.0 | 2461.17 |
|-----|-----------|-------------|-------|---------------|
| Total | 3232.99 | 3000.0 | 322.99 | 0 |


#### Pagamentos Variáveis: 
* Parcelas: 6

| Mes | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 91.0 | 1 | 90.0 | 2999 |
| 2 | 90.97 | 1 | 89.97 | 2998 |
| 3 | 90.94 | 1 | 89.94 | 2997 |
| 4 | 90.91 | 1 | 89.91 | 2996 |
| 5 | 90.88 | 1 | 89.88 | 2995 |
| 6 | 3084.85 | 2995 | 89.85 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 3539.55 | 3000 | 539.55 | 0 |


## Financiamento de um Jato (Bonús para criteiro E)
Para um Jato foi simulado um emprestimo de 1.000.000 reais, com juros de 3% ao ano, por 15 anos

#### Variaveis
* Valor Financiado: 1000000 reais
* Tempo de Financiamento: 15 meses
* Taxa de Financiamento: 3.0%

#### SAC - Sistema de Amortização Constante
* Total a pagar: 1240000.0
* Juros a pagar: 240000.0
* Amortização a pagar: 1000000

#### PRICE
* Total a pagar: 1256498.71
* Juros a pagar: 256498.71
* Amortização a pagar: 1000000

#### Sistema Americano
* Total a pagar: 1450000.0
* Juros a pagar: 450000.0
* Amortização a pagar: 1000000

#### Pagamento Único
* Total a pagar: 1556645.74
* Juros a pagar: 556645.74
* Amortização a pagar: 1000000

#### SAM - Sistema de Amortização Misto
* Total a pagar: 1248249.35
* Juros a pagar: 248249.35
* Amortização a pagar: 1000000.0

#### Sistema Alemão
* Total a pagar: 1226997.84
* Juros a pagar: 256997.84
* Amortização a pagar: 1000000.0

#### Pagamentos Variáveis
* Total a pagar: 1449996.85
* Juros a pagar: 449996.85
* Amortização a pagar: 1000000


### Menor juros: 
* SAC - Sistema de Amortização Constante: 240000.0
* PRICE: 256498.71
* Sistema Americano: 450000.0
* Pagamento Único: 556645.74
* SAM - Sistema de Amortização Misto: 248249.35
* Sistema Alemão: 256997.84
* Pagamentos Variáveis: 449996.85

O sistema com menor juros é: SAC - Sistema de Amortização Constante com 240000.0 reais de juros

### Menor prestação inicial: 
* SAC - Sistema de Amortização Constante: 96666.67
* PRICE: 83766.58
* Sistema Americano: 30000.0
* Pagamento Único: 0
* SAM - Sistema de Amortização Misto: 90216.62
* Sistema Alemão: 81799.86
* Pagamentos Variáveis: 30001.0

O sistema com menor prestacao no inico é: Pagamento Único com 0 reais no primeiro mês

### Maior Liquidez 
O investimento foi um emprestimo, usando o valor do fananciamento, com a data de recebimento a 1 ano antes do pagamento do financiamento original.

* SAC - Sistema de Amortização Constante: 1013660.05
* PRICE: 997161.34
* Sistema Americano: 803660.05
* Pagamento Único: 697014.31
* SAM - Sistema de Amortização Misto: 1005410.69
* Sistema Alemão: 1026662.21
* Pagamentos Variáveis: 803663.2

O sistema que mais gerou lucro a partir da liquidez própria foi o: Sistema Alemão com um lucro de 1026662.21 reais

### Menor saldo em 25%
* SAC - Sistema de Amortização Constante: 733333.33
* PRICE: 775060.68
* Sistema Americano: 1000000
* Pagamento Único: 1125508.81
* SAM - Sistema de Amortização Misto: 754197.01
* Sistema Alemão: 941488.45
* Pagamentos Variáveis: 999996

O menor saldo devedor é do sistema: SAC - Sistema de Amortização Constante com saldo devedor de 733333.33 reais

### Na perspectiva de um banco, qual sistema geraria mais lucro
* SAC - Sistema de Amortização Constante: 1240000.0
* PRICE: 1256498.71
* Sistema Americano: 1450000.0
* Pagamento Único: 1556645.74
* SAM - Sistema de Amortização Misto: 1248249.35
* Sistema Alemão: 1226997.84
* Pagamentos Variáveis: 1449996.85

O sistema que geraria mais lucro é: Pagamento Único com um total de 1556645.74 reais

### Tabelas por sistema: 

#### SAC - Sistema de Amortização Constante: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 96666.67 | 66666.67 | 30000.0 | 933333.33 |
| 2 | 94666.67 | 66666.67 | 28000.0 | 866666.67 |
| 3 | 92666.67 | 66666.67 | 26000.0 | 800000.0 |
| 4 | 90666.67 | 66666.67 | 24000.0 | 733333.33 |
| 5 | 88666.67 | 66666.67 | 22000.0 | 666666.67 |
| 6 | 86666.67 | 66666.67 | 20000.0 | 600000.0 |
| 7 | 84666.67 | 66666.67 | 18000.0 | 533333.33 |
| 8 | 82666.67 | 66666.67 | 16000.0 | 466666.67 |
| 9 | 80666.67 | 66666.67 | 14000.0 | 400000.0 |
| 10 | 78666.67 | 66666.67 | 12000.0 | 333333.33 |
| 11 | 76666.67 | 66666.67 | 10000.0 | 266666.67 |
| 12 | 74666.67 | 66666.67 | 8000.0 | 200000.0 |
| 13 | 72666.67 | 66666.67 | 6000.0 | 133333.33 |
| 14 | 70666.67 | 66666.67 | 4000.0 | 66666.67 |
| 15 | 68666.67 | 66666.67 | 2000.0 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 1240000.0 | 1000000 | 240000.0 | 0 |


#### PRICE: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 83766.58 | 53766.58 | 30000.0 | 946233.42 |
| 2 | 83766.58 | 55379.58 | 28387.0 | 890853.84 |
| 3 | 83766.58 | 57040.97 | 26725.62 | 833812.88 |
| 4 | 83766.58 | 58752.19 | 25014.39 | 775060.68 |
| 5 | 83766.58 | 60514.76 | 23251.82 | 714545.92 |
| 6 | 83766.58 | 62330.2 | 21436.38 | 652215.72 |
| 7 | 83766.58 | 64200.11 | 19566.47 | 588015.61 |
| 8 | 83766.58 | 66126.11 | 17640.47 | 521889.5 |
| 9 | 83766.58 | 68109.9 | 15656.68 | 453779.6 |
| 10 | 83766.58 | 70153.19 | 13613.39 | 383626.41 |
| 11 | 83766.58 | 72257.79 | 11508.79 | 311368.62 |
| 12 | 83766.58 | 74425.52 | 9341.06 | 236943.1 |
| 13 | 83766.58 | 76658.29 | 7108.29 | 160284.81 |
| 14 | 83766.58 | 78958.04 | 4808.54 | 81326.78 |
| 15 | 83766.58 | 81326.78 | 2439.8 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 1256498.71 | 1000000 | 256498.71 | 0 |


#### Sistema Americano: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 30000.0 | 0 | 30000.0 | 1000000 |
| 2 | 30000.0 | 0 | 30000.0 | 1000000 |
| 3 | 30000.0 | 0 | 30000.0 | 1000000 |
| 4 | 30000.0 | 0 | 30000.0 | 1000000 |
| 5 | 30000.0 | 0 | 30000.0 | 1000000 |
| 6 | 30000.0 | 0 | 30000.0 | 1000000 |
| 7 | 30000.0 | 0 | 30000.0 | 1000000 |
| 8 | 30000.0 | 0 | 30000.0 | 1000000 |
| 9 | 30000.0 | 0 | 30000.0 | 1000000 |
| 10 | 30000.0 | 0 | 30000.0 | 1000000 |
| 11 | 30000.0 | 0 | 30000.0 | 1000000 |
| 12 | 30000.0 | 0 | 30000.0 | 1000000 |
| 13 | 30000.0 | 0 | 30000.0 | 1000000 |
| 14 | 30000.0 | 0 | 30000.0 | 1000000 |
| 15 | 1030000.0 | 1000000 | 30000.0 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 1450000.0 | 1000000 | 450000.0 | 0 |


#### Pagamento Único: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 0 | 0 | 30000.0 | 1030000.0 |
| 2 | 0 | 0 | 30900.0 | 1060900.0 |
| 3 | 0 | 0 | 31827.0 | 1092727.0 |
| 4 | 0 | 0 | 32781.81 | 1125508.81 |
| 5 | 0 | 0 | 33765.26 | 1159274.07 |
| 6 | 0 | 0 | 34778.22 | 1194052.3 |
| 7 | 0 | 0 | 35821.57 | 1229873.87 |
| 8 | 0 | 0 | 36896.22 | 1266770.08 |
| 9 | 0 | 0 | 38003.1 | 1304773.18 |
| 10 | 0 | 0 | 39143.2 | 1343916.38 |
| 11 | 0 | 0 | 40317.49 | 1384233.87 |
| 12 | 0 | 0 | 41527.02 | 1425760.89 |
| 13 | 0 | 0 | 42772.83 | 1468533.71 |
| 14 | 0 | 0 | 44056.01 | 1512589.72 |
| 15 | 1556645.74 | 1512589.72 | 44056.01 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 1556645.74 | 1000000 | 556645.74 | 0 |


#### SAM - Sistema de Amortização Misto: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 90216.62 | 60216.62 | 30000.0 | 939783.38 |
| 2 | 89216.62 | 61023.12 | 28193.5 | 878760.25 |
| 3 | 88216.62 | 61853.82 | 26362.81 | 816906.44 |
| 4 | 87216.62 | 62709.43 | 24507.19 | 754197.01 |
| 5 | 86216.62 | 63590.71 | 22625.91 | 690606.29 |
| 6 | 85216.62 | 64498.43 | 20718.19 | 626107.86 |
| 7 | 84216.62 | 65433.39 | 18783.24 | 560674.47 |
| 8 | 83216.62 | 66396.39 | 16820.23 | 494278.08 |
| 9 | 82216.62 | 67388.28 | 14828.34 | 426889.8 |
| 10 | 81216.62 | 68409.93 | 12806.69 | 358479.87 |
| 11 | 80216.62 | 69462.23 | 10754.4 | 289017.64 |
| 12 | 79216.62 | 70546.09 | 8670.53 | 218471.55 |
| 13 | 78216.62 | 71662.48 | 6554.15 | 146809.07 |
| 14 | 77216.62 | 72812.35 | 4404.27 | 73996.72 |
| 15 | 76216.62 | 73996.72 | 2219.9 | 0.0 |
|-----|-----------|-------------|-------|---------------|
| Total | 1248249.35 | 1000000.0 | 248249.35 | 0 |


#### Sistema Alemão: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 81799.86 | 53401.91 | 28397.94 | 946598.09 |
| 2 | 81799.86 | 55053.52 | 26746.34 | 944946.48 |
| 3 | 81799.86 | 56756.21 | 25043.65 | 943243.79 |
| 4 | 81799.86 | 58511.55 | 23288.3 | 941488.45 |
| 5 | 81799.86 | 60321.19 | 21478.67 | 939678.81 |
| 6 | 81799.86 | 62186.79 | 19613.06 | 937813.21 |
| 7 | 81799.86 | 64110.09 | 17689.76 | 935889.91 |
| 8 | 81799.86 | 66092.88 | 15706.98 | 933907.12 |
| 9 | 81799.86 | 68136.99 | 13662.87 | 931863.01 |
| 10 | 81799.86 | 70244.32 | 11555.54 | 929755.68 |
| 11 | 81799.86 | 72416.82 | 9383.03 | 927583.18 |
| 12 | 81799.86 | 74656.52 | 7143.34 | 925343.48 |
| 13 | 81799.86 | 76965.48 | 4834.37 | 923034.52 |
| 14 | 81799.86 | 79345.86 | 2454.0 | 920654.14 |
| 15 | 81799.86 | 81799.86 | 0.0 | 918200.14 |
|-----|-----------|-------------|-------|---------------|
| Total | 1226997.84 | 1000000.0 | 256997.84 | 0 |


#### Pagamentos Variáveis: 
* Parcelas: 15

| Ano | Prestação | Amortização | Juros | Saldo Devedor |
|-----|-----------|-------------|-------|---------------|
| 1 | 30001.0 | 1 | 30000.0 | 999999 |
| 2 | 30000.97 | 1 | 29999.97 | 999998 |
| 3 | 30000.94 | 1 | 29999.94 | 999997 |
| 4 | 30000.91 | 1 | 29999.91 | 999996 |
| 5 | 30000.88 | 1 | 29999.88 | 999995 |
| 6 | 30000.85 | 1 | 29999.85 | 999994 |
| 7 | 30000.82 | 1 | 29999.82 | 999993 |
| 8 | 30000.79 | 1 | 29999.79 | 999992 |
| 9 | 30000.76 | 1 | 29999.76 | 999991 |
| 10 | 30000.73 | 1 | 29999.73 | 999990 |
| 11 | 30000.7 | 1 | 29999.7 | 999989 |
| 12 | 30000.67 | 1 | 29999.67 | 999988 |
| 13 | 30000.64 | 1 | 29999.64 | 999987 |
| 14 | 30000.61 | 1 | 29999.61 | 999986 |
| 15 | 1029985.58 | 999986 | 29999.58 | 0 |
|-----|-----------|-------------|-------|---------------|
| Total | 1449996.85 | 1000000 | 449996.85 | 0 |


