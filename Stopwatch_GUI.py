
# Import necessary packages
import tkinter as tk
import tkinter.font as tf

# Initialise
count = -1
run = False

def temp(mark):
   def value():
      if run:
         global count
         # Just before starting
         if count == -1:
            show = "Starting.."
         else:
            show = str(count)
         mark['text'] = show
         #Increment the count after every one second
         mark.after(1000, value)
         count += 1
   value()

# For Resetting the stopwatch
def Reset(label):
   global count
   count = -1
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Stopwatch!!'
   else:
      mark['text'] = 'Start'
       
# For Starting the stopwatch
def Start(mark):
   global run
   run = True
   temp(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'

# For Stopping the stopwatch
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False



base = tk.Tk()
base.title("STOPWATCH")
base.minsize(width=500, height=500)
mark = tk.Label(base, text="Stopwatch!", fg="blue", font="Helvetica 50 bold")
mark.pack()
myFont = tf.Font(size=20)
start = tk.Button(base, text='Start',height=2, width=20, command=lambda: Start(mark))
start['font'] = myFont
stop = tk.Button(base, text='Stop', height=2, width=20, state='disabled', command=Stop)
stop['font'] = myFont
reset = tk.Button(base, text='Reset',height=2, width=20, state='disabled', command=lambda: Reset(mark))
reset['font'] = myFont
start.pack()
stop.pack()
reset.pack()
base.mainloop()