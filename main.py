from tkinter import *
import pickle



class Clientes():
    def __init__(self,nombre,apellidos,telefono):
        self.nombre = nombre;
        self.apellidos = apellidos;
        self.telefono=telefono;

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getTelefono(self):
        return self.telefono

    def pintar(self):
        return"{}-{}-{}".format(self.nombre,self.apellidos,self.telefono)

    def __str__(self):
        return"{}-{}-{}".format(self.nombre,self.apellidos,self.telefono)


class ListaClientes:

    clientes=[]

    def __init__(self):
        try:
            listaDeClientes=open("fichero_clientes","ab+")
            listaDeClientes.seek(0)

            self.clientes=pickle.load(listaDeClientes)
            print("Clientes cargados {} clientes".format(len(self.clientes)))
        except:
            print("Fichero vacío")
        finally:
            listaDeClientes.close()
            del(listaDeClientes)

    def guardarClientesFichero(self):
        listaDeClientes = open("fichero_clientes", "wb")
        pickle.dump(self.clientes,listaDeClientes)
        listaDeClientes .close()
        del (listaDeClientes)


    def anadirClientes(self):
        ventana = Tk()
        ventana.geometry("400x300")
        etiquetaNombre = Label(ventana, text="Nombre")
        etiquetaNombre.pack()
        nombre = Entry(ventana)
        nombre.pack()
        etiquetaApe = Label(ventana, text="Apellidos")
        etiquetaApe.pack()
        apellidos = Entry(ventana)
        apellidos.pack()
        etiquetaTelef = Label(ventana, text="Telefono")
        etiquetaTelef.pack()
        telefono = Entry(ventana)
        telefono.pack()

        def anadirClientesCl():
            auxNom=nombre.get()
            auxApe=apellidos.get()
            auxTelf=telefono.get()

            c1 = Clientes(auxNom,auxApe,auxTelf)
            self.clientes.append(c1)
            self.guardarClientesFichero()
            ventana.destroy()

        boton = Button(ventana,text="Anadir cliente",command=anadirClientesCl)
        boton.pack()
        ventana.title("Objetos Serializables")
        ventana.mainloop()


    def mostrarClientes(self):
        for item in self.clientes:
            print(item)

    def leeFicheroClientes(self):
        ficheroBinario = open("fichero_clientes", "rb")
        lista = pickle.load(ficheroBinario)
        ficheroBinario.close()
        aux=""
        i=1;
        del(ficheroBinario)
        for itemclientes in lista:
            aux=aux+str(i)+" "+itemclientes.pintar()+"\n"
            i=i+1
        return aux

    def borrarCliente(self):
        ventana = Tk()
        ventana.geometry("400x300")
        etiquetaNombre = Label(ventana, text="Numero de cliente")
        etiquetaNombre.pack()
        posicion = Entry(ventana)
        posicion.pack()
        def borraClientePosicion():
            tamanioArray=len(self.clientes)
            poss=int(posicion.get())
            poss=poss-1
            if poss<=tamanioArray:
                self.clientes.pop(poss)
                self.guardarClientesFichero()
                ventana.destroy()


        boton = Button(ventana, text="Borrar", command=borraClientePosicion)
        boton.pack()
        ventana.title("Borrar Cliente")
        ventana.mainloop()

    def modificarCliente(self,p,ventanaPrincipal):
        tamanioArray = len(self.clientes)
        poss = int(p)
        poss=poss-1
        ventana = Tk()
        ventana.geometry("400x300")
        if poss <= tamanioArray and poss>=0:
            cliente=self.clientes[poss]
            ventanaPrincipal.destroy()
            cNombre=cliente.getNombre()
            cApe=cliente.getApellidos()
            cTelef=cliente.getTelefono()

            etiquetaNombre = Label(ventana, text="Nombre")
            etiquetaNombre.pack()
            nombre = Entry(ventana)
            nombre.insert(END,cNombre)
            nombre.pack()
            etiquetaApe = Label(ventana, text="Apellidos")
            etiquetaApe.pack()
            apellidos = Entry(ventana)
            apellidos.insert(END,cApe)
            apellidos.pack()
            etiquetaTelef = Label(ventana, text="Telefono")
            etiquetaTelef.pack()
            telefono = Entry(ventana)
            telefono.insert(END,cTelef)
            telefono.pack()

            def modCliente():
                self.clientes.pop(poss)
                c1=Clientes(nombre.get(),apellidos.get(),telefono.get())
                self.clientes.insert(poss,c1)
                self.guardarClientesFichero()
                ventana.destroy()
                ventana2=Tk();
                ventana2.geometry("300x70")
                etiquetaNombre = Label(ventana2, text="Cliente Modificado")
                etiquetaNombre.pack()
                def errMod():
                    ventana2.destroy()
                boton = Button(ventana2, text="Aceptar", command=errMod)
                boton.pack()
                ventana2.title("Modificado Con exito")
                ventana2.mainloop()

            boton = Button(ventana, text="Modificar Cliente",command=modCliente)
            boton.pack()
            ventana.title("Modificar Cliente")
            ventana.mainloop()
        else:

            ventana.geometry("300x70")
            etiquetaNombre = Label(ventana, text="Error al cargar el cliente")
            etiquetaNombre.pack()
            def errMod():
                ventana.destroy()

            boton = Button(ventana, text="Cerrar", command=errMod)
            boton.pack()
            ventana.title("Error al cargar cliente")
            ventana.mainloop()


def ventanaPrincipal():
    ventana = Tk()
    ventana.geometry("500x400")
    etiquetaaddClient = Label(ventana, text="Añadir Cliente")
    etiquetaaddClient.pack()
    boton = Button(ventana, text="Anadir cliente", command=anadirClientesVentana)
    boton.pack()
    etiquetadelCliente = Label(ventana, text="Borra Cliente")
    etiquetadelCliente.pack()
    boton = Button(ventana, text="Borra Cliente", command=borrarClientesVentana)
    boton.pack()
    etiquetalistCliente = Label(ventana, text="Listar Clientes")
    etiquetalistCliente.pack()
    boton = Button(ventana, text="Listar Clientes", command=listarClientesVentana)
    boton.pack()
    etiquetalistCliente = Label(ventana, text="Modificar Cliente")
    etiquetalistCliente.pack()
    boton = Button(ventana, text="Modificar Cliente", command=modificarClienteVentana)
    boton.pack()
    ventana.title("Objetos Serializables")
    ventana.mainloop()


def anadirClientesVentana():
    list=ListaClientes()
    list.anadirClientes()

def borrarClientesVentana():
    list=ListaClientes()
    list.borrarCliente()

def listarClientesVentana():
    list = ListaClientes()
    aux=list.leeFicheroClientes()
    ventana = Tk()
    ventana.geometry("600x500")
    etiquetaaddClient = Label(ventana, text="Clientes")
    etiquetaaddClient.pack()
    texto=Text(ventana,height=50,width=100)
    texto.insert(END,aux)
    texto.configure(state="disabled")
    texto.pack()
    ventana.title("Listado Clientes")
    ventana.mainloop()

def modificarClienteVentana():
    list = ListaClientes()
    ventana = Tk()
    ventana.geometry("400x300")
    etiquetaNombre = Label(ventana, text="Numero de cliente a modificar")
    etiquetaNombre.pack()
    posicion = Entry(ventana)
    posicion.pack()
    boton = Button(ventana, text="Ver Datos Cliente", command= lambda: list.modificarCliente(posicion.get(),ventana))
    boton.pack()
    ventana.title("Buscar Cliente a Modificar")
    ventana.mainloop()


ventanaPrincipal()

