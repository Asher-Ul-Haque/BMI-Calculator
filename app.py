#IMPORTS
import customtkinter as ctk
#-----------------------------------------------------------------------------------------------------------------------



#COLORS AND FONTS
backColor='#50BFAB'
lightGrey='#DDDDDD'
darkGrey='#EEEEEE'
red='#F00'
green='#0F0'
sortOfGreen= '#73FF00'
sortOfRed= '#FF5500'
orange= '#FF9100'
lime= '#AAFF00'
yellowReddish= '#FFBB00'
yellowGreenish= '#BBFF00'

basicFont=('Cambria', 15, 'bold')
bigFont=('Segoe UI', 120, 'bold')
#-----------------------------------------------------------------------------------------------------------------------



#SETTING UP THE ROOT-
root=ctk.CTk(fg_color=backColor)
root.geometry('500x400')
root.minsize(500, 400)
root.maxsize(600,480)
ctk.set_appearance_mode('light')
#-----------------------------------------------------------------------------------------------------------------------



#VARIABLES
unitSystem=ctk.StringVar()
bmi=ctk.DoubleVar()
weight=ctk.DoubleVar()
weightDisplay=ctk.StringVar()
height=ctk.DoubleVar()

unitSystem.set('')
bmi.set(22.2)
weight.set(50.0)
height.set(150.0)
#-----------------------------------------------------------------------------------------------------------------------



#SETTING UP THE GRID-
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)
root.rowconfigure((2,3), weight=2, uniform='a')
root.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='a')
#-----------------------------------------------------------------------------------------------------------------------



#FUNCTIONS TO UPDATE EVERYTHING
def changeColor():
    color=green
    if bmi.get()<16.0 or bmi.get()>40.0:
        color=red
    elif 16.0<bmi.get()<17.0 or 35.0<bmi.get()<40.0:
        color=sortOfRed
    elif 17.0<bmi.get()<17.5 or 32.0<bmi.get()<35.0:
        color=orange
    elif 17.5<bmi.get()<18.0 or 25.0<bmi.get()<=32.0:
        color=yellowReddish
    elif 18.0<bmi.get()<18.5 or 23.0<bmi.get()<25.0:
        color=yellowGreenish
    elif 18.5<bmi.get()<19.0 or 21.0<bmi.get()<23.0:
        color=sortOfGreen
    elif 19.0<bmi.get()<21.0:
        color=green
    else:
        color=green
    bmiLabel.configure(text_color=color)

def convertImperialToMetric(value, type):
    if type=='w':
        return float(value)*0.45
    if type=='h':
        return float(value)*30.48
def updateSystem():
    value_1=height.get()/100
    value_1=value_1**2
    value=(weight.get()/value_1)
    integerValue = int(str(value).split('.')[0])
    decimalValue = float('.' + str(value).split('.')[1][0])
    finalValue = integerValue + decimalValue
    bmi.set(finalValue)
    bmiLabel.configure(text=str(bmi.get()))
    changeColor()

def updateWeight():
    integerValue = int(str(weight.get()).split('.')[0])
    decimalValue = float('.'+str(weight.get()).split('.')[1][:2])
    if decimalValue==0.79:
        decimalValue=0.8
    elif decimalValue==0.89:
        decimalValue=0.9
    elif decimalValue==0.99:
        decimalValue=1.0
    elif decimalValue==0.09:
        decimalValue=0.1
    elif decimalValue==0.29:
        decimalValue=0.3
    finalValue = (integerValue + decimalValue)
    weight.set(finalValue)
    weightLabel.configure(text=f'{weight.get()} kg')
    updateSystem()

def updateHeight(value):
    integerValue = int(str(value).split('.')[0])
    decimalValue = float('.'+str(value).split('.')[1][0])
    finalValue=integerValue+decimalValue
    height.set(finalValue)
    heightLabel.configure(text=f'{height.get()} cm')
    updateSystem()
#-----------------------------------------------------------------------------------------------------------------------



#BUTTON TO SWITCH FROM METRIC TO IMPERIAL
unitSystemButton=ctk.CTkButton(textvariable=unitSystem,
                               fg_color=backColor,
                               bg_color='transparent',
                               hover_color=backColor,
                               text_color=darkGrey,
                               master=root,
                               font=basicFont,
                               anchor='e')

unitSystemButton.grid(row=0, column=8, columnspan=2, sticky='nse')
#-----------------------------------------------------------------------------------------------------------------------



#LABEL TO DISPLAY THE CALCULATED BMI
bmiLabel=ctk.CTkLabel(bg_color='transparent',
                      master=root,
                      text_color=green,
                      font=bigFont,
                      text=str(bmi.get()))

bmiLabel.grid(row=1, column=0, columnspan=10, sticky='news')
#-----------------------------------------------------------------------------------------------------------------------



#THE TWO FRAMES
weightFrame=ctk.CTkFrame(master=root, width=480, corner_radius=5, height=50, fg_color='white')
heightFrame=ctk.CTkFrame(master=root, width=480, corner_radius=5, height=50, fg_color='white')
weightFrame.grid(row=2, column=0, columnspan=10)
heightFrame.grid(row=3, column=0, columnspan=10)
#-----------------------------------------------------------------------------------------------------------------------



#WEIGHT
#    WEIGHT LABEL
weightLabel=ctk.CTkLabel(bg_color='white',
                      master=root,
                      text_color='black',
                      font=basicFont,
                      text=f'{weight.get()} kg',
                      anchor='center',
                      height=45)

weightLabel.place(x=230, y=265)

#WEIGHT FUNCTIONS
def subtractDecimal():
    weight.set(weight.get()-0.1)
    updateWeight()

def addDecimal():
    weight.set(weight.get()+0.1)
    updateWeight()

def subtractInteger():
    weight.set(weight.get() - 1.0)
    updateWeight()

def addInteger():
    weight.set(weight.get() + 1.0)
    updateWeight()

#   WEIGHT SUBTRACT BUTTONS
bigSubtract=ctk.CTkButton(master=root,
                          text='-',
                          font=basicFont,
                          corner_radius=4,
                          bg_color='white',
                          fg_color=lightGrey,
                          text_color='black',
                          hover_color='#D5D5D5',
                          height=35,
                          width=75,
                          command=subtractInteger)

smallSubtract=ctk.CTkButton(master=root,
                            text='-',
                            font=basicFont,
                            corner_radius=4,
                            bg_color='white',
                            fg_color=lightGrey,
                            text_color='black',
                            hover_color='#D5D5D5',
                            height=30,
                            width=50,
                            command=subtractDecimal)

bigSubtract.place(x=70, y=290, anchor='center')
smallSubtract.place(x=170, y=290, anchor='center')

#   WEIGHT ADDITION BUTTONS
bigAddition=ctk.CTkButton(master=root,
                          text='+',
                          font=basicFont,
                          corner_radius=4,
                          bg_color='white',
                          fg_color=lightGrey,
                          text_color='black',
                          hover_color='#D5D5D5',
                          height=35,
                          width=75,
                          command=addInteger)

smallAddition=ctk.CTkButton(master=root,
                            text='+',
                            font=basicFont,
                            corner_radius=4,
                            bg_color='white',
                            fg_color=lightGrey,
                            text_color='black',
                            hover_color='#D5D5D5',
                            height=30,
                            width=50,
                            command=addDecimal)

bigAddition.place(x=430, y=290, anchor='center')
smallAddition.place(x=330, y=290, anchor='center')
#-----------------------------------------------------------------------------------------------------------------------



#HEIGHT
heightSlider=ctk.CTkSlider(root,
                           from_=100,
                           to=200,
                           variable=height,
                           bg_color='white',
                           width=330,
                           fg_color=lightGrey,
                           progress_color=backColor,
                           command=updateHeight)

heightLabel=ctk.CTkLabel(bg_color='white',
                      master=root,
                      text_color='black',
                      font=basicFont,
                      text=f'{height.get()} cm',
                      anchor='center')

heightSlider.place(x=30, y=355)
heightLabel.place(x=410, y=350)
#-----------------------------------------------------------------------------------------------------------------------
#RUN
if __name__ == '__main__':
    root.mainloop()

