[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

##Distribution of 1000 random numbers

``` python
num = np.random.random(1000)  #initialize the variable num with 1000 random numbers

pmf = thinkstats2.Pmf(num) 
thinkplot.Pmf(pmf, linewidth = .05)
thinkplot.Config(xlabel='Random Variate', ylabel = 'PMF') 
```
The PMF shows what seems to be mostly evenly distributed probabilities for all numbers 0.0 - 1.0. This is expected if np.random.random is working as expected. 

``` python 
cdf = thinkstats2.Cdf(pmf)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random Variate', ylabel = 'CDF')
```

As expected, the CDF is a mostly straight line. All values 0.0 - 1.0 are equally likely. This exercise demonstrates the different functions of PMF and CDF. The PMF is less valuable than the CDF in this instance. The CDF very clearly shows the equal probailities of each value. 

