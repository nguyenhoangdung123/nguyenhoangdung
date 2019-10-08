import numpy
def Sum(myNumber):
  SUM=0
  for i in myNumber:
    SUM += i 
  return SUM

quan = ['ST', 'BĐ', 'BTL', 'CG', 'DD', 'HBT']
dientich = ['117.43', '9.224', '43.35', '12.04', '9.96', '10.09']
danso = ['150.300', '247.100', '333.300', '266.800', '420.900', '318.000']
matdodancu = numpy.arange(len(quan))
for i in range(len(quan)):
  matdodancu[i] = danso[i]/dientich[i]
  print((Sum(matdodancu)/(len(quan))+1))