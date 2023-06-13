import json as js
def input_rec(data,filename):
  n = int(input("Enter the Range of record : "))
  for i in range(n):
    row = []
    empId = int(input("Enter the employee id : "))
    name = input("Enter the employee Name : ")
    fname = input("Enter the employee father name : ")
    email = input("Enter the Email Address : ")
    row = [name,fname,email]
    data[empId] = row
  f = open(filename,'w')
  fh = js.dumps(data)
  f.write(fh)
  f.close()
  return data

# searching record into json file
def search_rec(filename):
  key = input("Enter the empId to search record : ")
  f = open(filename,'r')
  fh = js.load(f)
  for i in range(len(fh)):
    if list(fh.keys())[i]==key:
      print("Name                :              ",fh[key][0])
      print("Father Name         :              ",fh[key][1])
      print("Email               :              ",fh[key][2])
  f.close()

def display(filename):
  f = open(filename,'r')
  fh = js.load(f)
  for k,v in fh.items():
    print(k,v)
  f.close()