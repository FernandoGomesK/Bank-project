# C:\Users\Fernando Gomes\Desktop\Banco Beto\main.py

# Importações Absolutas a partir do nome do pacote (core, utils)
# Assumindo que Branch está em 'core/Branch.py'
from core.Bank import Bank
from core.Branch import Branch 
from utils.exceptions import InvalidBranchInstanceError # Adapte o caminho exato!

# -----------------------------------------------------------

# Exemplo de Teste:

# 1. Instanciando o Banco
banco_beto = Bank("Banco Beto", "12.345.678/0001-99", "Rua das Flores, 123", "(11) 98765-4321")

# 2. Instanciando uma Filial
filial_centro = Branch("001", "Av. Principal, 500", "(11) 3333-4444", banco_beto)

# 3. Adicionando a Filial (método testado)
banco_beto.add_branch(filial_centro)
print(f"Banco: {banco_beto._name}")
print(f"Filiais adicionadas: {[b.branch_id for b in banco_beto.show_branches()]}")