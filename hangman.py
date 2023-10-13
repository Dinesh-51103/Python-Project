import random
from tkinter import *
from tkinter import messagebox
import string as string


score = 0
run = True
b_g = '#000000' 


#letters icon
bl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
al = [i for i in range(0,26)]
# for i in al : 
#     exec(f"bl[{i}]=string.ascii_lowercase[{i}]")

#letters placement
# button = [['b1','a',0,585],['b2','b',70,585],['b3','c',140,585],['b4','d',210,585],['b5','e',280,585],['b6','f',350,585],['b7','g',420,585],['b8','h',490,585],['b9','i',560,585],['b10','j',630,585],['b11','k',700,585],['b12','l',770,585],['b13','m',840,585],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]
button = [[f"b{i+1}"] for i in range(0,26)]
for i in range(0,26) : 
    exec(f"button[{i}].extend([al[{i}]])")
    exec(f"button[{i}].extend([bl[{i}]])")
    if i <= 12 :
        exec(f"button[{i}].extend([{i}*70,585])")
    else :
        exec(f"button[{i}].extend([({i}-13)*70,645]) ")

# hangman images
# h123 = ['h1','h2','h3','h4','h5','h6','h7']
h123 = [f"h{i+1}" for i in range(0,7)]

#hangman placement
# han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
han = [[f"c{i+1}",h123[i]] for i in range(0,7)]

    # main loop
while run:
    count = 0
    win_count = 0
    root = Tk()
    root.geometry('920x700')
    root.title('--HANG MAN--')
    root.config(bg = b_g)
        

    # choosing word
    index = random.randint(0,853)
    with open('words.txt','r') as file:
        word_list = file.readlines()
    selected_word = word_list[index].strip('\n')
        
    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        x += 50
        exec('d{}=Label(root,text="_",fg="#ffffff",bg="#000000",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
           
        
    # creating letters 
    for let in al:
        exec('g{}=PhotoImage(file="images/{}.png")'.format(let,let))
            
        
    #creating hang images
    for hangman in h123:
        exec('{}=PhotoImage(file="images/{}.png")'.format(hangman,hangman))
            
    #checking each button
    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#000000",activebackground="#000000",font=10,image=g{})'.format(q1[0],q1[2],q1[0],q1[1]))

        # exec(f"i{i} = PhotoImage(file='images/{q1[i]}.png')")
            
        # exec(f"{q1[0]}=Button(root,bd=0,command=lambda:check('{q1[1]}','{q1[0]}'),bg='#000000',image={q1[0]},activebackground='#000000',font=10)")
        exec('{}.place(x={},y={})'.format(q1[0],q1[3],q1[4]))
            
    #hangman placement
    for p1 in han:
        exec('{}=Label(root,bg="#000000",image={})'.format(p1[0],p1[1]))
        # exec('{}=Label(place(x=300,y=100))'.format(p1[0]))
        
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('EXIT', 'DO YOU WANT TO EXIT THE GAME ? :(')
        if answer == True:
            run = False
            root.destroy()

    # Exit Button       
    e1 = PhotoImage(file = 'images/exit.png')
    ex = Button(root,bd = 0,command = close,bg="#999999",activebackground = "#999999",font = 0,image = e1,borderwidth=5,)
    ex.place(x=770,y=10)

    # Score 
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,fg="#ffffff",bg = "#000000",font = ("arial",25))
    s1.place(x = 10,y = 10)

    # button press check function
    def check (letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        # letter = string.ascii_lowercase[letter]
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 2
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            # exec('c{}.destroy()'.format(count))
            #hang formation
            exec('c{}.place(x={},y={})'.format(count+1,300,100))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()

