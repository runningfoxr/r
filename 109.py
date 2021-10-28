import random
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

diceresult=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1 + dice2)

mean=sum(diceresult)/len(diceresult)
sd=statistics.stdev(diceresult)
median=statistics.median(diceresult)
mode=statistics.mode(diceresult)

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

figure=ff.create_distplot([diceresult],["result"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
figure.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="sd2"))
figure.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="sd2"))
figure.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="sd3"))
figure.add_trace(go.Scatter(x=[third_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="sd3"))
figure.show()