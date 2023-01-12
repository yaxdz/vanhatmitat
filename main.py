LUODIT_KERROIN =13.3
NAULA_KERROIN = 32 * LUODIT_KERROIN
LEIVISKÄ_KERROIN = 20 * NAULA_KERROIN * LUODIT_KERROIN



leiviskätGrammoina = float(input("Anna leiviskät: ")) * LEIVISKÄ_KERROIN
naulatGrammoina =  float(input("Anna naulat: ")) * NAULA_KERROIN
luoditGrammoina = float(input("Anna luodit: ")) * LUODIT_KERROIN
grammatYhteensä = leiviskätGrammoina + naulatGrammoina + luoditGrammoina
kilogrammat = grammatYhteensä / 1000
grammat = grammatYhteensä % 1000

print(kilogrammat)
print(grammat)
print(leiviskätGrammoina)


print(LEIVISKÄ_KERROIN)
print(naulatGrammoina)
print(luoditGrammoina)