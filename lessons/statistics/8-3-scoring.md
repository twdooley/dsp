[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

```python
def ManyGames(lam = 2, m = 1000000):
    results = []
    for _ in range(m):
        L = SimulateGame(lam)
        results.append(L)
    
    print("RESULTS \n")
    print("MeanError", MeanError(results, lam))
    print("RMSE", RMSE(results, lam))
    print("First 5 results", results[:5])
    
    pmf = thinkstats2.Pmf(results)
    hist = thinkplot.Hist(pmf)
    thinkplot.Config(xlabel='Goals', ylabel = 'PMF')
    
    ci = pmf.Percentile(5), pmf.Percentile(95)
    print(f"Confidence Interval: {ci}")
    
    #create function to draw interval lines
    #y=1 to reach top of CDF 
    def ConfidenceLine(x, y=.3):
        thinkplot.Plot([x, x], [0, y], color='0.7', linewidth=3)
    
    #plot first line at ci, 5
    #plot second line at ci, 95
    ConfidenceLine(ci[0])
    ConfidenceLine(ci[1])
    
ManyGames(lam=2)
%time

> RESULTS 

>MeanError 0.000989
>RMSE 1.4129101174526284
>First 5 results [2, 2, 4, 1, 3]
>Confidence Interval: (0, 5)
>CPU times: user 2 µs, sys: 1 µs, total: 3 µs
>Wall time: 5.01 µs
```
```python
ManyGames(lam=10)

>RESULTS 

>MeanError 0.004257
>RMSE 10.007525218554285
>First 5 results [100, 105, 109, 96, 101]
```
With `lam=2` the RMSE is around 1.4. \
As `lam` increases the RMSE rises significantly. At `lam=10` the RMSE is around 10. MeanError also increases. Interestingly, with this high lambda not only are the average goals a ridiculous 100, but the distro looks normal.\
The Mean Error (around -.0001 at `m=1000000`) is small and becomes smaller with more simulations (increase `m`). 
