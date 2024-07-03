from customtkinter import *
from tkinter import *
import json
from tkinter import messagebox


q_num = 0
master = CTk()
master.title("TRIVIALAND")
master.geometry("720x750")
score = 0

bg = PhotoImage(file= r"c:\Users\LENOVO\Downloads\tkinter image.png")
bglabel = CTkLabel(master, image= bg, text="")
bglabel.place(x=0, y=0)



#get questions for the Json file
with open("Question Bank.json", "r") as f:
    bank = json.load(f)



#create the label where the question will eb displayed
question_label = CTkLabel(master, anchor= CENTER, wraplength= 450, font = ("Times New Roman", 25))
question_label.pack(pady = 20)

scorelabel = CTkLabel(master, text = "score: "+ str(score), font = ("arial black", 15))
scorelabel.pack(padx = 40,anchor = "w")

answer_list = []
correct_answer = []
#to check if the answer is correct
def check_asnwer(choice):
    global score
    nextquestion.configure(state = "normal", text_color = "black")
    answer =  button_list[choice].cget("text")
    answer_list.append({f"{current_question+1}": answer})
    correct_answer.append({f"{current_question+1}":question["answer"]})
    if question["answer"] == answer:
        score+=1
        button_list[choice].configure(bg_color=  "green",fg_color=  "green", state = "normal")
        fb.configure(text = "Correct!", text_color = "green")
    else:
        
        button_list[choice].configure(fg_color=  "red", bg_color=  "red")
        fb.configure(text = "False", text_color = "red")
    
    for button in button_list:
        button.configure(state = "disabled")
    scorelabel.configure(text = "score: "+ str(score))
    
         

###to create the buttons that we will use to display the options
button_list = [] 
for i in range(4):
    button = CTkButton(master,  command = lambda choice = i: check_asnwer(choice))
    button.pack( padx = 50, pady = 50, anchor = "center" )
    button_list.append(button)
   

###assign the question name and options to the buttons

current_question=0
def show_question():
    global question
    question = bank["Question"][current_question]
    question_label.configure(text = question["name"])
    nextquestion.configure(state = "disabled")

    for i in range(4):
        button_list[i].configure(text = question["options"][i],
                                  fg_color = "#ADD8E6", bg_color = "#ADD8E6", state = "normal", text_color = "black", font = ("Arial Black", 20))


###to go to next question and it's options

def next_question():
    global current_question
      
    if current_question < len(bank["Question"])-1 :
          current_question+=1
          show_question()
    else: 
        messagebox.showinfo("Score!" , f"Your Answers : {answer_list}\n\nYour Score is : {score}\n\n Correct answers are : {[i for i in correct_answer if len(correct_answer)>0 ]}")
        nextquestion.configure(state = "disabled")

    fb.configure(text = "")


    
#create and display the next question button
nextquestion = CTkButton(master, text= "Next Question",fg_color = "white", bg_color = "white", command= next_question)
nextquestion.pack()
#create and display the feedback button
fb = CTkLabel(master, text= "", font= ("arial black", 25))
fb.pack(pady  = 20)


show_question()


master.mainloop()


   






    



