[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

#First, make a child class DiffMeansResample from parent DiffMeansPermute

```python
class DiffMeansResample(DiffMeansPermute):
    def RunModel(self):
        """Seperate groups with random choice from pool of lengths self.n, self.m.
        Allow sampling with replacement with replace = True"""
        group_1 = np.random.choice(self.pool, self.n, replace = True)
        group_2 = np.random.choice(self.pool, self.m, replace = True)
        return group_1, group_2  
  ```
  
  The parent class ran a model by shuffling the pooled data then separating the data into groups equal to original preshuffle lengths. 
  This child class resamples instead of permutes. It picks random choices with replacement from the pooled data for 2 new groups of lengths of the original data groups. 

```python 
live, firsts, others = first.MakeFrames()
data_prglngth = firsts.prglngth.values, others.prglngth.values
rt_prglngth = DiffMeansResample(data_prglngth)
pvalue = rt_prglngth.PValue()
actual = rt_prglngth.actual
pvalue, actual
```
> 0.166, 0.07803726677754952

__Conclusion__: it seems that resampling returns an identical p-value to the prior permutation method. Perhaps both are equally valid methods of running a model to find a p-value. In any case, the p-value is too high at 17% to reject the null hypothesis for pregnancy lengths. 
