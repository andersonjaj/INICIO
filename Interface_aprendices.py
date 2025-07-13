#LIBRERIAS Y PAQUETES NECESARIOS
from tkinter import*
from tkinter import messagebox
import _sqlite3

#------funciones
#creamos una funcion para la creacion de la base de datos en sqlite3
def conexionBD():
	#asignamos un bombre a la BD
	miconexión=_sqlite3.connect("Apprendices")
	#creamos un cursor que nos ayudara a realizar las modifcaciones, insersiones
	# o creacion de lo necesario en la bd
	micursor=miconexión.cursor()
	#bloque try ayuda en el caso de que se tenga un error en este bloque
	#y de tener un error no se ejecutara
	try:
		#se crea la tabla con las columnas deseadas, indicamos nombre de la misma
		#nombre de las columnas y los tipos de datos
		micursor.execute('''
			CREATE TABLE DATOSAPRENDICES ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
				CEDULA INTEGER,
				NOMBRE VARCHAR(50),
				APELLIDO VARCHAR(50),
				ESTATUS VARCHAR(50),
				CALIFICACION INTEGER)
				''')
		#al finalizar la creacion de la tabla arrojara un el presente mensaje
		messagebox.showinfo("BD","BD creada con exito")
	#si hay un error en el bloque marcado indicara este mensaje	como excecioN
	except:
		messagebox.showwarning("CUIDADO", "La base de datos ya existe")
#creamos ahora una funcion para el menu desplegable de salir
def salirdelaapp():
	#Se realiza una pregunta de si y no para luego guardar el valor seleccionado
	valor=messagebox.askquestion("Salir","Quiere salir de la aplicación?")
	#si el valor es si entonces mediante el metodo destroy() cierra la app
	if valor=="yes":
		raiz.destroy()

#Se crear una funcion la cual limpiara los campos de los cuadros de texto
def limpiarcampos():
	#con las varibles indicadas en la seccion de cuadro de texto
	#indicamos con la funcion set que se igual a vacio  con ""
	miid.set("")
	cedula.set("")
	cnota.set("")
	cnombre.set("")
	capellido.set("")
	cstatus.set("")

#se crea una funcion para crear o registrar nueva informacion a la BD
def crear():
	#nos conectamos a la BD
	miconexión=_sqlite3.connect("Apprendices")
	#creamos el cursos
	micursor=miconexión.cursor()

	notaacomparar = int(cnota.get())
	#bloque try ayuda en el caso de que se tenga un error en este bloque
	#y de tener un error no se ejecutara
	try:
		if notaacomparar > 16:
			estatusA= "APROBADO"
		else:
			estatusA="REPROBADO"

		#instruccion sql para ingresar la informacion
		micursor.execute("INSERT INTO DATOSAPRENDICES VALUES(NULL,'" + cedula.get()+
			"','"+cnombre.get() +
			"','"+capellido.get() +
			"','"+estatusA +
			"','"+cnota.get() + " ')")
	#guardamos la informacion en la BD
		miconexión.commit()
		messagebox.showinfo("BD" , "Registro guardado!")
	except:
		messagebox.showwarning("CUIDADO", "Dato invalido en la nota")

def leer():
	#nos conectamos a la BD
	miconexión=_sqlite3.connect("Apprendices")
	#creamos el cursos
	micursor=miconexión.cursor()
	#instruccion para leer datos en la BD
	micursor.execute("SELECT * FROM DATOSAPRENDICES WHERE ID="+miid.get())

	#fetchall nos devuelve nos devuelve un array con lo datos  que se encuentren en la BD
	elaprendiz=micursor.fetchall()
	# Con el bucle for recorremos el array para luego asiganarselo a las variables y mostrarselas al usuario
	for aprendiz in elaprendiz:

		miid.set(aprendiz[0])
		cedula.set(aprendiz[1])
		cnombre.set(aprendiz[2])
		capellido.set(aprendiz[3])
		cstatus.set(aprendiz[4])
		cnota.set(aprendiz[5])
	#guardamos la informacion
	miconexión.commit()

def actualizar():
	#nos conectamos a la BD
	miconexión=_sqlite3.connect("Apprendices")
	#creamos el cursos
	micursor=miconexión.cursor()

	#bloque try ayuda en el caso de que se tenga un error en este bloque 
	#y de tener un error no se ejecutara 
	try:
		#Creamos una variable para guardar la informacion de las notas y convertimos a numeros para poder usar if
		notaacomparar = int(cnota.get())
		#aqui comparamos la nota antes convertida y si el alumno tiene mas de 16 aprueba la materia
		if notaacomparar > 16:
			estatusA= "APROBADO"
		else: 
			estatusA="REPROBADO"

	#instruccion sql para ingresar la informacion 
		micursor.execute("UPDATE DATOSAPRENDICES SET CEDULA='" + cedula.get()+
			"', NOMBRE='" + cnombre.get()+
			"', APELLIDO='" + capellido.get()+
			"', ESTATUS='" + estatusA+
			"', CALIFICACION='" + cnota.get()+
			"' WHERE ID="+miid.get())
	#guardamos la informacion en la BD
		miconexión.commit()
		#indicamos mediante un mensaje emergente si se actualizo correctamente
		messagebox.showinfo("BD" , "Registro actualizado!")
	except:
		#si hay error mostrara este mensaje denotando que ingresaron informacion incorrecta en el cuadro de texto de la nota
		messagebox.showwarning("CUIDADO", "Dato invalido en la nota")


def borraregistro():
	#nos conectamos a la BD
	miconexión=_sqlite3.connect("Apprendices")
	#creamos el cursos
	micursor=miconexión.cursor()
	#instruccion SQL para borrar la fila indicada mediante la ID
	micursor.execute("DELETE FROM DATOSAPRENDICES WHERE ID="+ miid.get())
	#GUARDAMOS LA INFORMACION
	miconexión.commit()

	messagebox.showinfo("BD","Registro borrado!")



#creamos la raiz donde se empezara la interface
raiz=Tk()

#menu de la parte superior---------------------------------------------------------------------
#con esto indicamos que este meni se encontrara en la raiz
barramenu=Menu(raiz)
#configuramos el menu, indicamos las dimenciones
raiz.config(menu=barramenu,width=300,height=300)
#elementos del menu, con tearoff quitamos las lineas para tener una mejor visualizacion (esteticamente)
bdmenu=Menu(barramenu, tearoff=0)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
bdmenu.add_command(label="Conectar", command=conexionBD)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
bdmenu.add_command(label="Salir",command=salirdelaapp)

borrarmenu=Menu(barramenu, tearoff=0)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
borrarmenu.add_command(label="Borrar campos", command=limpiarcampos)

crudmenu=Menu(barramenu, tearoff=0)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
crudmenu.add_command(label="Crear", command=crear)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
crudmenu.add_command(label="Leer", command=leer)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
crudmenu.add_command(label="Actualizar", command= actualizar)
#aqui indicamos con label indicamos el texto a aparecer en el menu desplegable
#junto a un comannd que es la funcion que se ejecutara al hacer click en ella
crudmenu.add_command(label="Borrar", command=borraregistro)

#aqui especificamos que los elementos antes mencionados pertenecen a la barra de menu
#pero agruparlos en su respectivo lugar
#indicamos con label el nombre de la etiqueta y luego con menu le indicamos los elementos que estarn en ella
barramenu.add_cascade(label="BD", menu=bdmenu)
barramenu.add_cascade(label="Borrar", menu=borrarmenu)
barramenu.add_cascade(label="CRUD", menu=crudmenu)

#cuadros de texto para la interface grafica------------------------------------------------------
miframe=Frame(raiz)
miframe.pack() 
#se crea una varible para anexarle la funcion stringvar,esto permitira eliminar o
#tomar lo datos datos colocados en los Entry
miid=StringVar()
cedula=StringVar()
cnombre=StringVar()
cnota=StringVar()
capellido=StringVar()
cstatus=StringVar()
#creamos un cuadro de texxto que correspondera a la casilla ID
#le indicamos donde se va a colocar en este caso sera en el frame llamado "miframe"
#y le indicamos la variable que se usara y ayudara a editar o tomar la informarcion
cuadroid=Entry(miframe, textvariable=miid)
#indicamos la posicion por la funcion grid y el espacio de separacion con padx y pady
cuadroid.grid(row=0, column=1, padx=10, pady=10)


cuadronombre=Entry(miframe, textvariable=cnombre)
cuadronombre.grid(row=1, column=1, padx=10, pady=10)

cuadroapellido=Entry(miframe, textvariable=capellido)
cuadroapellido.grid(row=1, column=3, padx=10, pady=10)

cuadroci=Entry(miframe, textvariable=cedula)
cuadroci.grid(row=2, column=1, padx=10, pady=10)
cuadroci.config(fg="blue")

cuadronota=Entry(miframe,textvariable=cnota)
cuadronota.grid(row=3, column=1, padx=10, pady=10)

cuadroestatus=Entry(miframe,textvariable=cstatus)
cuadroestatus.grid(row=3, column=3, padx=10, pady=10)


#identificacion de texto------------------------------------------

#con label indicamos la informacion o texto a colocar en cada cuadro, ubicandolos en
#La posicion idonea gracias a grind, con separacion de padx y padx, y justificado al 
#lado que mas nos convenga o veamos mejor
milabelid=Label(miframe, text="ID")
milabelid.grid(row=0, column=0, sticky="e", padx=10,pady=10)
milabelid.config(justify="right")

milabeltext=Label(miframe, text="La ID no es editable pero podra \n buscar, eleminar y actualizar \n información con la misma")
milabeltext.grid(row=0, column=2, sticky="e", padx=10,pady=10)
milabeltext.config(justify="left")

milabelcedula=Label(miframe, text="Cedula de identidad")
milabelcedula.grid(row=2, column=0, sticky="e", padx=10,pady=10)
milabelcedula.config(justify="right")

milabelnomnbre=Label(miframe, text="Nombre del apnrediz")
milabelnomnbre.grid(row=1, column=0, sticky="e", padx=10,pady=10)
milabelnomnbre.config(justify="right")

milabelapellido=Label(miframe, text="Apellido del apnrediz")
milabelapellido.grid(row=1, column=2, sticky="e", padx=10,pady=10)
milabelapellido.config(justify="right")

milabelnnota=Label(miframe, text="Ingresa la nota final")
milabelnnota.grid(row=3, column=0, sticky="e", padx=10,pady=10)
milabelnnota.config(justify="right")

milabelnnota=Label(miframe, text="Estatus final")
milabelnnota.grid(row=3, column=2, sticky="e", padx=10,pady=10)
milabelnnota.config(justify="right")

milabelnnota=Label(miframe, text="La nota para aparobar debe ser mayor a 16 si se equivoca \n podra actualizar la informacion en caso de equivocarse \n El estatus final queda determinado por la nota")
milabelnnota.grid(row=4, column=0, sticky="e", padx=10,pady=10)
milabelnnota.config(justify="right")

miframe2=Frame(raiz)
miframe2.pack()

#BOTONES----------------------------------------------------
#Se crean botones de facil acceso a cada una de las funciones de CRUD
#con button se crea el boton , especificando en que frame se ubicara, el texto
# y coamndo que se ejecutara al pulsarlo
#lo ubicamos con facilidad gracias a grind
botoncrear=Button(miframe2,text= "Create", command=crear)
botoncrear.grid(row=1,column=0, sticky="e",padx=10,pady=10)

botoncrear=Button(miframe2,text= "Read",command=leer)
botoncrear.grid(row=1,column=1, sticky="e",padx=10,pady=10)

botoncrear=Button(miframe2,text= "Update",command= actualizar)
botoncrear.grid(row=1,column=2, sticky="e",padx=10,pady=10)

botoncrear=Button(miframe2,text= "Delete", command=borraregistro)
botoncrear.grid(row=1,column=3, sticky="e",padx=10,pady=10)



raiz.mainloop()