#Emma Redfoot
#Calculating Effective neutron lifetime
#HW 5 problem 2

#imports
import numpy as np

beta_U = [0.00021, 0.001424, 0.001274, 0.002568, 0.000748, 0.000273]
beta_Pu =[0.000072,	0.000626,	0.000444,	0.000685,	0.00018,	0.000093]

lambda_U =[0.0124,	0.0305,	0.111,	0.301,	1.14,	3.01]
lambda_Pu =[0.01289302326,	0.03109017497,	0.1335260116,	0.3315789474,	1.262295082,	19.8]

beta_U_total = .0064
beta_Pu_total = .0021

lifetime_U = 0.0001
lifetime_Pu = 0.0000001

prompt_U =(1-beta_U_total)*lifetime_U
prompt_Pu =(1-beta_Pu_total)*lifetime_Pu


delayed_total=0
for i in range(6):
    delayed = beta_U[i]*(1/lambda_U[i]+lifetime_U)
    delayed_total=delayed_total + delayed

answer_U=delayed+delayed_total

print('Uranium Lifetime ='+ str(answer_U))

delayed_total_Pu =0
for i in range(6):
    delayed_Pu = beta_Pu[i]*(1/lambda_Pu[i]+lifetime_Pu)
    delayed_total_Pu=delayed_total_Pu + delayed_Pu

answer_Pu=delayed_Pu+delayed_total_Pu

print('Plutonium Lifetime='+str(answer_Pu))
