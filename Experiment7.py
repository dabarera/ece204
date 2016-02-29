#!/usr/bin/python

import Tkinter
import numpy as np
import numpy

top = Tkinter.Tk()
top.title("ECE204 - Experiment 7 Calculations (" + u"\u0DBB"+u"\u0D82"+ u"\u0D9C" +")")

# Code parameters
num_decimals = 2


# Code to add widgets will go here...
varTitle = Tkinter.StringVar()
labelTitle = Tkinter.Label(top, textvariable = varTitle).grid(row = 0, column = 0,columnspan=2)
varTitle.set("Update the measured values")
#labelTitle.pack()

varsubTitle = Tkinter.StringVar()
labelsubTitle = Tkinter.Label(top, textvariable = varsubTitle).grid(row = 1, column = 0,columnspan=2)
varsubTitle.set("Series Resonant Circuit")

Tkinter.Label(top, text = "Units").grid(row = 1, column = 2)

# Experiment 7 Varialbes
var_L = Tkinter.DoubleVar()
var_R = Tkinter.DoubleVar()
var_C = Tkinter.DoubleVar()

# Inductance
label_L = Tkinter.Label(top,text = "L :", justify = Tkinter.LEFT, anchor= Tkinter.W).grid(row = 2, column = 0)
Tkinter.Label(top, text = "mH").grid(row = 2, column = 2)
#label_L.pack(fill = Tkinter.X, pady = 10)
textvar_L = Tkinter.StringVar()
textvar_L.set(22)
text_L = Tkinter.Entry(top, bd = 2, textvariable = textvar_L, justify = Tkinter.RIGHT).grid(row = 2, column = 1)
#text_L.pack(side = Tkinter.RIGHT)
var_L = float(textvar_L.get())/1000

# Resistance
label_R = Tkinter.Label(top,text = "R :",justify = Tkinter.LEFT, anchor= Tkinter.W).grid(row = 3, column = 0)
Tkinter.Label(top, text = u"\u2126").grid(row = 3, column = 2)
textvar_R = Tkinter.StringVar()
textvar_R.set(560)
text_R = Tkinter.Entry(top, bd = 2, textvariable = textvar_R, justify = Tkinter.RIGHT).grid(row = 3, column = 1)
#text_R.pack(side = Tkinter.RIGHT)
var_R = float(textvar_R.get())

# Capacitance
label_C = Tkinter.Label(top,text = "C :" ,justify = Tkinter.LEFT, anchor= Tkinter.W ).grid(row = 4, column = 0)
Tkinter.Label(top, text = u"\u03BC"+ "F").grid(row = 4, column = 2)
textvar_C = Tkinter.StringVar()
textvar_C.set(0.047)
text_C = Tkinter.Entry(top, bd = 2, textvariable = textvar_C, justify = Tkinter.RIGHT).grid(row = 4, column = 1)
#text_C.pack(side = Tkinter.RIGHT)
var_C = float(textvar_C.get())/1000000


#intermediate vals
val_LC = var_L*var_C
val_CR = var_C*var_R
val_sqrt_CRLC = np.sqrt((val_CR)**2 + 4*val_LC)

# Resonant Frequency
label_f0 = Tkinter.Label(top, text= "f" + u"\u2080"+ " :" ,justify = Tkinter.LEFT).grid(row=5, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = 5, column = 2)
textVar_f0 = Tkinter.StringVar()
val_f0 = 1.0/(2*np.pi*np.sqrt(val_LC))
textVar_f0.set(np.round(val_f0,num_decimals))
label_val_f0 = Tkinter.Label(top, textvariable= textVar_f0, justify = Tkinter.RIGHT).grid(row = 5, column = 1)



# Low Half-Power Frequency
label_fL = Tkinter.Label(top, text="f" + u"\u029F"+ " :" ,justify = Tkinter.LEFT).grid(row=6, column = 0)
Tkinter.Label(top, text="Hz").grid(row=6, column = 2)
textVar_fL = Tkinter.StringVar()
val_fL = (val_sqrt_CRLC - val_CR)/(4*np.pi*val_LC)
textVar_fL.set(np.round(val_fL,num_decimals))
label_val_fL = Tkinter.Label(top, textvariable = textVar_fL, justify = Tkinter.RIGHT).grid(row = 6, column = 1)


# High Half-Power Frequency
label_fH = Tkinter.Label(top, text= "f"+ u"\u029C"+ " :" ,justify = Tkinter.LEFT).grid(row=7, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = 7, column = 2)
textVar_fH = Tkinter.StringVar()
val_fH = (val_sqrt_CRLC + val_CR)/(4*np.pi*val_LC)
textVar_fH.set(np.round(val_fH,num_decimals))
label_val_fH = Tkinter.Label(top, textvariable = textVar_fH, justify = Tkinter.RIGHT).grid(row = 7, column = 1)



# Bandwidth
label_BW = Tkinter.Label(top, text= "BW :" ,justify = Tkinter.LEFT).grid(row=8, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = 8, column = 2)
textVar_BW = Tkinter.StringVar()
val_BW = val_fH - val_fL
textVar_BW.set(np.round(val_BW,num_decimals))
label_val_BW = Tkinter.Label(top, textvariable = textVar_BW, justify = Tkinter.RIGHT).grid(row = 8, column = 1)

# Quality Factor
label_QF = Tkinter.Label(top, text= "Q :" ,justify = Tkinter.LEFT).grid(row=9, column = 0)
textVar_QF = Tkinter.StringVar()
val_QF = float(val_f0)/float(val_BW)
textVar_QF.set(np.round(val_QF,num_decimals))
label_val_QF = Tkinter.Label(top, textvariable = textVar_QF, justify = Tkinter.RIGHT).grid(row = 9, column = 1)

# calcSeriesVals Function
def calcSeriesVals():
    var_L = float(textvar_L.get())/1000
    var_R = float(textvar_R.get())
    var_C = float(textvar_C.get())/1000000

    #intermediate vals
    val_LC = var_L*var_C
    val_CR = var_C*var_R
    val_sqrt_CRLC = np.sqrt((val_CR)**2 + 4*val_LC)

    val_f0 = 1.0/(2*np.pi*np.sqrt(val_LC))
    textVar_f0.set(np.round(val_f0,num_decimals))

    val_fL = (val_sqrt_CRLC - val_CR)/(4*np.pi*val_LC)
    textVar_fL.set(np.round(val_fL,num_decimals))

    val_fH = (val_sqrt_CRLC + val_CR)/(4*np.pi*val_LC)
    textVar_fH.set(np.round(val_fH,num_decimals))

    val_BW = val_fH - val_fL
    textVar_BW.set(np.round(val_BW,num_decimals))

    val_QF = float(val_f0)/float(val_BW)
    textVar_QF.set(np.round(val_QF,num_decimals))


# Series Button
b = Tkinter.Button(top, text="Calculate for Series Resonant Circuit Values", command=calcSeriesVals).grid(row = 10, column = 0, columnspan = 2)

row_par = 10

varsubTitle_Par = Tkinter.StringVar()
labelsubTitle_Par = Tkinter.Label(top, textvariable = varsubTitle_Par).grid(row = row_par + 1, column = 0,columnspan=2)
varsubTitle_Par.set("Parallel Resonant Circuit")


# Experiment 7 Varialbes
#var_L = Tkinter.DoubleVar()
var_R_s = Tkinter.DoubleVar()
var_R_p = Tkinter.DoubleVar()
#var_C = Tkinter.DoubleVar()


# Resistance S
label_R_s = Tkinter.Label(top,text = "R"+u"\uA731"+ " :",justify = Tkinter.LEFT ).grid(row = row_par + 2, column = 0)
Tkinter.Label(top, text = "k"+ u"\u2126").grid(row = row_par + 2, column = 2)
textvar_R_s = Tkinter.StringVar()
textvar_R_s.set(3.3)
text_R_s = Tkinter.Entry(top, bd = 2, textvariable = textvar_R_s, justify = Tkinter.RIGHT).grid(row = row_par + 2, column = 1)
var_R_s = float(textvar_R_s.get())*1000


# Resistance P
label_R_p = Tkinter.Label(top,text = "R"+u"\u1D18" + " :",justify = Tkinter.LEFT ).grid(row = row_par + 3, column = 0)
Tkinter.Label(top, text = "k"+ u"\u2126").grid(row = row_par + 3, column = 2)
textvar_R_p = Tkinter.StringVar()
textvar_R_p.set(10)
text_R_p = Tkinter.Entry(top, bd = 2, textvariable = textvar_R_p, justify = Tkinter.RIGHT).grid(row = row_par + 3, column = 1)
#text_R.pack(side = Tkinter.RIGHT)
var_R_p = float(textvar_R_p.get())*1000



#intermediate vals
var_R_sp = float(var_R_s*var_R_p)/(var_R_s + var_R_p)
val_LCR_sp = var_L*var_C*var_R_sp
val_CR_sp = var_C*var_R_sp
val_sqrt_LLCR_sp = np.sqrt(var_L**2 + 4*val_LCR_sp*var_R_sp)

# Resonant Frequency
label_f0_p = Tkinter.Label(top, text= "f" + u"\u2080"+ " :" ,justify = Tkinter.LEFT).grid(row=row_par + 4, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = row_par + 4, column = 2)
label_val_f0_p = Tkinter.Label(top, textvariable= textVar_f0, justify = Tkinter.RIGHT).grid(row = row_par + 4, column = 1)


# Low Half-Power Frequency
label_fL_p = Tkinter.Label(top, text= "f" + u"\u029F"+ " :"  ,justify = Tkinter.LEFT).grid(row=row_par + 5, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = row_par + 5, column = 2)
textVar_fL_p = Tkinter.StringVar()
val_fL_p = (val_sqrt_LLCR_sp - var_L)/(4*np.pi*val_LCR_sp)
textVar_fL_p.set(np.round(val_fL_p,num_decimals))
label_val_fL_p = Tkinter.Label(top, textvariable = textVar_fL_p, justify = Tkinter.RIGHT).grid(row = row_par + 5, column = 1)


# High Half-Power Frequency
label_fH_p = Tkinter.Label(top, text= "f"+ u"\u029C"+ " :" ,justify = Tkinter.LEFT).grid(row=row_par + 6, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = row_par + 6, column = 2)
textVar_fH_p = Tkinter.StringVar()
val_fH_p = (val_sqrt_LLCR_sp + var_L)/(4*np.pi*val_LCR_sp)
textVar_fH_p.set(np.round(val_fH_p,num_decimals))
label_val_fH_p = Tkinter.Label(top, textvariable = textVar_fH_p, justify = Tkinter.RIGHT).grid(row = row_par + 6, column = 1)


# Bandwidth
label_BW_p = Tkinter.Label(top, text= "BW :" ,justify = Tkinter.LEFT).grid(row=row_par + 7, column = 0)
Tkinter.Label(top, text = "Hz").grid(row = row_par + 7, column = 2)
textVar_BW_p = Tkinter.StringVar()
val_BW_p = val_fH_p - val_fL_p
textVar_BW_p.set(np.round(val_BW_p,num_decimals))
label_val_BW_p = Tkinter.Label(top, textvariable = textVar_BW_p, justify = Tkinter.RIGHT).grid(row = row_par + 7, column = 1)

# Quality Factor
label_QF_p = Tkinter.Label(top, text= "Q :" ,justify = Tkinter.LEFT).grid(row=row_par + 8, column = 0)
textVar_QF_p = Tkinter.StringVar()
val_QF_p = float(val_f0)/float(val_BW_p)
textVar_QF_p.set(np.round(val_QF_p,num_decimals))
label_val_QF_p = Tkinter.Label(top, textvariable = textVar_QF_p, justify = Tkinter.RIGHT).grid(row = row_par + 8, column = 1)

# calcParalleVals Function
def calcParVals():
    var_L = float(textvar_L.get())/1000
    var_R_s = float(textvar_R_s.get())*1000
    var_R_p = float(textvar_R_p.get())*1000
    var_C = float(textvar_C.get())/1000000

    #intermediate vals
    var_R_sp = float(var_R_s*var_R_p)/(var_R_s + var_R_p)
    val_LCR_sp = var_L*var_C*var_R_sp
    val_CR_sp = var_C*var_R_sp
    val_sqrt_LLCR_sp = np.sqrt(var_L**2 + 4*val_LCR_sp*var_R_sp)

    val_LC = var_L*var_C
    val_f0 = 1.0/(2*np.pi*np.sqrt(val_LC))
    textVar_f0.set(np.round(val_f0, num_decimals))

    val_fL_p = (val_sqrt_LLCR_sp - var_L)/(4*np.pi*val_LCR_sp)
    textVar_fL_p.set(np.round(val_fL_p,num_decimals))

    val_fH_p = (val_sqrt_LLCR_sp + var_L)/(4*np.pi*val_LCR_sp)
    textVar_fH_p.set(np.round(val_fH_p,num_decimals))

    val_BW_p = val_fH_p - val_fL_p
    textVar_BW_p.set(np.round(val_BW_p,num_decimals))

    val_QF_p = float(val_f0)/float(val_BW_p)
    textVar_QF_p.set(np.round(val_QF_p,num_decimals))


# Series Button
b_p = Tkinter.Button(top, text="Calculate for Parallel Resonant Circuit Values", command=calcParVals).grid(row = row_par + 9, column = 0, columnspan = 2)




top.mainloop()

#top.destroy()