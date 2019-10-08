a={"Name":"Huy","role":"waiter","hours":12,"Salary per hour($)":0.8}
b={"Name":"Tung","Role":"Cook","Hours":24,"Salary per hour($)":1.5}
c={"Name":"M.Duc","role":"Manager","Hours":20,"Salary per hour($)":2}
d=[a,b,c]
print(*d,sep='\n')
e={"Name":"Don","Role":"Waiter","Hours":12,"Salary per hour($)":0.9}

f={"Name":"H.Duc","Role":"waiter","Hours":14,"Salary per hour($)":0.7}
d.append(e)
d.append(f)
print(*d,sep="\n")