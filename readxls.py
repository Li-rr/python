import xlrd 
import numpy
import matplotlib.pyplot as plt
#from pyExcelerator import *
fname = "school.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("1")
except:
    print "no sheet in  %s named Sheet1" %fname

nrows = sh.nrows
ncols = sh.ncols

weight_list = []
height_list = []
print "nrows %d, ncols %d" %(nrows,ncols)
for i in range(2,nrows):
    sex = sh.cell(i,7).value
    if(sex==2):
       cell_weight = sh.cell(i,11).value
       cell_height = sh.cell(i,10).value
       print "%s %s"%(cell_weight,cell_height)
       weight_list.append(cell_weight)
       height_list.append(cell_height)


#plt.plot(weight_list,height_list)
#plt.xlabel('weight')
#plt.ylabel('height')
#plt.title('HFNU girls weight and height')
#plt.yticks([140,150,160,170,180])
#plt.xticks([30,40,50,60,70,80])
plt.hist(weight_list,bins = 6)
plt.xlabel('weight')
plt.ylabel('girls number')
plt.show()
plt.hist(height_list,bins = 6)
plt.xlabel('height')
plt.ylabel('girls number')
plt.show()
