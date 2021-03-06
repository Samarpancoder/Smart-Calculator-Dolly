"""A simple Scientific Calculator in python"""
from tkinter import *
from tkinter import messagebox
import math

class but:
    def __init__(self,window):

        self.window=window
        self.text_value = StringVar()
        self.textoperator = StringVar()
        self.textoperator2 = StringVar()
        self.fact = 1

        self.widget()



    def butn(self):
        self.plus = Button(self.window,text="+",width=3,font=("arial",15,"bold"),fg="green",
                           command=lambda : self.opr("+"))
        self.plus.place(x=535,y=240)

        self.subs = Button(self.window, text="-", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("-"))
        self.subs.place(x=535, y=300)

        self.mul = Button(self.window, text="X", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("X"))
        self.mul.place(x=535, y=360)

        self.div = Button(self.window, text="/", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("/"))
        self.div.place(x=535, y=420)

        self.rad = Button(self.window, text="rad", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Radian"))
        self.rad.place(x=440, y=360)

        self.reci = Button(self.window, text="1/x", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Reciprocal"))
        self.reci.place(x=440, y=420)


        self.sqr = Button(self.window, text="X^2", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Square"))
        self.sqr.place(x=440, y=240)

        self.cube = Button(self.window, text="X^3", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Cube"))
        self.cube.place(x=440, y=300)

        self.equal = Button(self.window, text="=", width=11, font=("arial", 15, "bold"), fg="green",
                            command=self.evaluation_opr)
        self.equal.place(x=440, y=480)

        self.clear = Button(self.window, text="Information", width=11, font=("arial", 10, "bold"),
                            fg="green",command=self.information)
        self.clear.place(x=480, y=68)

        self.sqrt = Button(self.window, text="Square root", width=11, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Square root"))
        self.sqrt.place(x=10, y=240)

        self.cubert = Button(self.window, text="Cube root", width=11, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Cube root"))
        self.cubert.place(x=200, y=240)

        self.log2 = Button(self.window, text="log(base2)", width=11, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("log2"))
        self.log2.place(x=10, y=300)

        self.log10 = Button(self.window, text="log(base10)", width=11, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("log10"))
        self.log10.place(x=200, y=300)



        self.exponent = Button(self.window, text="e^x", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Exponent"))
        self.exponent.place(x=200, y=360)

        self.power = Button(self.window, text="X^Y", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("x^y"))
        self.power.place(x=295, y=360)

        self.factorial = Button(self.window, text="n!", width=5, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("Factorial"))
        self.factorial.place(x=10, y=360)

        self.mod = Button(self.window, text="Mod", width=4, font=("arial", 15, "bold"), fg="green",
                                command=lambda: self.opr("Modulus"))
        self.mod.place(x=94, y=360)


        self.reset = Button(self.window, text="Reset", width=5, font=("arial", 15, "bold"), fg="green",
                           command=self.reset_now)
        self.reset.place(x=10, y=420)

        self.reset = Button(self.window, text="Pi", width=4, font=("arial", 15, "bold"), fg="green",
                            command=self.pi_val)
        self.reset.place(x=95 ,y=420)

        self.sin = Button(self.window, text="sin", width=5, font=("arial", 15, "bold"), fg="green",
                               command=lambda: self.opr("sin"))
        self.sin.place(x=10, y=480)

        self.cos = Button(self.window, text="cos", width=4, font=("arial", 15, "bold"), fg="green",
                            command=lambda: self.opr("cos"))
        self.cos.place(x=95, y=480)

        self.tan = Button(self.window, text="tan", width=3, font=("arial", 15, "bold"), fg="green",
                                command=lambda: self.opr("tan"))
        self.tan.place(x=200, y=480)
        self.cot = Button(self.window, text="cot", width=3, font=("arial", 15, "bold"), fg="green",
                                command=lambda: self.opr("cot"))
        self.cot.place(x=295, y=480)



        self.bye = Button(self.window, text="Exit", width=47, font=("arial", 15, "bold"), fg="brown",
                           command=self.tata)
        self.bye.place(x=10, y=540)

        self.lcm = Button(self.window, text="LCM", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("lcm"))
        self.lcm.place(x=200, y=420)

        self.hcf = Button(self.window, text="HCF", width=3, font=("arial", 15, "bold"), fg="green",
                           command=lambda : self.opr("hcf"))
        self.hcf.place(x=295, y=420)

    def widget(self):
        self.heading = Label(self.window,text="Scientific Calculator(Dolly)",font=("arial",30,"bold","italic"),fg="blue")
        self.heading.place(x=50,y=5)

        self.result_name = Label(self.window, text="Result: ", width=8, font=("arial", 16, "bold", "italic"),
                                  fg="green")
        self.result_name.place(x=40, y=65)

        self.result = Entry(self.window,font=("Helvetica",20,"bold","italic"),fg="red",
                            bg="white",state="disable",textvar=self.text_value)
        self.result.place(x=140,y=65)



        self.butn()
        self.take_input()


    def take_input(self):
        self.number1_name = Label(self.window, text="Number 1: ",width=8, font=("arial", 16, "bold",
                                                                                "italic"),fg="blue")
        self.number1_name.place(x=10, y=170)

        self.number1 = Entry(self.window,width=8,bg="white",font=("arial",20,"bold","italic"),fg="grey")
        self.number1.place(x=125,y=170)

        self.number1.focus()

        self.number2_name = Label(self.window, text="Number 2: ", width=8, font=("arial", 16, "bold", "italic"),
                                  fg="blue")
        self.number2_name.place(x=340, y=170)

        self.number2 = Entry(self.window, width=8, bg="white", font=("arial", 20, "bold", "italic"),fg="grey")
        self.number2.place(x=455, y=170)

        self.operator_name = Label(self.window, text="Operator:", width=12, font=("arial", 17, "bold", "italic"),
                                  fg="brown")
        self.operator_name.place(x=100, y=115)

        self.operator = Entry(self.window, width=12, bg="white", font=("arial", 20, "bold", "italic"),
                              fg="grey",state="disable",textvar=self.textoperator)
        self.operator.place(x=250, y=117)


    def pi_val(self):
        messagebox.showinfo("Value of pi","The value of pi is: 3.14159265")
    def reset_now(self):
        self.textoperator.set(" ")
        self.text_value.set(" ")
    def tata(self):
        self.decision = messagebox.askyesno("Conformation","Do you want to exit right now?")
        if self.decision>0:
            window.destroy()
        else:
            pass



    def information(self):
        self.window_information = Tk()
        self.window_information.title("Information")
        self.window_information.geometry("500x400")
        self.window_information.maxsize(500,400)
        self.window_information.minsize(500,400)

        self.point1 = Label(self.window_information,fg="blue",font=("arial",11,"bold","italic"),
                            text="1.Write number and select operator at first, then click on equal(=) sign.")
        self.point1.place(x=5,y=15)

        self.point2 = Label(self.window_information, fg="blue", font=("arial", 12, "bold", "italic"),
                            text="2.For single digit operation(e.g. rad,exponent,Reciprocal(1/x),")

        self.point2.place(x=5, y=50)

        self.point2_continue1 = Label(self.window_information, fg="blue", font=("arial", 12, "bold", "italic"),
                            text="square,cube,square root,cube root,log,factorial(n!),exponent etc.)")

        self.point2_continue1.place(x=5, y=70)

        self.point2_continue2 = Label(self.window_information, fg="blue", font=("arial", 12, "bold", "italic"),
                                     text="only write number input in the 'Number1' but not write ")

        self.point2_continue2.place(x=5, y=90)

        self.point2_continue3 = Label(self.window_information, fg="blue", font=("arial", 12, "bold", "italic"),
                                      text="input in 'Number2' .After that select favourable operator and go.")

        self.point2_continue3.place(x=5, y=110)

        self.last = Label(self.window_information, fg="green", font=("arial", 15, "bold", "italic"),
                            text="Best of luck!")
        self.last.place(x=180, y=200)

        self.point3 = Label(self.window_information, fg="blue", font=("arial", 12, "bold", "italic"),
                            text="3.For single no. operation,if there is present two no. in 'Number1'")
        self.point3.place(x=5, y=140)

        self.point3_continue = Label(self.window_information, fg="blue", font=("arial", 12, "bold", "italic"),
                            text="and 'Number2', only input number in 'Number1' will taken.")
        self.point3_continue.place(x=5, y=160)

        self.window_information.mainloop()

    def opr(self,work):
        self.work = work
        self.textoperator.set(self.work)


    def evaluation_opr(self):
        self.n1 = (self.number1.get())
        self.n2 = (self.number2.get())
        self.work_done = self.textoperator.get()
        print("n1 is: ",self.n1)
        print("n2 is: ",self.n2)
        print(self.work_done)
        if self.work_done=="+":
            try:
               self.text_value.set(eval(self.n1)+eval(self.n2))

            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="-":
            try:
               self.text_value.set(eval(self.n1)-eval(self.n2))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="X":
            try:
               self.text_value.set(eval(self.n1)*eval(self.n2))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="/":
            try:
               self.text_value.set(eval(self.n1)/eval(self.n2))
            except ZeroDivisionError:
                self.text_value.set("Can not divide by zero")
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()

        elif self.work_done=="Reciprocal":
            try:
                self.text_value.set(round(1.0/eval(self.n1),2))
            except ZeroDivisionError:
                self.text_value.set("Can not divide by zero")

            except:
                messagebox.showerror("Input Error","Please write number in the right position.Please read the information carefully")
                self.information()
                self.reset_now()


        elif self.work_done=="Square":
            try:
               self.text_value.set(eval(self.n1) ** 2.0)
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="Cube":
            try:
               self.text_value.set(eval(self.n1) ** 3.0)
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="Square root":
            try:
               self.text_value.set(eval(self.n1)**0.5)
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "Cube root":
            try:
               self.text_value.set(eval(self.n1)**(1/3))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()

        elif self.work_done == "Exponent":
            try:
               self.text_value.set(math.exp(eval(self.n1)))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="x^y":
            try:
               self.text_value.set(eval(self.n1) ** eval(self.n2))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="Factorial":
            try:

                for i in range(1,eval(self.n1)+1):
                    self.fact= self.fact * i

                self.text_value.set(self.fact)

                self.fact=1
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="lcm":
            try:
                if eval(self.n1)>eval(self.n2):
                   self.text_value.set((eval(self.n1)*eval(self.n2))/math.gcd(eval(self.n1),eval(self.n2)))
                else:
                   self.text_value.set((eval(self.n2)*eval(self.n1))/math.gcd(eval(self.n2),eval(self.n1)))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done=="hcf":
            try:
                if eval(self.n1) > eval(self.n2):
                   self.text_value.set(math.gcd(eval(self.n1),eval(self.n2)))
                else:
                    self.text_value.set(math.gcd(eval(self.n2), eval(self.n1)))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "log2":
            try:
                self.text_value.set(math.log2(eval(self.n1)))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "log10":
            try:
                self.text_value.set(math.log10(eval(self.n1)))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "Modulus":
            try:
                self.text_value.set(eval(self.n1)%eval(self.n2))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "Radian":
            try:
                self.text_value.set(round(math.radians(eval(self.n1)),3))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "sin":
            try:
                self.text_value.set(round(math.sin(math.radians(eval(self.n1))),1))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "cos":
            try:
                self.text_value.set(round(math.cos(math.radians(eval(self.n1))),1))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "tan":
            try:
                if eval(self.n1) == 90:
                    self.text_value.set("Infinite")
                else:
                    self.text_value.set(round(math.tan(math.radians(eval(self.n1))),1))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        elif self.work_done == "cot":
            try:
                if eval(self.n1) == 0:
                    self.text_value.set("Infinite")
                else:
                    self.text_value.set(round(1/(math.tan(math.radians(eval(self.n1)))),1))
            except:
                messagebox.showerror("Error","Something error in input.please check it.")
                self.information()
                self.reset_now()
        else:
            messagebox.showerror("Error","Please read the information carefully at first.")
            self.information()
            self.reset_now()


        self.number1.focus()








if __name__ == '__main__':
    window = Tk()
    window.title("Smart Scientific Calculator")
    window.geometry("600x600")
    window.maxsize(600,600)
    window.minsize(600,600)
    but(window)
    window.mainloop()
