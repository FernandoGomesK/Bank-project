
#testing the bank

from core.Bank import Bank
from core.Branch import Branch 
from utils.exceptions import InvalidBranchInstanceError 


banco_beto = Bank("Banco Beto", "12.345.678/0001-99", "Rua das Flores, 123", "(11) 98765-4321")


filial_centro = Branch("001", "Av. Principal, 500", "(11) 3333-4444", banco_beto)


banco_beto.add_branch(filial_centro)
print(f"Banco: {banco_beto._name}")
print(f"Filiais adicionadas: {[b.branch_id for b in banco_beto.show_branches()]}")