# Maximal

N = 256
 
def mdc(str, n):
    
    count = [0] * N
      
    for i in range(n): 
        count[ord(str[i])] += 1
      
    max_distinct = 0
    for i in range(N): 
        if (count[i] != 0): 
            max_distinct += 1    
      
    return max_distinct 
  
def ssmd(str): 
  
    n = len(str)     
  
    max_distinct = mdc(str, n) 
    minl = n
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = mdc(subs,subs_lenght) 
             
            if (subs_lenght < minl and max_distinct == sub_distinct_char): 
                minl = subs_lenght 
  
    return minl 

if __name__ == "__main__": 
      
    s = input()
      
    l = ssmd(s); 
    print( "The length of the smallest substring : ", l)
