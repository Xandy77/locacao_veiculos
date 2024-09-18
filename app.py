from modulo import *

if __name__ == "__main__":
    # Cadastrando veículos
    veiculo1 = Veiculo('Fusca', 'Volkswagen', 1975, 50.00)
    veiculo2 = Veiculo('Civic', 'Honda', 2020, 150.00)
    veiculo3 = Veiculo('Corolla', 'Toyota', 2021, 120.00)
    veiculo4 = Veiculo('Onix', 'Chevrolet', 2019, 80.00)
    veiculo5 = Veiculo('Forte', 'Hyundai', 2022, 130.00)

    veiculos = [veiculo1, veiculo2, veiculo3, veiculo4, veiculo5]

    # Cadastro de usuário
    nome = input('Informe o nome do usuário: ')
    documento = input('Informe o documento do usuário: ')
    usuario = Usuario(nome, documento)

    # Exibindo veículos disponíveis
    print("\nVeículos disponíveis:")
    for i, veiculo in enumerate(veiculos, start=1):
        print(f'{i}. {veiculo.exibir_informacoes()}')

    # Escolha do veículo
    escolha = int(input('Escolha o número do veículo que deseja alugar: '))
    if 1 <= escolha <= len(veiculos):
        usuario.alugar_veiculo(veiculos[escolha - 1])
    else:
        print("Escolha inválida.")

    # Saída de dados
    print("\nDados do cliente e veículo alugado:")
    print(usuario.exibir_dados())