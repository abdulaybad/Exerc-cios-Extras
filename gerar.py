import random
def gera_recargas():
	recargas =''
	for _ in range(0,9):
		i = random.randrange(0,9)
		recargas = recargas + str(i)
		
	return recargas 



