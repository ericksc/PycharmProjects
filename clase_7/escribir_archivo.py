# Se abre el archivo para escritura con el modo 'w'
archivo = open('texto.txt', 'w')
# se escriben algunas líneas
archivo.write('primera linea\n')
archivo.write('segunda linea\n')
archivo.write('buenas noches!!!!!!!!!!!')
# Y se cierra el archivo para que el sistema actulice la información en disco
archivo.close()