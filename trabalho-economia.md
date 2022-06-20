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


