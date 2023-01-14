from scipy import linalg
import numpy as np
from numpy import loadtxt
import math
from Dtreefunc import *
import pandas as pd

dataset_col = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8' , 'A9','A10', 'A11', 'A12', 'A13', 'A14' , 'A15', 'A16']
dataset = pd.read_csv("data/crx.data", names=dataset_col)
dataset.head()
print(dataset)

dataset = dataset.replace('?',np.nan)

#Preprocess data
#function to fill missing value
def fix_missing_mean(dataset,col):
    #replace missing values with mean 
    dataset[col] = pd.to_numeric(dataset[col], errors = 'coerce')
    dataset[col].fillna(dataset[col].mean(), inplace = True)    

def fix_missing_ffill(dataset, col):
    dataset[col] = dataset[col].fillna(method='ffill')  

#fill missing value by column
fix_missing_ffill(dataset,'A1')
fix_missing_ffill(dataset,'A2')
fix_missing_ffill(dataset,'A4')
fix_missing_ffill(dataset,'A5')
fix_missing_ffill(dataset,'A6')
fix_missing_ffill(dataset,'A7')
fix_missing_mean(dataset,'A14')


#checking
#Are missing values still available?
for i in dataset.columns:
    #print(i)
    if dataset[i].dtype==object:
        print(dataset[i].unique())


M=3 #row

a1=np.zeros(2)
a1CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a2=np.zeros(2) #wait to generate range
a2CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a3=np.zeros(2) #wait for generate range
a3CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a4=np.zeros(4)
a4CI=[[0 for i in range(M)] for j in range(4)] # zero matrix 3 rows 3 columns (class and info gain of age)


a5=np.zeros(3)
a5CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

a6=np.zeros(14)
a6CI=[[0 for i in range(M)] for j in range(14)] # zero matrix 3 rows 3 columns (class and info gain of age)

a7=np.zeros(9)
a7CI=[[0 for i in range(M)] for j in range(9)] # zero matrix 3 rows 3 columns (class and info gain of age)

a8=np.zeros(2)  #wait to generate range
a8CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a9=np.zeros(2)
a9CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a10=np.zeros(2)
a10CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a11=np.zeros(2) #wait to generate range
a11CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a12=np.zeros(2)
a12CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a13=np.zeros(3)
a13CI=[[0 for i in range(M)] for j in range(3)] # zero matrix 3 rows 3 columns (class and info gain of age)

a14=np.zeros(2) #wait to generate change
a14CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a15=np.zeros(2) #wait to generate change
a15CI=[[0 for i in range(M)] for j in range(2)] # zero matrix 3 rows 3 columns (class and info gain of age)

a16=np.zeros(2)

# print(dataset.iloc[0][0])
if (dataset.iloc[0][0] == 'a'): 
    print("YES")
        
    
#วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
for i in range(0,654):
    #A1
    if (dataset.iloc[i][0] == 'b'): 
        a1[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
            a1CI[0][0]+=1 #class +
        else:
            a1CI[0][1]+=1 #class -
    elif(dataset.iloc[0][0] == 'b'): 
        a1[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][0] == 'b') and (dataset.iloc[i][15] == '+'):
            a1CI[1][0]+=1 #class +
        else:
            a1CI[1][1]+=1 #class -

    #A2
    
    ########################################################

    #A3
    
    #######################################################
        
    #A4
    if (dataset.iloc[i][3] == 'u'): 
        a4[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][3] == 'u') and (dataset.iloc[i][15] == '+'):
            a4CI[0][0]+=1 #class +
        else:
            a4CI[0][1]+=1 #class -
    elif(dataset.iloc[i][3] == 'y'): 
        a4[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][3] == 'y') and (dataset.iloc[i][15] == '+'):
            a4CI[1][0]+=1 #class +
        else:
            a4CI[1][1]+=1 #class -
    elif(dataset.iloc[i][3] == 'l'): 
        a4[2]+=1 # total sample tha age <=30
        if (dataset.iloc[i][3] == 'l') and (dataset.iloc[i][15] == '+'):
            a4CI[2][0]+=1 #class +
        else:
            a4CI[2][1]+=1 #class -
    elif(dataset.iloc[i][3] == 't'): 
        a4[3]+=1 # total sample tha age <=30
        if (dataset.iloc[i][3] == 't') and (dataset.iloc[i][15] == '+'):
            a4CI[3][0]+=1 #class +
        else:
            a4CI[3][1]+=1 #class -

    #A5
    if (dataset.iloc[i][4] == 'g'): 
        a5[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][4] == 'g') and (dataset.iloc[i][15] == '+'):
            a5CI[0][0]+=1 #class +
        else:
            a5CI[0][1]+=1 #class -
    elif(dataset.iloc[i][4] == 'p'): 
        a5[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][4] == 'p') and (dataset.iloc[i][15] == '+'):
            a5CI[1][0]+=1 #class +
        else:
            a5CI[1][1]+=1 #class -
    elif(dataset.iloc[i][4] == 'gg'): 
        a5[2]+=1 # total sample tha age <=30
        if (dataset.iloc[i][4] == 'gg') and (dataset.iloc[i][15] == '+'):
            a5CI[2][0]+=1 #class +
        else:
            a5CI[2][1]+=1 #class -

    #A6
    if (dataset.iloc[i][5] == 'c'): 
        a6[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'c') and (dataset.iloc[i][15] == '+'):
            a6CI[0][0]+=1 #class +
        else:
            a6CI[0][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'd'): 
        a6[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'd') and (dataset.iloc[i][15] == '+'):
            a6CI[1][0]+=1 #class +
        else:
            a6CI[1][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'cc'): 
        a6[2]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'cc') and (dataset.iloc[i][15] == '+'):
            a6CI[2][0]+=1 #class +
        else:
            a6CI[2][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'i'): 
        a6[3]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'i') and (dataset.iloc[i][15] == '+'):
            a6CI[3][0]+=1 #class +
        else:
            a6CI[3][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'j'): 
        a6[4]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'j') and (dataset.iloc[i][15] == '+'):
            a6CI[4][0]+=1 #class +
        else:
            a6CI[4][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'k'): 
        a6[5]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'k') and (dataset.iloc[i][15] == '+'):
            a6CI[5][0]+=1 #class +
        else:
            a6CI[5][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'm'): 
        a6[6]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'm') and (dataset.iloc[i][15] == '+'):
            a6CI[6][0]+=1 #class +
        else:
            a6CI[6][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'r'): 
        a6[7]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'r') and (dataset.iloc[i][15] == '+'):
            a6CI[7][0]+=1 #class +
        else:
            a6CI[7][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'q'): 
        a6[8]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'q') and (dataset.iloc[i][15] == '+'):
            a6CI[8][0]+=1 #class +
        else:
            a6CI[8][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'w'): 
        a6[9]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'w') and (dataset.iloc[i][15] == '+'):
            a6CI[9][0]+=1 #class +
        else:
            a6CI[9][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'x'): 
        a6[10]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'x') and (dataset.iloc[i][15] == '+'):
            a6CI[10][0]+=1 #class +
        else:
            a6CI[10][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'e'): 
        a6[11]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'e') and (dataset.iloc[i][15] == '+'):
            a6CI[11][0]+=1 #class +
        else:
            a6CI[11][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'aa'): 
        a6[12]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'aa') and (dataset.iloc[i][15] == '+'):
            a6CI[12][0]+=1 #class +
        else:
            a6CI[12][1]+=1 #class -
    elif(dataset.iloc[i][5] == 'ff'): 
        a6[13]+=1 # total sample tha age <=30
        if (dataset.iloc[i][5] == 'ff') and (dataset.iloc[i][15] == '+'):
            a6CI[13][0]+=1 #class +
        else:
            a6CI[13][1]+=1 #class -

    #A7
    if (dataset.iloc[i][6] == 'v'): 
        a7[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'v') and (dataset.iloc[i][15] == '+'):
            a7CI[0][0]+=1 #class +
        else:
            a7CI[0][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'h'): 
        a7[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'h') and (dataset.iloc[i][15] == '+'):
            a7CI[1][0]+=1 #class +
        else:
            a7CI[1][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'bb'): 
        a7[2]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'bb') and (dataset.iloc[i][15] == '+'):
            a7CI[2][0]+=1 #class +
        else:
            a7CI[2][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'j'): 
        a7[3]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'j') and (dataset.iloc[i][15] == '+'):
            a7CI[3][0]+=1 #class +
        else:
            a7CI[3][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'n'): 
        a7[4]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'n') and (dataset.iloc[i][15] == '+'):
            a7CI[4][0]+=1 #class +
        else:
            a7CI[4][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'z'): 
        a7[5]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'z') and (dataset.iloc[i][15] == '+'):
            a7CI[5][0]+=1 #class +
        else:
            a7CI[5][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'dd'): 
        a7[6]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'dd') and (dataset.iloc[i][15] == '+'):
            a7CI[6][0]+=1 #class +
        else:
            a7CI[6][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'ff'): 
        a7[7]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'ff') and (dataset.iloc[i][15] == '+'):
            a7CI[7][0]+=1 #class +
        else:
            a7CI[7][1]+=1 #class -
    elif (dataset.iloc[i][6] == 'o'): 
        a7[8]+=1 # total sample tha age <=30
        if (dataset.iloc[i][6] == 'o') and (dataset.iloc[i][15] == '+'):
            a7CI[8][0]+=1 #class +
        else:
            a7CI[8][1]+=1 #class -
    
    #A8

    #######################################################33

    #A9
    if (dataset.iloc[i][8] == 't'): 
        a9[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][8] == 't') and (dataset.iloc[i][15] == '+'):
            a9CI[0][0]+=1 #class +
        else:
            a9CI[0][1]+=1 #class -
    elif (dataset.iloc[i][8] == 'f'): 
        a9[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][8] == 'f') and (dataset.iloc[i][15] == '+'):
            a9CI[1][0]+=1 #class +
        else:
            a9CI[1][1]+=1 #class -

    #A10
    if (dataset.iloc[i][9] == 't'): 
        a10[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][9] == 't') and (dataset.iloc[i][15] == '+'):
            a10CI[0][0]+=1 #class +
        else:
            a10CI[0][1]+=1 #class -
    elif (dataset.iloc[i][9] == 'f'): 
        a10[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][9] == 'f') and (dataset.iloc[i][15] == '+'):
            a10CI[1][0]+=1 #class +
        else:
            a10CI[1][1]+=1 #class -

    #A11

    ##################################################

    #A12
    if (dataset.iloc[i][11] == 't'): 
        a12[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][11] == 't') and (dataset.iloc[i][15] == '+'):
            a12CI[0][0]+=1 #class +
        else:
            a12CI[0][1]+=1 #class -
    elif (dataset.iloc[i][11] == 'f'): 
        a12[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][11] == 'f') and (dataset.iloc[i][15] == '+'):
            a12CI[1][0]+=1 #class +
        else:
            a12CI[1][1]+=1 #class -

    #A13
    if (dataset.iloc[i][12] == 'g'): 
        a13[0]+=1 # total sample tha age <=30
        if (dataset.iloc[i][12] == 'g') and (dataset.iloc[i][15] == '+'):
            a13CI[0][0]+=1 #class +
        else:
            a13CI[0][1]+=1 #class -
    elif (dataset.iloc[i][12] == 'p'): 
        a13[1]+=1 # total sample tha age <=30
        if (dataset.iloc[i][12] == 'p') and (dataset.iloc[i][15] == '+'):
            a13CI[1][0]+=1 #class +
        else:
            a13CI[1][1]+=1 #class -
    elif (dataset.iloc[i][12] == 's'): 
        a13[2]+=1 # total sample tha age <=30
        if (dataset.iloc[i][12] == 's') and (dataset.iloc[i][15] == '+'):
            a13CI[2][0]+=1 #class +
        else:
            a13CI[2][1]+=1 #class -

    #A14

    #############################################

    #A15

    ############################################

    #A16
    if (dataset.iloc[i][15] == '+'): 
        a16[0]+=1 # total sample tha age <=30
    elif (dataset.iloc[i][15] == '-'): 
        a16[1]+=1 # total sample tha age <=30



# calculate information gain of dataset and attb
# info D,age,income,stu,credit
info = np.zeros(4)
InD=entropy(a16[1],a16[0])

a1CI[0][2] = entropy(a1CI[0][0],a1CI[0][1])
a1CI[1][2] = entropy(a1CI[1][0],a1CI[1][1])


# a2CI[0][2] = entropy(a2CI[0][0],a2CI[0][1])


# a3CI[0][2] = entropy(a3CI[0][0],a3CI[0][1])


a4CI[0][2] = entropy(a4CI[0][0],a4CI[0][1])
a4CI[1][2] = entropy(a4CI[1][0],a4CI[1][1])
a4CI[2][2] = entropy(a4CI[2][0],a4CI[2][1])
a4CI[3][2] = entropy(a4CI[3][0],a4CI[3][1])


a5CI[0][2] = entropy(a5CI[0][0],a5CI[0][1])
a5CI[1][2] = entropy(a5CI[1][0],a5CI[1][1])
a5CI[2][2] = entropy(a5CI[2][0],a5CI[2][1])


a6CI[0][2] = entropy(a6CI[0][0],a6CI[0][1])
a6CI[1][2] = entropy(a6CI[1][0],a6CI[1][1])
a6CI[2][2] = entropy(a6CI[2][0],a6CI[2][1])
a6CI[3][2] = entropy(a6CI[3][0],a6CI[3][1])
a6CI[4][2] = entropy(a6CI[4][0],a6CI[4][1])
a6CI[5][2] = entropy(a6CI[5][0],a6CI[5][1])
a6CI[6][2] = entropy(a6CI[6][0],a6CI[6][1])
a6CI[7][2] = entropy(a6CI[7][0],a6CI[7][1])
a6CI[8][2] = entropy(a6CI[8][0],a6CI[8][1])
a6CI[9][2] = entropy(a6CI[9][0],a6CI[9][1])
a6CI[10][2] = entropy(a6CI[10][0],a6CI[10][1])
a6CI[11][2] = entropy(a6CI[11][0],a6CI[11][1])
a6CI[12][2] = entropy(a6CI[12][0],a6CI[12][1])
a6CI[13][2] = entropy(a6CI[13][0],a6CI[13][1])


a7CI[0][2] = entropy(a7CI[0][0],a7CI[0][1])
a7CI[1][2] = entropy(a7CI[1][0],a7CI[1][1])
a7CI[2][2] = entropy(a7CI[2][0],a7CI[2][1])
a7CI[3][2] = entropy(a7CI[3][0],a7CI[3][1])
a7CI[4][2] = entropy(a7CI[4][0],a7CI[4][1])
a7CI[5][2] = entropy(a7CI[5][0],a7CI[5][1])
a7CI[6][2] = entropy(a7CI[6][0],a7CI[6][1])
a7CI[7][2] = entropy(a7CI[7][0],a7CI[7][1])
a7CI[8][2] = entropy(a7CI[8][0],a7CI[8][1])


# a8CI[0][2] = entropy(a8CI[0][0],a7CI[0][1])


a9CI[0][2] = entropy(a9CI[0][0],a9CI[0][1])
a9CI[1][2] = entropy(a9CI[1][0],a9CI[1][1])

a10CI[0][2] = entropy(a10CI[0][0],a10CI[0][1])
a10CI[1][2] = entropy(a10CI[1][0],a10CI[1][1])


# a11CI[1][2] = entropy(a10CI[1][0],a10CI[1][1])


a12CI[0][2] = entropy(a12CI[0][0],a12CI[0][1])
a12CI[1][2] = entropy(a12CI[1][0],a12CI[1][1])


a13CI[0][2] = entropy(a13CI[0][0],a13CI[0][1])
a13CI[1][2] = entropy(a13CI[1][0],a13CI[1][1])
a13CI[2][2] = entropy(a13CI[2][0],a13CI[2][1])


# a14CI[2][2] = entropy(a14CI[2][0],a14CI[2][1])


# a15CI[2][2] = entropy(a15CI[2][0],a15CI[2][1])



# หาค่า gain แบบไม่ใช้ และใช้ฟังก์ชัน
"""
การหาแบบไม่ใช้ฟังก์ชัน
Info_A1D = ((a1[0]/690)*a1CI[0][2])+((a1[1]/690)*a1CI[1][2])
print("InfoD A1 is",Info_A1D)
print("A1 Ci [:],[1] is",[a1CI[0][2],a1CI[1][2])
print("InfoD A1 is",Info_A1)
"""

Info_A1 = inforD(a1,[a1CI[0][2],a1CI[1][2]])
Info_A2 = inforD(a2,[a2CI[0][2],a2CI[1][2]]) #waiting
Info_A3 = inforD(a3,[a3CI[0][2],a3CI[1][2]]) #waiting
Info_A4 = inforD(a4,[a4CI[0][2],a4CI[1][2],a4CI[2][2],a4CI[3][2]])
Info_A5 = inforD(a5,[a5CI[0][2],a5CI[1][2],a5CI[2][2]])
Info_A6 = inforD(a6,[a6CI[0][2],a6CI[1][2],a6CI[2][2],a6CI[3][2],a6CI[4][2],a6CI[5][2],a6CI[6][2],a6CI[7][2],a6CI[8][2],a6CI[9][2],a6CI[10][2],a6CI[11][2],a6CI[12][2],a6CI[13][2]])
Info_A7 = inforD(a7,[a7CI[0][2],a7CI[1][2],a7CI[2][2],a7CI[3][2],a7CI[4][2],a7CI[5][2],a7CI[6][2],a7CI[7][2],a7CI[8][2]])
Info_A8 = inforD(a8,[a8CI[0][2],a8CI[1][2]]) #waiting
Info_A9 = inforD(a9,[a9CI[0][2],a9CI[1][2]])
Info_A10 = inforD(a10,[a10CI[0][2],a10CI[1][2]])
Info_A11 = inforD(a11,[a11CI[0][2],a11CI[1][2]]) #waiting
Info_A12 = inforD(a12,[a12CI[0][2],a12CI[1][2]])
Info_A13 = inforD(a13,[a13CI[0][2],a13CI[1][2],a13CI[2][2]])
Info_A14 = inforD(a14,[a14CI[0][2],a14CI[1][2]]) #waiting
Info_A15 = inforD(a15,[a15CI[0][2],a15CI[1][2]]) #waiting


# แสดงผลการทำงานรอบแรก
"""
print("A1 count is", a1)
print("A2 count is",a2)
print("A3 count is",a3)
print("A4 count is",a4)
print("A5 count is", a5)
print("A6 count is",a6)
print("A7 count is", a7)
print("A8 count is", a8)
print("A9 count is", a9)
print("A10 count is", a10)
print("A11 count is", a11)
print("A12 count is", a12)
print("A13 count is", a13)
print("A14 count is", a14)
print("A15 count is", a15)
print("A16 count is", a16)

print("A1 Info relate to class",a1CI)
print("A2 Info relate to class",a2CI)
print("A3 Info relate to class",a3CI)
print("A4 Info relate to class",a4CI)
print("A5 Info relate to class",a5CI)
print("A6 Info relate to class",a6CI)
print("A7 Info relate to class",a7CI)
print("A8 Info relate to class",a8CI)
print("A9 Info relate to class",a9CI)
print("A10 Info relate to class",a10CI)
print("A11 Info relate to class",a11CI)
print("A12 Info relate to class",a12CI)
print("A13 Info relate to class",a13CI)
print("A14 Info relate to class",a14CI)
print("A15 Info relate to class",a15CI)



print("Info(D) is %5.3f" % InD)
print("Info(A1 = b  is %5.3f" % a1CI[0][2])
print("Info(A1 = a  is %5.3f" % a1CI[1][2])

print("Info(A2 =   is %5.3f" % a2CI[0][2])
print("Info(A2 =   is %5.3f" % a2CI[1][2])

print("Info(A3 =   is %5.3f" % a3CI[0][2])
print("Info(A3 =   is %5.3f" % a3CI[1][2])

print("Info(A4 = u  is %5.3f" % a4CI[0][2])
print("Info(A4 = y  is %5.3f" % a4CI[1][2])
print("Info(A4 = l  is %5.3f" % a4CI[2][2])
print("Info(A4 = t  is %5.3f" % a4CI[3][2])

print("Info(A5 = g  is %5.3f" % a5CI[0][2])
print("Info(A5 = p  is %5.3f" % a5CI[1][2])
print("Info(A5 = gg  is %5.3f" % a5CI[2][2])

print("Info(A6 = c  is %5.3f" % a6CI[0][2])
print("Info(A6 = d  is %5.3f" % a6CI[1][2])
print("Info(A6 = cc  is %5.3f" % a6CI[2][2])
print("Info(A6 = i  is %5.3f" % a6CI[3][2])
print("Info(A6 = j  is %5.3f" % a6CI[4][2])
print("Info(A6 = k  is %5.3f" % a6CI[5][2])
print("Info(A6 = m  is %5.3f" % a6CI[6][2])
print("Info(A6 = r  is %5.3f" % a6CI[7][2])
print("Info(A6 = q  is %5.3f" % a6CI[8][2])
print("Info(A6 = w  is %5.3f" % a6CI[9][2])
print("Info(A6 = x  is %5.3f" % a6CI[10][2])
print("Info(A6 = e  is %5.3f" % a6CI[11][2])
print("Info(A6 = aa  is %5.3f" % a6CI[12][2])
print("Info(A6 = ff  is %5.3f" % a6CI[13][2])

print("Info(A7 = v  is %5.3f" % a7CI[0][2])
print("Info(A7 = h  is %5.3f" % a7CI[1][2])
print("Info(A7 = bb  is %5.3f" % a7CI[2][2])
print("Info(A7 = j  is %5.3f" % a7CI[3][2])
print("Info(A7 = n  is %5.3f" % a7CI[4][2])
print("Info(A7 = z  is %5.3f" % a7CI[5][2])
print("Info(A7 = dd  is %5.3f" % a7CI[6][2])
print("Info(A7 = ff  is %5.3f" % a7CI[7][2])
print("Info(A7 = o  is %5.3f" % a7CI[8][2])


print("Info(A8 =   is %5.3f" % a8CI[0][2])  


print("Info(A9 = t  is %5.3f" % a9CI[0][2])
print("Info(A9 = f  is %5.3f" % a9CI[1][2])

print("Info(A10 = t  is %5.3f" % a10CI[0][2])
print("Info(A10 = f  is %5.3f" % a10CI[1][2])


print("Info(A11 =   is %5.3f" % a11CI[0][2])


print("Info(A12 = t  is %5.3f" % a12CI[0][2])
print("Info(A12 = f  is %5.3f" % a12CI[1][2])

print("Info(A13 = g  is %5.3f" % a13CI[0][2])
print("Info(A13 = p  is %5.3f" % a13CI[1][2])
print("Info(A13 = s  is %5.3f" % a13CI[2][2])


print("Info(A14 =   is %5.3f" % a14CI[2][2])


print("Info(A15 =   is %5.3f" % a15CI[2][2])


print("Info A1 (D) is %5.3f" % Info_A1)
print("Info A2 (D) is %5.3f" % Info_A2)
print("Info A3 (D) is %5.3f" % Info_A3)
print("Info A4 (D) is %5.3f" % Info_A4)
print("Info A5 (D) is %5.3f" % Info_A5)
print("Info A6 (D) is %5.3f" % Info_A6)
print("Info A7 (D) is %5.3f" % Info_A7)
print("Info A8 (D) is %5.3f" % Info_A8)
print("Info A9 (D) is %5.3f" % Info_A9)
print("Info A10 (D) is %5.3f" % Info_A10)
print("Info A11 (D) is %5.3f" % Info_A11)
print("Info A12 (D) is %5.3f" % Info_A12)
print("Info A13 (D) is %5.3f" % Info_A13)
print("Info A14 (D) is %5.3f" % Info_A14)
print("Info A15 (D) is %5.3f" % Info_A15)

"""
print("\n***Gain results of all dataset***")
print("InD is %5.3f"% InD)
gainA1=InD-Info_A1
print("Gain (A1) is %5.3f"% gainA1)
gainA2=InD-Info_A2
print("Gain (A2) is %5.3f"% gainA2)
gainA3=InD-Info_A3
print("Gain (A3) is %5.3f"% gainA3)
gainA4=InD-Info_A4
print("Gain (A4) is %5.3f"% gainA4)
gainA5=InD-Info_A5
print("Gain (A5) is %5.3f"% gainA5)
gainA6=InD-Info_A6
print("Gain (A6) is %5.3f"% gainA6)
gainA7=InD-Info_A7
print("Gain (A7) is %5.3f"% gainA7)
gainA8=InD-Info_A8
print("Gain (A8) is %5.3f"% gainA8)
gainA9=InD-Info_A9
print("Gain (A9) is %5.3f"% gainA9)
gainA10=InD-Info_A10
print("Gain (A10) is %5.3f"% gainA10)
gainA11=InD-Info_A11
print("Gain (A11) is %5.3f"% gainA11)
gainA12=InD-Info_A12
print("Gain (A12) is %5.3f"% gainA12)
gainA13=InD-Info_A13
print("Gain (A13) is %5.3f"% gainA13)
gainA14=InD-Info_A14
print("Gain (A14) is %5.3f"% gainA14)
gainA15=InD-Info_A15
print("Gain (A15) is %5.3f"% gainA15)



#rule of root node

Result_All=[gainA1,gainA2,gainA3,gainA4,gainA5,gainA6,gainA7,gainA8,gainA9,gainA10,gainA11,gainA12,gainA13,gainA14,gainA15]
max_gain=max(Result_All)
pos=np.argmax(Result_All)
print("max gain of attb is %5.3f" % max_gain,"position is",pos)

# #วน loop แยก dataset ตาม attb age
# X2L=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age <=30
# X2M=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age 31-40
# X2R=[] #ข้อมูลสำหรับสร้าง level 2 ที่ Age >=40
# f1=open("buycomL2left.txt","w")
# f2=open("buycomL2middle.txt","w")
# f3=open("buycomL2right.txt","w")


# for i in range(0,15):
#     if ((X[i].count('<=30')==1)): 
#         f1.write(str(X[i]))
    
#     elif(X[i].count('31-40')==1):
#         f2.write(str(X[i]))
        
#     elif(X[i].count('>=40')==1):
#         f3.write(str(X[i]))

# # dataset of layer 2 of dtree generate
# f1=open("buycomL2left.txt","r")
# f2=open("buycomL2middle.txt","r")
# f3=open("buycomL2right.txt","r")
# X2L=f1.readlines()
# X2M=f2.readlines()
# X2R=f3.readlines()
