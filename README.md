# RPN-Calculator
This is a simple RPN Calculator I made using Tkinter
It works by loading values into registers R0 and R1 and then clicking on an operation button from the INPUT panel.  
To operate, enter a number into R0 and then click the Arrow Up Button to transfer the number to the R1 register.  Then, the second number
can be entered (upon transfer of the value to R1, the R0 Register is cleared and ready to accept the second value).  The user can then 
select the mathematical operator or press the Up Arrow Button again, which will transfer the value in R1 into R2 as well as move the value 
in R0 to R1.  At this point a new value can be entered into R0.  Operations will only be performed on the values in R0 and R1 and as such, 
the result will be displayed in R0 and the R1 Register will be cleared.  The value in R2 will be static (it will not cascade to R1) and 
will have to be moved into R1 using the Down Arrow Button in order to interact with the resultant value now in R0.  Please note that, 
if the registers contain values and the Down Arrow Button is pushed, the value in the upper register will replace the value in the register
below it.  I have debated as to whether to change this behavior but I currently like having this type of control over the registers.
