import math
def mean_centric(x):
    val=0
    n=len(x[1])
    for j in x[1]:
        val+=float(j[1])
    m = val/n
    for j in x[1]:
        j[1] = [j[1],j[1]-m]
    return x

def helper(x):
    res={}
    for k,v in x.items():
        if k  in ["date","user_id","business_id"]:
            res[k]=v
    return res

def key_value_conversion(x):
    res={}
    for j in x[1]:
        res[j[0]]=j[1]
    return (x[0],res)

def havecommon_2(x,y):
    item_list_1=x.keys()
    item_list_2=y.keys()
    i=0
    for ele in item_list_1:
        if ele in item_list_2:
            i+=1
        if i==2:
            return True
    return False

def cosine_sim(x,y):
    res={}
    for k,v in x.items():
        if k not in res.keys():
            res[k]=[]
        res[k].append([1,v])
    for k,v in y.items():
        if k not in res.keys():
            res[k]=[]
        res[k].append([2,v])
    n=0
    d1=0
    d2=0
    for k,v in res.items():
        if len(v)==2:
            n+=v[0][1][1]*v[1][1][1]
            d1+=v[0][1][1]*v[0][1][1]
            d2+=v[1][1][1]*v[1][1][1]
        else:
            if v[0][0]==1:
                d1+=v[0][1][1]*v[0][1][1]
            else:
                d2+=v[0][1][1]*v[0][1][1]
    return n/(math.sqrt(d1)*math.sqrt(d2)) if d1!=0 and d2!=0 else 0

def cal_t_user_p_val(x):
    n=0
    d=0
    for i in x[1]:
        n+=i[0]*i[1]
        d+=i[1]
    return (x[0],n/d if d!=0 else 0)