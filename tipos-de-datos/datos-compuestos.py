#DATOS COMPUESTOS

#LISTA []: Son modificables
lista = ["leche", "manteca", "pan", 1, 3.4, False]
print(lista, "indice 1 de la lista:", lista[1])

#TUPLA (): No son modificables / para llamar el indice de una tupla es con []
tupla = ("leche", "manteca", "pan", 1, 3.4, False)
print(tupla[3])

#CONJUNTO/SET: No tienen un ordne fijo. Los elementos no se pueden modificar pero si su orden.
# el conjunt en sí si se puede redefinir 
# No se puede acceder a un elemento por el indice[i] No almacena datos duplicados
conjunto = {"leche", "manteca", "pan", 1, 3.4, False}
conjunto = {"hola, redifini el conjunto"}
print(conjunto)

#DICCIONARIO: Es equivalente a un json en JS - estructira 'clave': 'valor',
diccionario= {
'nombre': 'lucas dalto',
'canal_en': 'youtube'
}

print(diccionario['canal_en'])