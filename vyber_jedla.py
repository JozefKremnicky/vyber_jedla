import tkinter
canvas=tkinter.Canvas(width=450,height=170)
canvas.pack()#vytvorene platna a zadanie jeho rozmerov

def stvorceky():# definovanie funkcie stvorceky 
    for i in range(len(farby)): # vytvorenie 4 stvorcekov 
        canvas.create_rectangle(x+i*vel, y, x+i*vel+vel-2, y+vel-2, fill=farby[i])
def stlacenie(sur): # definovanie funkcie stlacenie 
    if y < sur.y < y+ vel: # podmienka
        poradie = (sur.x-x) // vel
        if 0 <=poradie <len (farby):# podmienka
            print(poradie)
            student=entry1.get()
            if student != '': # podmienka ak v studentovi nieje nic napisane tak
                subor = open ('vyber_jedla','a') # otvory subor
                subor.write(student+''+kody[poradie]+'\n') # zapisanie do suboru cislo studenta + jeho kod a prida to novy riadok
                subor.close() # zavrie subor
canvas.create_text(200,20,text='VYBER JEDLA',font='Arial 20',fill='red') # vytvorenie textu
subor=open('/vyber_jedla','w') #otvorenie suboru z moznostou zapisovania
subor.close()# zavretie suboru
farby = ['green','red','blue','orange'] # premenna farby v ktorej su vlozene 4 farby
kody = 'grbo' # premenna kody v ktorej su 4 zaciatocne pismena na farby
x,y,vel = 15,50,100 # hodnoty premmennych x, y a vel
stvorceky() # vytvory stvorceky
canvas.bind('<Button-1>',stlacenie)# vytvorenie tlacitka
label1 = tkinter.Label(text='kod studenta:') # vytvorenie widgetu na text aby sa mohol aktualizovat 
label1.pack()
entry1 = tkinter.Entry() # vytvorenie vstupneho pola
entry1.pack()

                                
