'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.

'''

listaCarro = []
listaConsumo = []

while len(listaCarro) < 5:
    listaCarro.append(input('Digite o nome do carro: '))
    listaConsumo.append(float(input('Digite o consumo do carro (km por litro): ')))
    print('novos dados inseridos\n')

results = ''
valor_gas = 4.55
total_km = 1000
for j, c in enumerate(listaCarro):
    print('Veiculo {}'.format(j+1))
    print('Nome: {}'.format(c))
    print('Km por litro: {}\n'.format(listaConsumo[j]))

    consumo_l = round(total_km/listaConsumo[j], 2)
    results += 'O carro {} consume {}L e custará $R{} quando fizer {}km\n'.format(c, consumo_l, round(consumo_l*valor_gas, 2), total_km)

print('O carro mais económico é o {}'.format(listaCarro[listaConsumo.index(max(listaConsumo))])) # descobrir na listaCarro o carro cujo o indice e o mesmo do que o indice do maior valor na listaConsumo
print(results)