resp = nsfg.ReadFemResp()
In [39]:
# Solution goes here
kids = thinkstats2.Pmf(resp.numkdhh, label = 'numkdhh')
In [46]:
# Solution goes here
thinkplot.Pmf(kids)
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')

In [47]:
# Solution goes here
biased_kids=BiasPmf(kids, label='biased')
In [48]:
# Solution goes here
thinkplot.PrePlot(2)
thinkplot.Pmfs([kids, biased_kids])
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')

In [51]:
# Solution goes here
kids.Mean()
Out[51]:
1.024205155043831
In [52]:
# Solution goes here
biased_kids.Mean()
Out[52]:
2.403679100664282
