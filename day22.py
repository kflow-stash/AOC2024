
from collections import defaultdict
input_ = list(map(int,open("data/day22.txt", "r").read().split("\n")))

def process(secret):
    x1 = secret * 64
    x2 = x1 ^ secret
    x3 = x2 % 16777216
    
    y1 = x3 // 32
    y2 = y1 ^ x3
    y3 = y2 % 16777216
    
    z1 = y3 * 2048
    z2 = z1 ^ y3
    z3 = z2 % 16777216
    
    return z3
   
t = 100000000 % 16777216
    
pt1 = 0
#input_ = [123]
prices = []
diffs = []
for x in input_:
    price_seq = []
    diff_seq = []
    val = int(str(x)[-1])
    for z in range(2000):
        x = process(x)  
        val2 = int(str(x)[-1])
        price_seq.append(val2) 
        diff_seq.append(val2-val)
        val = val2
        
    prices.append(price_seq)
    diffs.append(diff_seq)
    
    pt1 += x
    
print("initial calc complete")
seqs = defaultdict(lambda: 0)
for price, diff in zip(prices,diffs):
    item_seq = {}
    for ix in range(3,len(price)):
        seq = tuple(diff[ix-3:ix+1])
        if seq not in item_seq:
            item_seq[seq] = price[ix]
            
    for seq, price in item_seq.items():
        seqs[seq] += price
        


print(max(seqs.values()))

#1690 too low