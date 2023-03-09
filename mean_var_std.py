def calculate():
    cal = []
    import numpy as np
    for i in range(9):
        cal.append(input())
    lit = []
    output = {
              'mean':[],
              'variance':[],
              'standard deviation':[],
              'max':[],
              'min':[],
              'sum':[]
    }
    if len(cal) == 9:
        b = np.array(cal,dtype='int64')
        b = b.reshape(3,3)
        
        lit.append(np.mean(b,axis=0).tolist())
        lit.append(np.mean(b,axis=1).tolist())
        lit.append(np.mean(b))
        output['mean'] = lit.copy()
        del(lit[0:3])
        
        lit.append(np.var(b,axis=0).tolist())
        lit.append(np.var(b,axis=1).tolist())
        lit.append(np.var(b))
        output['variance'] = lit.copy()
        del(lit[0:3])
        
        lit.append(np.std(b,axis=0).tolist())
        lit.append(np.std(b,axis=1).tolist())
        lit.append(np.std(b))
        output['standard deviation'] = lit.copy()
        del(lit[0:3])
        
        lit.append(np.max(b,axis=0).tolist())
        lit.append(np.max(b,axis=1).tolist())
        lit.append(np.max(b))
        output['max'] = lit.copy()
        del(lit[0:3])
        
        lit.append(np.min(b,axis=0).tolist())
        lit.append(np.min(b,axis=1).tolist())
        lit.append(np.min(b))
        output['min'] = lit.copy()
        del(lit[0:3])
        
        lit.append(np.sum(b,axis=0).tolist())
        lit.append(np.sum(b,axis=1).tolist())
        lit.append(np.sum(b))
        output['sum'] = lit.copy()
        del(lit[0:3])
    else:
        raise ValueError("List must contain nine numbers.")
    return output