import math

def sensitivity(tp,fn):
    return tp/(tp+fn)

def specificity(tn,fp):
    return tn/(tn+fp)

def geo_mean(tp,fn,tn,fp):
    return math.sqrt(sensitivity(tp,fn)*specificity(tn,fp))

def precision(tp,fp):
    return tp/(tp+fp)

def F_measure(tp,fp,recall):
    num = 2*precision(tp,fp)*recall
    den = precision(tp,fp)+recall
    return num/den

def accuracy(tn,tp,fn,fp):
    num = tn+tp
    den = tn+tp+fn+fp
    return num/den