from tkinter import *
root =Tk()

root.geometry("400x300")
def action():
    N=int(Entryn1.get())
    N2=2*N
    Entryn2.delete(0,END)
    Entryn2.insert(0,N2)
lbln1=Label(root,text='Entrez la valeur de N:')
lbln1.place(x=40,y=40)
Entryn1=Entry(root,name="hello")
Entryn1.place(x=150,y=40)
lbln2=Label(root,text="resultat est :")
lbln2.place(x=40,y=80)
Entryn2=Entry(root)
Entryn2.place(x=150,y=80)
Valid=Button(root,text="valider l'operation",command=action)
Valid.place(x=200,y=150)
root.mainloop()