
def freqAlphabets(s: str) -> str:
    mapping_dict = {
                '1':'a','2':'b','3':'c','4':'d','5':'e',
                '6':'f','7':'g','8':'h','9':'i','10#':'j',
                '11#':'k','12#':'l','13#':'m','14#':'n',
                '15#':'o','16#':'p','17#':'q','18#':'r',
                '19#':'s','20#':'t','21#':'u','22#':'v',
                '23#':'w','24#':'x','25#':'y','26#':'z'
            }
    i = 0
    res = []
    
    while i<len(s):
            if i<len(s)-2 and s[i+2]=='#':
                    res.append(mapping_dict[s[i:i+3]])
                    i+=3
            else:
                res.append(mapping_dict[s[i]])
                i+=1
           
    print(''.join(res))
                         
    
               

freqAlphabets(input())