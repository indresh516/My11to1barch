# main program
from operations import *

data ={}
ch =0
while ch!=5:
  print("-"*80)
  print("****EMPLOYEE MANAGEMENT SYSTEM****".center(80))
  print("-"*80)
  print("\t[1.] INSERT EMPLOYEE RECORD")
  print("\t[2.] SEARCH EMPLOYEE RECORD")
  print("\t[3.] DISPLAY EMPLOYEE RECORD")
  print("\t[4.] UPDATE EMPLOYEE RECORD")
  print("\t[5.] EXIT")
  ch = int(input("Enter Your Choice : "))
  if ch==1:
    print("-"*80)
    print("****INSERT EMPLOYEE RECORD****".center(80))
    print("-"*80)
    filename = input("Enter file name to be written employee Data : ")
    input_rec(data,filename)
    print("record Added Successfully............")
  if ch==2:
    print("-"*80)
    print("****SEARCH EMPLOYEE RECORD****".center(80))
    print("-"*80)
    filename = input("Enter file name to be written employee Data : ")
    search_rec(filename)
  if ch==3:
    print("-"*80)
    print("****DISPLAY EMPLOYEE RECORD****".center(80))
    print("-"*80)
    filename = input("Enter file name to be written employee Data : ")
    display(filename)
  if ch ==4:
    print("under construction")
  if ch==5:
    pass