

class Calories():
    """
    A class to represent Calories.

    ...

    Attributes
    ----------
    weight : float
        weight of the person
    height : int
        height of the person
    age : int
        age of the person
    sex : str 
        sex of the person (F or M)

    """
    
    def __init__(self, weight, height, age, sex):
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
             
    def bf(self):
        '''Calculating body fat (not needed at the moment) '''
        
        bf = 10.2107142857142+1.22571429*self.accu_mesure-0.01428571*self.accu_mesure**2
        return round(bf,1)
       
    def LBM(self):       
        '''Calculate lean body mass'''
        
        return self.weight*(1-self.bf()/100)
    
    def BMR(self, sex):        
        '''Calculate basal metabolic rate'''
        
        #Harris–Benedict equation
        if sex == "M":
            bmr = ((10*self.weight) + (6.25*self.height) - (5*self.age) + 5)
        else:   
            bmr = ((10*self.weight) + (6.25*self.height) - (5*self.age) - 161)
            #bmr = 370 + 21.6*self.LBM()
        return bmr
     
    def TDEE(self, act_mult = 1.4):        
        '''Calculate total daily energy expenditure'''
        
        return round(self.BMR(self.sex)*act_mult)
    
    def bulk(self, percentage = 0.2, act_mult = 1.4):        
        '''Calculate bulk calories''' 
        
        return round(self.TDEE(act_mult = act_mult)*(1+percentage))
    
    def cut(self, percentage = 0.2, act_mult = 1.4):        
        '''Calculate cut calories'''
        
        return round(self.TDEE(act_mult = act_mult)*(1-percentage))
    
    def protein_intake(self, weight, mult = 2.2):       
        '''Calculate protein intake'''
        
        return round(self.weight*mult)
    


