[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)


```python
# Solution goes here
def Simulator(n=10, lam=2, iters=1000):
    """
    n: sample size
    lam: param of exponential distr
    iters=simiulation runs"""
    
    estimates=[]
    for _ in range(iters):
        xs = np.random.exponential(1.0/lam, n)
        big_l = 1/np.mean(xs)
        estimates.append(big_l)
    
    #find standard error using RMSE above
    stderr = RMSE(estimates, lam)
    print(f"Standard error: {stderr}")

    #find cdf to find confidence interval
    cdf=thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print(f"Confidence Interval: {ci}")
    
    #create function to draw interval lines
    #y=1 to reach top of CDF 
    def ConfidenceLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.7', linewidth=3)
    
    #plot first line at ci, 5
    #plot second line at ci, 95
    ConfidenceLine(ci[0])
    ConfidenceLine(ci[1])
    
    #plot CDF
    #Config labels
    thinkplot.Cdf(cdf)
    thinkplot.Config(xlabel='estimate',
                     ylabel='CDF',
                     title='Sampling distribution')
    
Simulator()
```

![sampling distribution] (dsp/img/sampling_dist.png)


