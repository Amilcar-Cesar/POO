from utilitarios import(cadastrar_categoria, cadastrar_transacao,calcular_total, LISTA_TRANSACOES)



# categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_fixos = cadastrar_categoria("Gastos fixos")
categoria_viagens = cadastrar_categoria("Viagens")
categoria_lazer = cadastrar_categoria("Lazer")


#transacoes
cadastrar_transacao(
    descricao= "Salario jan/2025",
    valor=2000,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao= "serviço externo",
    valor=50,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao= "shopping",
    valor=-200,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao= "conta de luz",
    valor=-135,
    categoria=categoria_fixos
)

cadastrar_transacao(
    descricao= "Viagem França",
    valor=-500,
    categoria=categoria_viagens
)

# Loop para mostrar o extrato de transacao
print('-- Extrato de transações --')
for transacao in LISTA_TRANSACOES:
    transacao.exibir()
print('-'*60)

total = calcular_total()

print("Saldo Total: ",total)
