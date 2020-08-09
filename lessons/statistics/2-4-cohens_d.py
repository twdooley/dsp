
def WeightDiff(live, firsts, others):
    """Get means"""
    mean_live = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean_oth = others.totalwgt_lb.mean()
    
    """Get vars"""
    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()
    
    print('Means')
    print(f'First birth: {mean1}')
    print(f'Others: {mean_oth}\n')
    print('Variances')
    print(f'First: {var1}')
    print(f'Others: {var2}\n')
    print('Differences in Means')
    print(f'First - Others in lbs: {mean1 - mean_oth}')
    print(f'First - Others in oz: {(mean1-mean_oth)*16}\n')
    d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print(f"Cohen's d: {d}")
   
 WeightDiff(live, firsts, others)
