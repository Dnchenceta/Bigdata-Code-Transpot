# -*- coding: utf-8 -*-

#多面筛子&火车头问题的贝叶斯处理框架

#E表示证据集合，data表示证据中的一项
#hypos表示假设集合，hypo表示假设的一项
#prob表示概率的字典,存储格式为{'hypo1':0.01,'hypo2':0.02,...}
import random

def pre(hypos): #先验概率P(Hx)，x=0,1,2...
    probs={}    
    count=len(hypos)    
    for hypo in hypos:
        probs[hypo]=1.0/count
    print('先验概率：', probs, hypos)
    return probs

def LikeliHood(data,hypo): #一个证据data出现时，计算P(data|Hx),x=0,1,2...
    if hypo == data or data == e1:
        re=0
    elif hypo!= data and hypo == e1:
        re= 1.0/hypo
    elif hypo!= data and hypo!= e1:
        re= 1.0/hypo
    return re

def update(evidence,probs,hypos):  #更新后验概率，P(data|Hx)*P(Hx),x=0,1,2...
    for hypo in hypos:
        like=LikeliHood(evidence,hypo)
        probs[hypo] = probs[hypo] * like
        
def run(evidence,hypos):   
    probs=pre(hypos)
    for data in evidence:    
        update(data,probs,hypos)
    sum=0.0             
    for hypo,prob in probs.items(): 
        sum += prob                #计算贝叶斯公式的分母
    for hypo,prob in probs.items(): #计算 P(Hx|E)
        probs[hypo] = prob/sum
    return probs

H = [1,2,3,4,5,6,7,8,9,10]
e1 = random.choice(H)
E = [2,3,4]
print('开门：', e1, run(E, H))
