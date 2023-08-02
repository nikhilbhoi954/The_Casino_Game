from tkinter import*
import time
import random
from turtle import back
#home page
root=Tk()
root.title("Data Science")
root.geometry("1000x500")
root.configure(background="black")

balance = 2000
#*********************************************************************************
def RULES():
     global e,Current_balance_seven,Current_balance_seven1,Current_balance_seven2,Back_Btn,Bet,Start_Btn,Try
     rules_btn.destroy()
     guess_btn.destroy()
     seven_btn.destroy()
     exit_btn.destroy()
     Current_balance_main.destroy( )
     Welcome.destroy()
     
     Back_Btn = Button (root,text="Back",bg="yellow",height=1,width=4,bd=5,fg= "black",command= exit)
     Back_Tuple = ("Times New Roman",20,"bold")
     Back_Btn.configure(font = Back_Tuple )
     Back_Btn.grid(row=0,column=0,padx=10,pady =10)

     Try = Label(root,text=f"           RULES ",bg="black",fg="yellow")
     Try_Tuple =("Times New Roman",40,"bold")
     Try.configure(font = Try_Tuple)
     Try.grid(row=1,column=3,padx=150,pady =5, columnspan=25,rowspan =2)

     Current_balance_seven =  Label(root,text=f"  1. You need sufficient balance.    ",bg="black",fg="light blue")
     Current_balance_seven1 = Label(root,text=f"2. Bet in guess game is 2*.  ",bg="black",fg="light blue")
     Current_balance_seven2 = Label(root,text=f"     3. Betting point in seven game this are following :\ni) Three times seven then bet 10*.\n             ii) Three numbers are even or odd then bet 5*.  ",bg="black",fg="light blue")
     
     Balance_tuple = ("Times New Roman",20,"bold")
     Current_balance_seven.configure(font="balance_tuple")
     Current_balance_seven.grid(row=4,column=1,padx=300,pady=15,rowspan=2,columnspan=8)

     Balance_tuple = ("Times New Roman",20,"bold")
     Current_balance_seven1.configure(font="balance_tuple")
     Current_balance_seven1.grid(row=6,column=1,padx=0,pady=15,rowspan=2,columnspan=8)

     Balance_tuple = ("Times New Roman",20,"bold")
     Current_balance_seven2.configure(font="balance_tuple")
     Current_balance_seven2.grid(row=8,column=2,padx=300,pady=15,rowspan=2,columnspan=8)




#*********************************************************************************
#seven game program
def destroy_call_seven(): 
    num_label.destroy()
    Congratulations.destroy()
    Play_again_btn.destroy()
    Current_balance_seven.destroy()
    Current_balance_seven1.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Back_Btn.destroy()
    Start_Btn.destroy()
    SEVEN()

def destroy_to_main_seven():
    num_label.destroy()
    Congratulations.destroy()
    Play_again_btn.destroy()
    Current_balance_seven1.destroy()
    Current_balance_seven.destroy()
    Try.destroy()
    Bet.destroy()
    e.destroy()
    Back_Btn.destroy()
    Start_Btn.destroy()
    main()

def bet_try_seven():
    global num_label,Congratulations,Play_again_btn,Current_balance_seven1,balance
    time.sleep(2)
    try:
       bet_guess = int(e.get())
    except ValueError:
        bet_guess =100
    
    if(bet_guess <= balance):
        num_list = [0,1,2,3,4,5,6,7,8,9]
        num1 = random.choice(num_list)    
        num2 = random.choice(num_list)  
        num3 = random.choice(num_list)


        num_label= Label(root,text=f"{num1}     {num2}      {num3}",bg="black",fg="white")  
        num_Tuple = ("Times New Roman",55,"bold")
        num_label.configure(font = num_Tuple )
        num_label.grid(row=8,column=4,padx=10,pady =10,columnspan=12)

        if(num1==7 and num2==7 and num3 == 7):
            Congratulations=Label(root,text=f"Congratulation !! Yor are Won : ${bet_guess*10}",bg="black",fg="light blue")
            Congo_Tuple=("Times New Roman",40,"bold")
            Congratulations.configure(font = Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady =25,columnspan= 35)
            Current_balance_seven.destroy()
            balance = balance + bet_guess*9
            Current_balance_seven1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
            Balance_Tuple=("Times New Roman",25,"bold")
            Current_balance_seven1.configure(font = Balance_Tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,columnspan=5,rowspan=2)  
         
        elif(num1==num2 and num2==num3 and num3==num1):
            Congratulations=Label(root,text=f"Congratulation !! Yor are Won : ${bet_guess*5}",bg="black",fg="light blue")
            Congo_Tuple=("Times New Roman",40,"bold")
            Congratulations.configure(font = Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady =25,columnspan= 35)
            Current_balance_seven.destroy()
            balance = balance + bet_guess*4
            Current_balance_seven1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
            Balance_Tuple=("Times New Roman",25,"bold")
            Current_balance_seven1.configure(font = Balance_Tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,columnspan=5,rowspan=2)  
        
        elif(num1%2==0 and num2%2==0 and num3%2==0 ):  
            Congratulations=Label(root,text=f"Congratulation !! Yor are Won : ${bet_guess*2}",bg="black",fg="light blue")
            Congo_Tuple=("Times New Roman",40,"bold")
            Congratulations.configure(font = Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady =25,columnspan= 35)
            Current_balance_seven.destroy()
            balance = balance + bet_guess
            Current_balance_seven1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
            Balance_Tuple=("Times New Roman",25,"bold")
            Current_balance_seven1.configure(font = Balance_Tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,columnspan=5,rowspan=2)  
        
        elif(num1%2!=0 and num2%2!=0 and num3%2!=0 ):  
            Congratulations=Label(root,text=f"Congratulation !! Yor are Won : ${bet_guess*2}",bg="black",fg="light blue")
            Congo_Tuple=("Times New Roman",40,"bold")
            Congratulations.configure(font = Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady =25,columnspan= 35)
            Current_balance_seven.destroy()
            balance = balance + bet_guess
            Current_balance_seven1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
            Balance_Tuple=("Times New Roman",25,"bold")
            Current_balance_seven1.configure(font = Balance_Tuple)
            Current_balance_seven1.grid(row=0,column=1,pady=5,columnspan=5,rowspan=2)  

        else:
            Congratulations=Label(root,text=f"Oops !! You are Lost : ${bet_guess}",bg="black",fg="light blue")
            Congo_Tuple=("Times New Roman",40,"bold")
            Congratulations.configure(font = Congo_Tuple)
            Congratulations.grid(row=7,column=2,padx=10,pady =25,columnspan= 35)
            Current_balance_seven.destroy()
            balance = balance - bet_guess
            Current_balance_seven1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
            Balance_Tuple=("Times New Roman",25,"bold")
            Current_balance_seven1.configure(font = Balance_Tuple)
            Current_balance_seven1.grid(row=0,column=1,pady =5,columnspan= 5,rowspan=2)

            Play_tuple =("Times New Roman",20,"bold")
            Play_again_btn =Button(root,text= "Play Again", bg="yellow",fg="red",font = Play_tuple,command=destroy_call_seven )
            Play_again_btn.grid(row=14,column=4,padx=10,columnspan= 10)
              


def SEVEN():
     global e,Current_balance_seven,Back_Btn,Bet,Start_Btn,Try
     rules_btn.destroy()
     guess_btn.destroy()
     seven_btn.destroy()
     exit_btn.destroy()
     Current_balance_main.destroy()
     Welcome.destroy()

     Back_Btn = Button (root,text="Back",bg="yellow",height=1,width=4,bd=5,fg= "black",command= destroy_to_main_seven)
     Back_Tuple = ("Times New Roman",20,"bold")
     Back_Btn.configure(font = Back_Tuple )
     Back_Btn.grid(row=0,column=0,padx=10,pady =10)

     Current_balance_seven = Label(root,text=f" Your Current balance is :- ${balance}",bg="black",fg="white")
     Balance_tuple = ("Times New Roman",30,"bold")
     Current_balance_seven.configure(font="balance_tuple")
     Current_balance_seven.grid(row=0,column=1,padx=0,pady=5,rowspan=2,columnspan=8)
     
     Try = Label(root,text=f" Let's Play The Game !!",bg="black",fg="yellow")
     Try_Tuple =("Times New Roman",45,"bold")
     Try.configure(font = Try_Tuple)
     Try.grid(row=3,column=1,padx=100,pady =5, columnspan=30,rowspan =2)

     Bet = Label(root,text=f"   Place Your Bet :-->",bg="black",fg="light blue")
     Bet_tuple =("Times New Roman",20,"bold")
     Bet.configure(font = Bet_tuple)
     Bet.grid(row=5,column=1,pady =5, columnspan=10)

     e=Entry(root,width=20,bg="light blue",fg="blue")
     e.grid(row=5,column=8,pady =5, columnspan=10)

     Start_Tuple = ("Times New Roman",15,"bold")
     Start_Btn = Button(root,text="Place",bg="yellow",fg="red",font= Start_Tuple,bd=5,command=bet_try_seven)
     Start_Btn.grid(row=5,column=13,columnspan=7,pady=20)
    



#**********************************************************************************
#guess game
def destroy_call_guess():
      e_choose.destroy()
      Choose.destroy()
      Congratulations.destroy()
      num_label.destroy()
      Current_balance_guess1.destroy()
      Play_again_btn.destroy()
      Current_balance_guess.destroy()
      Back_Btn.destroy()
      Try.destroy() 
      Bet.destroy()
      e.destroy()
      Start_Btn1.destroy()
      Start_Btn.destroy()
     
      GUESS()

def destroy_call_main():
      e_choose.destroy()
      Choose.destroy()
      Congratulations.destroy()
      num_label.destroy()
      Current_balance_guess1.destroy()
      Current_balance_guess.destroy()
      Back_Btn.destroy()
      Try.destroy() 
      Bet.destroy()
      e.destroy()
      Play_again_btn.destroy()
      Start_Btn1.destroy()
      Start_Btn.destroy()
      main()


def bet_choosed():
       global balance,Congratulations,Current_balance_guess1,num_label,Play_again_btn


       try :
         choosen_num= int(e_choose.get())
       except ValueError:
         choosen_num=0

       num_list = [1,2,3,4,5]     
       num=random.choice(num_list)
       num_label=Label(root,text=f"Computer choosed:--> {num}",bg="black",fg="light blue")
       num_tuple=("Times New Roman",45,"bold")
       num_label.configure(font = num_tuple )
       num_label.grid(row=7,column=1,padx=10,pady =10,columnspan= 30)
       time.sleep(2)
      
       if(choosen_num==num):
          Congratulations=Label(root,text=f"Congratulation !! Yor are Won : ${bet_guess*2}",bg="black",fg="light blue")
          Congo_Tuple=("Times New Roman",40,"bold")
          Congratulations.configure(font = Congo_Tuple)
          Congratulations.grid(row=8,column=2,padx=10,pady =10,columnspan= 35)
          Current_balance_guess.destroy()
          balance = balance + bet_guess
          Current_balance_guess1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
          Balance_Tuple=("Times New Roman",25,"bold")
          Current_balance_guess1.configure(font = Balance_Tuple)
          Current_balance_guess1.grid(row=0,column=1,pady=5,columnspan=5,rowspan=2)

       

       else:
          Congratulations=Label(root,text=f"Oops !! You are Lost : ${bet_guess}",bg="black",fg="light blue")
          Congo_Tuple=("Times New Roman",40,"bold")
          Congratulations.configure(font = Congo_Tuple)
          Congratulations.grid(row=8,column=2,padx=10,pady =10,columnspan= 35)
          Current_balance_guess.destroy()
          balance = balance - bet_guess
          Current_balance_guess1 = Label(root,text=f"Your Current Balance is :--> ${balance}",bg="black",fg="light blue")
          Balance_Tuple=("Times New Roman",25,"bold")
          Current_balance_guess1.configure(font = Balance_Tuple)
          Current_balance_guess1.grid(row=0,column=1,pady =5,columnspan= 5,rowspan=2)

          Play_tuple =("Times New Roman",20,"bold")
          Play_again_btn =Button(root,text= "Play Again", bg="yellow",fg="red",font = Play_tuple,command=destroy_call_guess )
          Play_again_btn.grid(row=15,column=3,padx=10,columnspan= 10)
          
       



def bet_try_guess():

   global e_choose,bet_guess,Choose,Start_Btn

   try:
      bet_guess = int(e.get())
   except ValueError:
      bet_guess=100

   if (bet_guess <= balance):
      Choose = Label(root,text="    Choose a number b/w [1-5]:--> ",bg="black",fg="light blue")
      Choose_Tuple = ("Times New Roman",20,"bold")
      Choose.configure(font = Choose_Tuple )
      Choose.grid(row=6,column=1,pady =5,columnspan= 10)

      e_choose = Entry(root,width=10,bg="light blue",fg="blue")
      e_choose.grid(row=6,column=10,pady =5,columnspan= 5)  
      
      Start_Tuple=("Times New Roman",15,"bold")
      Start_Btn =Button (root,text="Done",bg="yellow",fg= "red",font=Start_Tuple,command=bet_choosed,bd=5)                          
      Start_Btn.grid(row=6,column=13,columnspan=7,pady=20)

  
       

def GUESS():

   global Current_balance_guess,e,Bet,Back_Btn,Try,Start_Btn1

   rules_btn.destroy()
   guess_btn.destroy()
   seven_btn.destroy()
   exit_btn.destroy()
   Current_balance_main.destroy()
   Welcome.destroy()

   Back_Btn = Button (root,text="Back",bg="yellow",height=1,width=4,bd=5,fg= "black",command=destroy_call_main)
   Back_Tuple = ("Times New Roman",20,"bold")
   Back_Btn.configure(font = Back_Tuple )
   Back_Btn.grid(row=0,column=0,padx=10,pady =10)

   Current_balance_guess = Label(root,text=f" Your Current balance is :- ${balance}",bg="black",fg="white")
   Balance_tuple = ("Times New Roman",30,"bold")
   Current_balance_guess.configure(font="Balance_tuple")
   Current_balance_guess.grid(row=0,column=1,padx=0,pady=5,rowspan=2,columnspan=8)

   Try = Label(root,text=f" Let's Play The Game !!",bg="black",fg="yellow")
   Try_Tuple =("Times New Roman",45,"bold")
   Try.configure(font = Try_Tuple)
   Try.grid(row=3,column=1,padx=100,pady =5, columnspan=30,rowspan =2)

   Bet = Label(root,text=f"   Place Your Bet :-->",bg="black",fg="light blue")
   Bet_tuple =("Times New Roman",20,"bold")
   Bet.configure(font = Bet_tuple)
   Bet.grid(row=5,column=1,pady =5, columnspan=10)

   e=Entry(root,width=20,bg="light blue",fg="blue")
   e.grid(row=5,column=8,pady =5, columnspan=10)

   Start_Tuple = ("Times New Roman",15,"bold")
   Start_Btn1 = Button(root,text="Place",bg="yellow",fg="red",font= Start_Tuple,bd=5,command=bet_try_guess)
   Start_Btn1.grid(row=5,column=13,columnspan=7,pady=20)







def main():
   global rules_btn,guess_btn,seven_btn,exit_btn,Current_balance_main,Welcome


   Current_balance_main = Label(root,text=f" Your Current balance is :- ${balance}",bg="black",fg="white")
   Balance_tuple = ("Times New Roman",25)
   Current_balance_main.configure(font="balance_tuple")
   Current_balance_main.grid(row=0,column=0,padx=0,pady=10,rowspan=2,columnspan=8)

   Welcome=Label(root,text="  The Casino Game",bg="black",fg="yellow")
   Welcome_tuple=("Times New Roman",60,"bold")
   Welcome.configure(font = Welcome_tuple)
   Welcome.grid(row=2,column=1,rowspan=2,columnspan=40,padx=150)

   #home page BUTTONS

   guess_btn= Button(root,text="Guess",bg="light blue",height=1,width=5,bd=10,command = GUESS)
   guess_tuple=("Arial",30,"bold")
   guess_btn.configure(font=guess_tuple)
   guess_btn.grid(row=4,column=6,columnspan=1,padx=150)


   seven_btn= Button(root,text="Seven",bg="light blue",fg="black",height=1,width=13,bd=10,command=SEVEN)
   seven_btn.configure(font=guess_tuple)
   seven_btn.grid(row=4,column=10,columnspan=2)

   rules_btn = Button(root,text="Rules",bg="light blue",width=5,bd=10,command=RULES)
   rules_btn.configure(font=guess_tuple)
   rules_btn.grid(row=5,column=6,columnspan=1,padx=20,pady=10)

   exit_btn = Button(root,text="Exit",bg="light blue",width=5,bd=10,command=exit)
   exit_btn.configure(font=guess_tuple)
   exit_btn.grid(row=5,column=10,columnspan=1,padx=20,pady=10)




  
main()
root.mainloop()
