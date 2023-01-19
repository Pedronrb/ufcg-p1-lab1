palavra = "programação"                    # strinsg são sequências
frase = ["python", "é", "a", "linguagem"]  # listas são sequências
dados = (10.4, 5.5, "tupla heterogenea")   # tuplas são sequências
sequencia = range(100, 200, 15)            # ranges são sequências
# a função iter() cria um iterador para uma sequência
it1 = iter(palavra)
it2 = iter(frase)
it3 = iter(dados)
it4 = iter(sequencia)

e1 = next(it3)     # retorna o primeiro elemento da iteração
e2 = next(it3)     # retorna o segundo elemento
e3 = next(it3)     # retorna o terceiro (e último) elemento
# e3 = next(it3)   # esta invocação dá erro: StopIteration
print(e1, e2, e3)