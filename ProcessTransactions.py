import csv
filename='SampleTransCG4.csv'
def Get_Trans(filename):
	csv_file=open(filename) 
	Trans = csv.reader(csv_file)
	return Trans

def Get_Keys(Trans):
	UniqID = set()
	for k,v in Trans:
		UniqID.add(k)
	return UniqID	

def Get_Values(PurchaseID):
	Values=[]
	Trans=Get_Trans(filename)
	for k,v in Trans:
		if k==PurchaseID:
			Values.append(v)
	#print Values
	return Values		

def Write_to_CSV(LofL):
	with open("SampleOutput.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(LofL)

def main(filename):
	LofL = []
	Trans=Get_Trans(filename)
	Uniq=Get_Keys(Trans)
	for i in Uniq:
		values=Get_Values(i)
		LofL.append(values)
	Write_to_CSV(LofL)	

main(filename)