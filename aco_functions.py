import random
import numpy as np
from preprocessing import cols,dataset


def get_matrix():
    #defective rules
    defective_rules = []
    for col in cols[0:-1]:
        operator = random.randint(0,1)
        num = random.random()%100
        rule = [col,operator,num]
        defective_rules.append(rule)
    #Non defective rules
    non_defective_rules = []
    for col in cols[0:-1]:
        operator = random.randint(0,1)
        num = random.random()%100
        rule = [col,operator,num]
        non_defective_rules.append(rule)
    #convert it to a dictionary
    rule_matrix = [defective_rules,non_defective_rules]
    return rule_matrix

def apply_rule(attribute,operator,num):
    if operator is 0:
        if attribute<num:
            return True
        else:
            return False
    
    if operator is 1:
        if attribute>num:
            return True
        else:
            return False


def get_cutpoint_based_value(col,columns):
    cpts = []
    for column in columns:
        boundary_pts = []
        dataset.sort_values(by=[column],inplace=True)
        d = dataset['Defective'][0]
        for i,defect in enumerate(dataset['Defective']):
            if defect is not d:
                d = defect
                boundary_pts.append(dataset[col][i])
        
        boundary_pts = np.array(boundary_pts)
        cpts.append(np.median(boundary_pts))
    randno = random.randint(0,len(cpts)-1)
    return cpts[randno]

def build_solution():
    pass

def update_pheromone():
    pass


def perturb_cell(mat,i,j):
    try:
        pass
    except KeyError:
        print("this is empty lol")



