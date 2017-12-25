
#coding:utf-8
def PrimeNum(num):
      r_value =[]
      for i in range (2,num+1):
            for j in range(2,i):
                  if i % j == 0:
                        break
            else:
                  r_value.append(i)
      returnr_value
 
def PrimeFactorSolve(num,prime_list):
      for n in prime_list :
            if num % n == 0:
                  return[n,num / n]
 
 
def PrimeDivisor(num):
      prime_range= PrimeNum(num)
      ret_vale =[]
      while numnot in prime_range:
            factor_list= PrimeFactorSolve(num,prime_range)
            ret_vale.append(factor_list[0])
            num =factor_list[1]
      else:
            ret_vale.append(num)
      printret_vale
 
PrimeDivisor(92164540447138944597127069158431585971338721360079328713704210939368383094265948407248342716209676429509660101179587761913570951794712775006017595393099131542462929920832865544705879355440749903797967940767833598657143883346150948256232023103001435628434505839331854097791025034667912357133996133877280328143
)
 