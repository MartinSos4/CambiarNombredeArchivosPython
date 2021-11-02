import os
from tkinter import * 
raiz=Tk()
raiz.title("Cambiar")
raiz.resizable(True,False)
raiz.iconbitmap()
raiz.config(bg="black")

#miFrame=Frame(raiz,width=1200,height=600)
#miFrame.pack()


#cuadroNombre=Entry(miFrame)
#cuadroNombre.grid(row=0,column=1,padx=10, pady=10)

#cuadroNombre=Entry(miFrame)
#cuadroNombre.grid(row=1,column=1,padx=10, pady=10)


#nombreLabel=Label(miFrame, text="Dirección:")
#nombreLabel.grid(row=0, column=0,sticky="e", padx=10,pady=10)

#direccion1Label=Label(miFrame, text="Dirección a cambiar:")
#direccion1Label.grid(row=1, column=0,sticky="e", padx=10,pady=10)



#raiz.mainloop()


os.chdir(r"C:\Users\Martin\Desktop\Template FG0")
#colocar aquí datos con numeros C.I.
f=open(r"C:\Users\Martin\Desktop\Desarrollo-San\ListadoPrueba2.txt")
fsal=open(r"C:\Users\Martin\Desktop\Desarrollo-San\Listadosalida.txt")
lista=f.read().splitlines()
listasal=fsal.read().splitlines()
listareemplazos=list()
lista1=list(lista)
listanoreemplazos1 = list(lista)
listanoreemplazossal = list(listasal)
print(lista1)
#colocar aquí datos viejos.
f=open(r"C:\Users\Martin\Desktop\Desarrollo-San\ListadoPrueba1.txt")
lista=f.read().splitlines()
lista2=list(lista)
listanoreemplazos2 = list(lista)
largolista=len(lista1)
print(lista2)
i=0
flog = open(r"C:\Users\Martin\Desktop\Desarrollo-San\Log.txt","w")
ferr = open(r"C:\Users\Martin\Desktop\Desarrollo-San\Errores.txt","w")
for file in os.listdir():
	ext = os.path.splitext(file)
	
	for i in range(largolista):
		linea = listasal[i]
		src=lista2[i]
		dst=lista1[i]
		if os.path.isfile(src + ext[1]):
			os.rename(src + ext[1],dst + ext[1])
			
			flog.write(src + ext[1] + "," + dst + ext[1] + os.linesep)	
			listareemplazos.append(src + ext[1])
			print(listanoreemplazos1)
			if src in listanoreemplazos2:
				listanoreemplazossal.remove(linea)
				listanoreemplazos1.remove(dst)
				listanoreemplazos2.remove(src)
	if file not in listareemplazos:
				ferr.write(file + os.linesep)	
flog.close()
ferr.close()
fnr = open(r"C:\Users\Martin\Desktop\Desarrollo-San\Noreemplazados.txt","w")
fnrsal = open(r"C:\Users\Martin\Desktop\Desarrollo-San\NoreemplazadosSalida.txt","w")
for i in range(len(listanoreemplazossal)):
	fnrsal.write(listanoreemplazossal[i])
for i in range(len(listanoreemplazos1)):
	fnr.write(listanoreemplazos1[i] + "," + listanoreemplazos2[i] + os.linesep)
fnr.close()
