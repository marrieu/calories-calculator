

class Calories():
    
    def __init__(self, weight, height, age, sex):
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
        
    # calculating body fat (not needed at the moment)    
    def bf(self):
        bf = 10.2107142857142+1.22571429*self.accu_mesure-0.01428571*self.accu_mesure**2
        return round(bf,1)
     
    # calculate lean body mass
    def LBM(self):
        lbm = self.weight*(1-self.bf()/100)
        return lbm
    
    # Calculate basal metabolic rate 
    def BMR(self, sex):
        
        #Harris–Benedict equation
        if sex == "M":
            bmr = ((10*self.weight) + (6.25*self.height) - (5*self.age) + 5)
        else:   
            bmr = ((10*self.weight) + (6.25*self.height) - (5*self.age) - 161)
            #bmr = 370 + 21.6*self.LBM()
        return bmr
     
    def TDEE(self, act_mult = 1.4):
        tdee = self.BMR(self.sex)*act_mult
        #tdee = act_mult*self.BMR()
        return tdee
    
    def bulk(self, percentage = 0.2):
        return self.TDEE()*(1+percentage)
    
    def cut(self, percentage = 0.2):
        return self.TDEE()*(1-percentage)
    
    
