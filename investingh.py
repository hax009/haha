import numpy as np
from itertools import combinations


def get_index(i):
    comb = combinations(p, i)

    # Print the obtained combinations
    comblist = []
    for k in list(comb):
        comblist.append(k)
        
    abk = []
    for ii in comblist:
        dd = [0]*len(p)
        for ik in range(len(p)):
            if p[ik] in ii:
                dd[ik] = 1
        abk.append(dd)
    return abk









def est_pdf(p):
    result = np.empty(len(p))
    #def get_index(i):
    
    for i in range(len(p)):
        indexes = get_index(i)
        
        #p = [0.4,0.5,0.1]
        #ex: i = 2, return indexes = [[1,1,0],[0,1,1],[1,0,1]]
        
        for j in range(len(indexes)):
            #p_k = 0
            #j = 1
            p_k = []
            
            for k in indexes[j]:
                sm = []
                cc = 0
                #k = 1
                #p_k += p[indexes[j][k]==1]*(1-p[indexes[j][k]==0])
                if p[cc] == k:
                    sm.append(p[cc])
                else:
                    sm.append(1-p[cc])
                cc += 1
            p_k.append(np.prod(sm))
            
            result[i] = np.sum(p_k)
                
                
                
                
                
                
                #for og in range(len(p)):
                    #if k == 1:
                        #p_k.append(p[og])
                    #else:
                        #p_k.append(1-p[og])
                #p_kk = np.prod(p_k)
            #result[i] = p_kk
    return result
