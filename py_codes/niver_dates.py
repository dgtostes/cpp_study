days_list = [i for i in range(0,32)]
months_list = [i for i in range(0,12)]

for i in range(0,10):
  days_list.append("0%s" % i)
  months_list.append("0%s" % i)
years_list = [i for i in range(1900, 2012)]

if __name__ == "__main__":
 #  print days_list 
 #  print months_list
 #  print years_list
    pass_list = []
    for day in days_list:
       for month in months_list:
          for year in years_list:
              pass1 = '%s%s%s' % (day, month, year)
              pass2 = '%s%s%s' % (day, month, str(year)[2:])
              pass_list.append(pass1)
              pass_list.append(pass2)


    print ('151182' in pass_list)
