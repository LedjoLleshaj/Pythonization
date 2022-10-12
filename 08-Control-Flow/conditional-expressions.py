codice_fiscale = input("Inserisci il tuo codice fiscale: ")
# length validation long version
# if len(codice_fiscale) == 16:
#     print("Valido")
# else:
#     print("Non valido")

check = "Valido" if len(codice_fiscale) == 16 else "Non valido"
print(check)
