from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tempfile, os
import EmployeeDatabase

#Frontend

class Employee:
  
	def __init__(self,root):
		self.root = root
		self.root.title("Employee Database Management System")
		self.root.geometry("1350x800+0+0")
		self.root.configure(bg="Gainsboro")

		MainFrame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE)
		MainFrame.grid()

		TopFrame1 = Frame(MainFrame, bd=7, width=1340, height=100, relief=RIDGE)
		TopFrame1.grid(row=2,column = 0)

		TopFrame2 = Frame(MainFrame, bd=7, width=1340, height=150, relief=RIDGE)
		TopFrame2.grid(row=1,column = 0)

		TopFrame3 = Frame(MainFrame, bd=7, width=1340, height=600, relief=RIDGE)
		TopFrame3.grid(row=0,column = 0)

		LeftFrame = Frame(TopFrame3, bd=5, width=1340, height=400, padx=2,bg="Gainsboro", relief=RIDGE)
		LeftFrame.pack(side=LEFT)
		LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2,bg="Gainsboro", relief=RIDGE)
		LeftFrame1.pack(side=TOP)
		
		LeftFrame2 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2,bg="Gainsboro", relief=RIDGE)
		LeftFrame2.pack(side=TOP)
		LeftFrame2Left = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2,bg="Gainsboro", relief=RIDGE)
		LeftFrame2Left.pack(side=LEFT)
		LeftFrame2Right = Frame(LeftFrame2, bd=5, width=300, height=170, padx=2,bg="Gainsboro", relief=RIDGE)
		LeftFrame2Right.pack(side=RIGHT)

		RightFrame1 = Frame(TopFrame3, bd=5, width=320, height=400, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame1.pack(side=RIGHT)

		RightFrame1a = Frame(RightFrame1, bd=5, width=310, height=300, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame1a.pack(side=TOP)

		RightFrame2 = Frame(TopFrame3, bd=5, width=300, height=400, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame2.pack(side=RIGHT)

		RightFrame2a = Frame(RightFrame2, bd=5, width=280, height=50, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame2a.pack(side=TOP)

		RightFrame2b = Frame(RightFrame2, bd=5, width=280, height=180, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame2b.pack(side=TOP)
		
		RightFrame2c = Frame(RightFrame2, bd=5, width=280, height=100, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame2c.pack(side=TOP)
		
		RightFrame2d = Frame(RightFrame2, bd=5, width=280, height=50, padx=2,bg="Gainsboro", relief=RIDGE)
		RightFrame2d.pack(side=TOP)

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxVARIABLESxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		
		Firstname = StringVar()
		Surname = StringVar()
		Address = StringVar()
		Reference = StringVar()
		Surname = StringVar()
		CityWeighting = IntVar()
		Mobile = StringVar()
		BasicSalary = IntVar()
		OverTime = StringVar()
		GrossPay = StringVar()
		NetPay = StringVar()
		Tax = StringVar()
		Pension = StringVar()
		StdLoan = StringVar()
		NIPayment = StringVar()
		Deductions = StringVar()
		Gender = StringVar()
		Payday = StringVar()
		Taxperiod = StringVar()
		NINumber = StringVar()
		NICode = StringVar()        
		TaxablePay = StringVar()
		PensionablePay = StringVar()
		OtherPaymentDue = StringVar()
		TaxCode = StringVar()


		CityWeighting.set("")
		BasicSalary.set("")
		OtherPaymentDue.set("0.00")

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxFUNCTIONSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
		
		def addData():
			if(len (Reference.get())!=0):
				EmployeeDatabase.addEmployeeRec(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(), 
				Mobile.get(), NINumber.get(), StdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get())
				lstEmployee.delete(0,END)
				lstEmployee.insert(END,(Reference.get(), Firstname.get(), Surname.get(), Address.get(), Gender.get(), 
							Mobile.get(), NINumber.get(), StdLoan.get(), Tax.get(), Pension.get(), Deductions.get(), NetPay.get(), GrossPay.get()))

		def DisplayData():
			lstEmployee.delete(0,END)
			for row in EmployeeDatabase.viewData():
				lstEmployee.insert(END, row, str(""))

		def EmployeeRec(event):

			searchEd = lstEmployee.curselection()[0]
			Ed = lstEmployee.get(searchEd) 

			self.txtReference.delete(0,END)
			self.txtReference.insert(END, Ed[1])
			self.txtFirstname.delete(0,END)
			self.txtFirstname.insert(END, Ed[2])
			self.txtSurname.delete(0,END)
			self.txtSurname.insert(END, Ed[3])
			self.txtAddress.delete(0,END)
			self.txtAddress.insert(END, Ed[4])
			self.txtGender.delete(0,END)
			self.txtGender.insert(END, Ed[5])
			self.txtMobile.delete(0,END)
			self.txtMobile.insert(END, Ed[6])
			self.txtNINumber.delete(0,END)
			self.txtNINumber.insert(END, Ed[7])
			self.txtStdLoan.delete(0,END)
			self.txtStdLoan.insert(END, Ed[8])
			self.txtTax.delete(0,END)
			self.txtTax.insert(END, Ed[9])
			self.txtPension.delete(0,END)
			self.txtPension.insert(END, Ed[10])
			self.txtDeductions.delete(0,END)
			self.txtDeductions.insert(END, Ed[11])
			self.txtNetPay.delete(0,END)
			self.txtNetPay.insert(END, Ed[12])
			self.txtGrossPay.delete(0,END)
			self.txtGrossPay.insert(END, Ed[13])

		


		
		def Reset():
			Firstname.set(" ")
			Surname.set(" ")
			Address.set(" ")
			Reference.set(" ")
			Surname.set(" ")
			CityWeighting.set(" ")
			Mobile.set(" ")
			BasicSalary.set(" ")
			OverTime.set(" ")
			GrossPay.set(" ")
			NetPay.set(" ")
			Tax.set(" ")				
			Pension.set(" ")
			StdLoan.set(" ")
			NIPayment.set(" ")
			Deductions.set(" ")
			Gender.set(" ")
			Payday.set(" ")
			Taxperiod.set(" ")
			NINumber.set(" ") 
			NICode.set(" ")
			TaxablePay.set(" ")
			PensionablePay.set(" ")
			TaxCode.set(" ")
			OtherPaymentDue.set("0.00")
			self.txtReceipt.delete("1.0",END)

		def iQuit():
			iQuit = tkinter.messagebox.askyesno("EMPLOYEE DATABASE SYSTEM","ARE YOU SURE \n\nYOU WANT TO EXIT ?")
			if iQuit > 0:
				root.destroy()
				return

		def PayRef():
			Payday.set(time.strftime("%d/%m/%y"))
			Refday = random.randint(16462,708488)
			Refpaid = ("Ref" + str(Refday))
			Reference.set(Refday)

			NIpay = random.randint(34501,409765)
			NIpaid = ("NI" + str(NIpay))
			NINumber.set(NIpay)

			iDate = datetime.datetime.now() 
			Taxperiod. set (iDate.month)

			NCode = random.randint (1290, 13123) 
			CodeNI = ("NIC" + str (NCode)) 
			NICode. set (CodeNI)

			iTaxCode = random. randint (7589, 15875)
			PaymentTaxCode = ("TCode" + str (iTaxCode)) 
			TaxCode. set (PaymentTaxCode)  

		def MonthlySalary():
			PayRef()

			BS = float (BasicSalary.get())
			CW = float (CityWeighting.get())
			OT = float (OverTime.get())
			OPD = float (OtherPaymentDue.get())

			MTax = ((BS + CW + OT + OPD) * 0.3)
			TTax = str('%.2f'% (MTax) )
			Tax.set (TTax) 
			
			M_Pension = ( (BS + CW + OT + OPD) * 0.02) 
			MM_Pension = str('%.2f' % (M_Pension) )
			Pension.set(MM_Pension)

			M_StdLoan = ((BS + CW + OT + OPD) * 0.012) 
			MM_StdLoan = str('%.2f' % (M_StdLoan))
			StdLoan. set (MM_StdLoan)

			M_NIPayment = ( (BS + CW + OT + OPD) * 0.011) 
			MM_NIPayment = str('%.2f' % (M_NIPayment)) 
			NIPayment.set (MM_NIPayment)

			Deduct = (MTax + M_Pension + M_StdLoan + M_NIPayment)
			Deduct_Payment = str('%.2f' % (Deduct))
			Deductions.set (Deduct_Payment)

			Gross_Pay = str('%.2f' % (BS+ CW + OT + OPD)) 
			GrossPay.set(Gross_Pay)

			NetPayAfter = (BS + CW + OT + OPD) - Deduct 
			NetAfter = str("%.2f" % (NetPayAfter))
			NetPay.set (NetAfter)

			TaxablePay.set (TTax) 
			PensionablePay.set (MM_Pension)

			self.txtReceipt.insert (END, '\t\t Monthly Pay Slip' + "\n\n") 
			self.txtReceipt.insert (END, 'Reference: \t\t\t'+ Reference.get() +"\n") 
			self.txtReceipt.insert (END, 'PayDay: \t\t\t'+ Payday.get() +"\n") 
			self.txtReceipt.insert (END, 'Surname: \t\t\t'+ Surname.get()+"\n")
			self.txtReceipt.insert (END, 'FirstName: \t\t\t'+ Firstname.get()+"\n\n") 
			self.txtReceipt.insert (END, 'Tax: \t\t\t' + Tax.get()+"\n") 
			self.txtReceipt.insert (END, 'Pension: \t\t\t' + Pension.get()+"\n") 
			self.txtReceipt.insert (END, 'Student Loan: \t\t\t' + StdLoan.get()+"\n") 
			self.txtReceipt.insert (END, 'NI Number: \t\t\t' + NINumber.get() + "\n") 
			self.txtReceipt.insert (END, 'NI Payment: \t\t\t' + NIPayment.get() + "\n") 

			self.txtReceipt.insert (END, 'Deductions: ititle' + Deductions.get()+"\n") 
			self.txtReceipt.insert (END, 'City Weighting: \t\t\t' + str('%.2f' %(CityWeighting.get())) + "\n") 
			
			self.txtReceipt.insert (END, '\nTax Paid: \t\t\t' + str( '%.2f' %(BasicSalary .get())) + "\n") 
			self.txtReceipt.insert (END, 'OverTime:\t\t\t'+ OverTime.get()+"\n") 
			self.txtReceipt.insert (END, 'NetPay: \t\t\t' + NetPay.get()+"\n") 
			self.txtReceipt.insert (END, 'GrossPay: \t\t\t' + GrossPay.get()+"\n") 
			addData()

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxRECEIPTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		self.txtReceipt = Text(RightFrame1a, height=23, width=32, bd=10, font=('arial',9,'bold'))
		self.txtReceipt.grid(row=0, column=0)
		
		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		self.lblLabel = Label(TopFrame2, font=('arial',10,'bold'),padx=6,pady=2,
                text="Reference\tFirstname\tSurname\tAddress\t\tGender\tMobile\tNI Number\tStudent loan\tTax\tPension\
                                    Deductions\tNet pay\t\tGross pay")
		self.lblLabel.grid(row=0, column=0, columnspan=17)
		
		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxListbox and scrollbarxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		scrollbar = Scrollbar(TopFrame2)
		scrollbar.grid(row=1, column=1, sticky ='ns')

		lstEmployee = Listbox(TopFrame2, width = 145, height=5, font=('arial',12,'bold'), yscrollcommand=Scrollbar.set)
		lstEmployee.bind('<<ListBoxSelect>>',EmployeeRec)
		lstEmployee.grid(row=1, column=0, padx=1, sticky ='nsew')
		scrollbar.config(command = lstEmployee.xview)

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxwidgetxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		self.lblReference= Label(LeftFrame1, font=('arial',12,'bold'), text="Reference", bd=7, bg="Gainsboro", anchor='w')
		self.lblReference.grid(row=0, column=0, sticky ='w', padx =5)
		self.txtReference= Entry(LeftFrame1, font=('arial',12,'bold'), textvariable=Reference, bd=5, width=60, justify='left')
		self.txtReference.grid(row=0, column=1)

		self.lblFirstname= Label(LeftFrame1, font=('arial',12,'bold'), text="Firstname", bd=7, bg="Gainsboro", anchor='w')
		self.lblFirstname.grid(row=1, column=0, sticky ='w', padx =5)
		self.txtFirstname= Entry(LeftFrame1, font=('arial',12,'bold'), textvariable=Firstname, bd=5, width=60, justify='left')
		self.txtFirstname.grid(row=1, column=1)

		self.lblSurname= Label(LeftFrame1, font=('arial',12,'bold'), text="Surname", bd=7, bg="Gainsboro", anchor='w')
		self.lblSurname.grid(row=2, column=0, sticky ='w', padx =5)
		self.txtSurname= Entry(LeftFrame1, font=('arial',12,'bold'), textvariable=Surname, bd=5, width=60, justify='left')
		self.txtSurname.grid(row=2, column=1)

		self.lblAddress= Label(LeftFrame1, font=('arial',12,'bold'), text="Address", bd=7, bg="Gainsboro", anchor='w')
		self.lblAddress.grid(row=3, column=0, sticky ='w', padx =5)
		self.txtAddress= Entry(LeftFrame1, font=('arial',12,'bold'), textvariable=Address, bd=5, width=60, justify='left')
		self.txtAddress.grid(row=3, column=1)

		self.lblGender= Label(LeftFrame1, font=('arial',12,'bold'), text="Gender", bd=7, bg="Gainsboro", anchor='w')
		self.lblGender.grid(row=4, column=0, sticky ='w', padx =5)
		self.txtGender= Entry(LeftFrame1, font=('arial',12,'bold'), textvariable=Gender, bd=5, width=60, justify='left')
		self.txtGender.grid(row=4, column=1)

		self.lblMobile= Label(LeftFrame1, font=('arial',12,'bold'), text="Mobile", bd=7, bg="Gainsboro", anchor='w')
		self.lblMobile.grid(row=5, column=0, sticky ='w', padx =5)
		self.txtMobile= Entry(LeftFrame1, font=('arial',12,'bold'), textvariable=Mobile, bd=5, width=60, justify='left')
		self.txtMobile.grid(row=5, column=1)

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		self.lblCityWeighting= Label(LeftFrame2Left, font=('arial',12,'bold'), text="Cityweighting", bd=7, bg="Gainsboro", anchor='e')
		self.lblCityWeighting.grid(row=0, column=0, sticky ='w')
		self.txtCityWeighting= Entry(LeftFrame2Left, font=('arial',12,'bold'), textvariable=CityWeighting, bd=5, width=20, justify='left')
		self.txtCityWeighting.grid(row=0, column=1)

		self.lblBasicSalary= Label(LeftFrame2Left, font=('arial',12,'bold'), text="BasicSalary", bd=7, bg="Gainsboro", anchor='w')
		self.lblBasicSalary.grid(row=1, column=0, sticky ='w')
		self.txtBasicSalary= Entry(LeftFrame2Left, font=('arial',12,'bold'), textvariable=BasicSalary, bd=5, width=20, justify='left')
		self.txtBasicSalary.grid(row=1, column=1)

		self.lblOverTime= Label(LeftFrame2Left, font=('arial',12,'bold'), text="OverTime", bd=7, bg="Gainsboro", anchor='w')
		self.lblOverTime.grid(row=2, column=0, sticky ='w')
		self.txtOverTime= Entry(LeftFrame2Left, font=('arial',12,'bold'), textvariable=OverTime, bd=5, width=20, justify='left')
		self.txtOverTime.grid(row=2, column=1)

		self.lblOtherPaymentDue= Label(LeftFrame2Left, font=('arial',12,'bold'), text="OtherPaymentDue", bd=7, bg="Gainsboro", anchor='w')
		self.lblOtherPaymentDue.grid(row=3, column=0, sticky ='w')
		self.txtOtherPaymentDue= Entry(LeftFrame2Left, font=('arial',12,'bold'), textvariable=OtherPaymentDue, bd=5, width=20, justify='left')
		self.txtOtherPaymentDue.grid(row=3, column=1)

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		self.lblTax= Label(LeftFrame2Right, font=('arial',12,'bold'), text="Tax", bd=7, bg="Gainsboro", anchor='e')
		self.lblTax.grid(row=0, column=0, sticky ='w')
		self.txtTax= Entry(LeftFrame2Right, font=('arial',12,'bold'), textvariable=Tax, bd=5, width=20, justify='left')
		self.txtTax.grid(row=0, column=1)

		self.lblPension= Label(LeftFrame2Right, font=('arial',12,'bold'), text="Pension", bd=7, bg="Gainsboro", anchor='w')
		self.lblPension.grid(row=1, column=0, sticky ='w')
		self.txtPension= Entry(LeftFrame2Right, font=('arial',12,'bold'), textvariable=Pension, bd=5, width=20, justify='left')
		self.txtPension.grid(row=1, column=1)

		self.lblStdLoan= Label(LeftFrame2Right, font=('arial',12,'bold'), text="StdLoan", bd=7, bg="Gainsboro", anchor='w')
		self.lblStdLoan.grid(row=2, column=0, sticky ='w')
		self.txtStdLoan= Entry(LeftFrame2Right, font=('arial',12,'bold'), textvariable=StdLoan, bd=5, width=20, justify='left')
		self.txtStdLoan.grid(row=2, column=1)

		self.lblNIPayment= Label(LeftFrame2Right, font=('arial',12,'bold'), text="NIPayment", bd=7, bg="Gainsboro", anchor='w')
		self.lblNIPayment.grid(row=3, column=0, sticky ='w')
		self.txtNIPayment= Entry(LeftFrame2Right, font=('arial',12,'bold'), textvariable=NIPayment, bd=5, width=20, justify='left')
		self.txtNIPayment.grid(row=3, column=1)

		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

		self.lblPayday= Label(RightFrame2a, font=('arial',12,'bold'), text="Payday", bd=7, bg="Gainsboro", anchor='w')
		self.lblPayday.grid(row=0, column=0, sticky ='w')
		self.txtPayday= Entry(RightFrame2a, font=('arial',12,'bold'), textvariable=Payday, bd=5, width=27, justify='left')
		self.txtPayday.grid(row=0, column=1)

		self.lblTaxperiod= Label(RightFrame2b, font=('arial',12,'bold'), text="Taxperiod", bd=7, bg="Gainsboro", anchor='w')
		self.lblTaxperiod.grid(row=0, column=0, sticky ='w')
		self.txtTaxperiod= Entry(RightFrame2b, font=('arial',12,'bold'), textvariable=Taxperiod, bd=5, width=25, justify='left')
		self.txtTaxperiod.grid(row=0, column=1)

		self.lblTaxCode= Label(RightFrame2b, font=('arial',12,'bold'), text="TaxCode", bd=7, bg="Gainsboro", anchor='w')
		self.lblTaxCode.grid(row=1, column=0, sticky ='w')
		self.txtTaxCode= Entry(RightFrame2b, font=('arial',12,'bold'), textvariable=TaxCode, bd=5, width=25, justify='left')
		self.txtTaxCode.grid(row=1, column=1)

		self.lblNINumber= Label(RightFrame2b, font=('arial',12,'bold'), text="NINumber", bd=7, bg="Gainsboro", anchor='w')
		self.lblNINumber.grid(row=2, column=0, sticky ='w')
		self.txtNINumber= Entry(RightFrame2b, font=('arial',12,'bold'), textvariable=NINumber, bd=5, width=25, justify='left')
		self.txtNINumber.grid(row=2, column=1)

		self.lblNICode= Label(RightFrame2b, font=('arial',12,'bold'), text="NICode", bd=7, bg="Gainsboro", anchor='w')
		self.lblNICode.grid(row=3, column=0, sticky ='w')
		self.txtNICode= Entry(RightFrame2b, font=('arial',12,'bold'), textvariable=NICode, bd=5, width=25, justify='left')
		self.txtNICode.grid(row=3, column=1)

		self.lblTaxablePay= Label(RightFrame2c, font=('arial',12,'bold'), text="TaxablePay", bd=7, bg="Gainsboro", anchor='w')
		self.lblTaxablePay.grid(row=0, column=0, sticky ='w')
		self.txtTaxablePay= Entry(RightFrame2c, font=('arial',12,'bold'), textvariable=TaxablePay, bd=5, width=20, justify='left')
		self.txtTaxablePay.grid(row=0, column=1)

		self.lblPensionablePay= Label(RightFrame2c, font=('arial',12,'bold'), text="PensionablePay", bd=7, bg="Gainsboro", anchor='w')
		self.lblPensionablePay.grid(row=1, column=0, sticky ='w')
		self.txtPensionablePay= Entry(RightFrame2c, font=('arial',12,'bold'), textvariable=PensionablePay, bd=5, width=20, justify='left')
		self.txtPensionablePay.grid(row=1, column=1)

		self.lblNetPay= Label(RightFrame2d, font=('arial',12,'bold'), text="NetPay", bd=7, bg="Gainsboro", anchor='w')
		self.lblNetPay.grid(row=0, column=0, sticky ='w')
		self.txtNetPay= Entry(RightFrame2d, font=('arial',12,'bold'), textvariable=NetPay, bd=5, width=25, justify='left')
		self.txtNetPay.grid(row=0, column=1)

		self.lblGrossPay= Label(RightFrame2d, font=('arial',12,'bold'), text="GrossPay", bd=7, bg="Gainsboro", anchor='w')
		self.lblGrossPay.grid(row=1, column=0, sticky ='w')
		self.txtGrossPay= Entry(RightFrame2d, font=('arial',12,'bold'), textvariable=GrossPay, bd=5, width=25, justify='left')
		self.txtGrossPay.grid(row=1, column=1)

		self.lblDeductions= Label(RightFrame2d, font=('arial',12,'bold'), text="Deductions", bd=7, bg="Gainsboro", anchor='w')
		self.lblDeductions.grid(row=2, column=0, sticky ='w')
		self.txtDeductions= Entry(RightFrame2d, font=('arial',12,'bold'), textvariable=Deductions, bd=5, width=25, justify='left')
		self.txtDeductions.grid(row=2, column=1)
		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
		
		self.btnAddNewTotal= Button(TopFrame1, bd=4, fg= "black", font=('arial',16,'bold'), padx=30,
							 width=15,text="AddNew/Total", command= MonthlySalary).grid(row=0, column=0, padx=1)

		

		self.btnDisplay= Button(TopFrame1, bd=4, fg= "black", font=('arial',16,'bold'), padx=30,
							 width=15,text="Display", command= DisplayData).grid(row=0, column=2, padx=1)

		

		self.btnReset= Button(TopFrame1, bd=4, fg= "black", font=('arial',16,'bold'), padx=30,
							 width=15,text="Reset", command= Reset).grid(row=0, column=6, padx=1)

		self.btnExit= Button(TopFrame1, bd=4, fg= "black", font=('arial',16,'bold'), padx=30,
							 width=15,text="Exit", command = iQuit).grid(row=0, column=7, padx=1)
		#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx5xxxxxxxxxxx

if __name__=='__main__':
	Ed = []
	root = Tk()
	application = Employee(root)
	root.mainloop()
