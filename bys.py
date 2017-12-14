# -*- coding: utf-8 -*-
"""
题目：利用贝叶斯框架估计共有10个门，主持人打开3个空门的蒙提霍尔问题。
"""

# -*- coding: utf-8 -*-
import random

def get_value(n): #计算阶乘
    if n==1:
        return n
    else:
        return n * get_value(n-1)
        
def C(n,m): #计算组合数
     first = get_value(n)
     second = get_value(m)
     third = get_value((n-m))
     return first/(second * third)

def pre(hypos): #先验概率P(Hx)，x=0,1,2...
    probs={}    
    count=len(hypos)    
    for hypo in hypos:
        probs[hypo]=1.0/count
    print('先验概率：', probs, hypos)
    return probs

def LikeliHood(data,hypo): #一个证据data出现时，计算P(data|Hx),x=0,1,2...
    re = 0
    if hypo == data or data == e1:
        re=0
    if hypo!= data and hypo == e1:
        re= C(8, 2)/C(9, 3)
    if hypo!= data and hypo!= e1:
        re= C(7, 2)/C(8, 3)
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
E = random.sample(H, 3)
e1 = random.choice(list(set(H).difference(set(E))))
print('选择：', e1, "开门：", E, run(E, H))
