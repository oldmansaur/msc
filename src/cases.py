'''
Created on Mar 11, 2015

@author: saur

I am not sure if this file will be used, it is an attempt to decouple the pypower model from the agent
so that different agents can make their changes.
'''
from scipy import array,ones
from pypower.api import  ppoption, runopf

class cases(object):
    '''
    classdocs
    '''

    def __init__(self, Time):
        '''
        Constructs a pypower case and inits a load profile
        '''
        #data for the power flow 
        self.Time = Time ## might be a useless variable since the laod profile has been moved to the agent
        ##options
        self.ppopt = ppoption(OPF_ALG=0,opf_flow_lim=2, VERBOSE= False,OUT_ALL=0) #using default opf solver
        self.ppc = {"version": '2'}
        
        
        ## system MVA base
        self.ppc["baseMVA"] = 0.144
        
        ## bus data
        # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
        self.ppc["bus"] = array([
        [1,3,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [2,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [3,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [4,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [5,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [6,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [7,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [8,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [9,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [10,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [11,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [12,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [13,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [14,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [15,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [16,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [17,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [18,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [19,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [20,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [21,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [22,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [23,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [24,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
        [25,1,0,0,0,0,0,1,1,0,1,1.1,0.94],
    ])
        ## generator data
        # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
        # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
        self.ppc["gen"] = array([
        [1, 1, -16.9, 1,   0, 1.0,  100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [10, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [11, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [13, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [14, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [15, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [16, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [17, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [18, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [19, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [20, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [21, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [22, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [23, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [24, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [25, 0, 0, 1,   0, 1.0,  100, 1,0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
        self.ppc["branch"] = array([
        [2,1,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [3,2,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [4,3,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [5,4,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [6,5,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [7,6,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [8,1,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [9,8,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [10,9,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [11,10,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [12,11,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [13,12,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [14,1,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [15,14,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [16,15,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [17,16,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [18,17,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [19,18,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [20,1,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [21,20,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [22,21,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [23,22,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [24,23,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360],
        [25,24,0.001590, 0.000814,0,0,0,0,0,0,1,-360,360]
        ])
        self.ppc["branch"][:,2]= (0.494 * 0.1 / 1.1) * ones(24)
        self.ppc["branch"][:,3]= (0.0883 * 0.1 / 1.1) * ones(24)
        
        self.ppc["gencost"] = array([
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        [2, 0, 0, 1, 1, 1],
        ])
        
        
        
    def get_output(self):
        #returns the output of the load flow calculation
        ppc_result,y = runopf(self.ppc, self.ppopt)
        #print ppc_result["bus"][node,7]
        return ppc_result
    
   
    def set_power(self,node, power):
        # sets the power at a specific node
        print - power / 1000.0
        self.ppc["gen"][node -1,1]= - power / 1000.0 #divide by 1000 to transform it to MW , the node -1 because indexing starts with 0 
        
    
    
    def change_restrictions(self,rateA):
        self.ppc["branch"][:,5]= rateA
        
        
        
    #def get_power_actual(self, node):
    #    ppc_result,y = runpf(self.ppc, self.ppopt)
    #    return ppc_result["bus"][node,2]
        
    #def set_base(self,Time):
        #sets the model to the base load profiles at a certain point in time
    #    Time = Time % 96
    #    p = self.loadprofile[Time] * ones(25)
    #    p[0] = 0 # set the power at slack to 0
    #    for k in range(0,self.ppc["bus"].shape[0]):
    #        self.ppc["bus"][k,2]= p[k] #reset the p value
        
        
        
        