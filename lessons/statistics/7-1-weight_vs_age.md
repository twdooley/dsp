[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

``` python 
ages= live.agepreg
totalwgt = live.totalwgt_lb
print(f"Pearson: {Corr(ages, totalwgt)}")
print(f"Spearman: {SpearmanCorr(ages, totalwgt)}")
print(f"Pearson log: {Corr(ages, np.log(totalwgt))}")

>Pearson: 0.06883397035410904
>Spearman: 0.09461004109658226
>Pearson log: 0.047422550910037505

def ScatterPlot(ages, weights, alpha = 0.1, s=10):
    thinkplot.Scatter(ages, weights, alpha=alpha)
    thinkplot.Config(xlabel = 'Maternal Age in years', 
                    ylabel = 'Weight in Pounds', 
                    xlim = [10,50],
                    ylim = [0, 15])
ScatterPlot(ages, totalwgt)

thinkplot.HexBin(ages, totalwgt, alpha = 1)
thinkplot.Config(xlabel='Ages',
                 ylabel='Weight (lb)',
                 xlim = [10,45],
                 ylim = [0, 15],
                 legend=False)

def PlotPercentiles(df):
  bins = np.arange(10, 50, 3)
  indices = np.digitize(df.agepreg, bins)
  groups = df.groupby(indices)

  ages = [group.agepreg.mean() for i, group in groups]
  cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

  thinkplot.PrePlot(3)
  for percent in [75, 50 ,25]:
      weights = [cdf.Percentile(percent) for cdf in cdfs]
      label = '%dth' % percent
      thinkplot.plot(ages, weights, label = label)

  thinkplot.Config(xlabel = 'Maternal Age in years', 
                  ylabel = 'Weight in Pounds', 
                  xlim = [14, 45],
                  label = True)
                  
PlotPercentiles(live)
```
*Conclusion:* The scatter, and especially the HexBin, show some coalescence between 6 and 8 lbs for all ages. The percentiles show that the 50th percentile does in fact hover around 7 lbs. Further, it shows that the relationship between maternal age and birthweight is nonlinear at the extremes of maternal age. For women in the middle age ranges, the effect may be more linear. However, the overall relationship is nonlinear. 
