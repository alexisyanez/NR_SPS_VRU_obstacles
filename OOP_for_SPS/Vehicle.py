# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:36:52 2023

@author: CSUST
"""

import math
import numpy as np
from message import Beacon
import copy
import random
from list_process import transfer_2Dlist_to_1Dlist
from RBG import RGBs_set
from Obstacles import Obstacles


# =============================================================================
#     v_RBG is the observed suhchannel, 
#     the function "sense_single_RBG" is to get the sum power received by the object vehicle.
#     if the observed slot is used by object vehicle, return "False"
# =============================================================================


class Vehicle():
    
    def __init__(self, index, location, power, p_resource_keeping,RCrange,target_distance,obstacles_bool,obstacles,nr):
        self.index = index
        self.type = location[3]
        #print(self.type) just to dbug the type
        self.location = location
        self.v_RBG = None
        self.v_em_RBGs_set = []
        self.v_em_RBGs_multiple = []
        self.choose_RBGs_multiple = []
        self.message_list = None
        self.power = power
        self.sensepower_1100ms = {}
        self.sensingpower_current_slot = {}
        self.RBGlist_1100ms = []
        self.RBGlist_tillnow = []
        self.RBGlist_in_slot = []
        self.prepower_in_selection_window = {}
        self.best_RBG_list_beacon = []
        self.neighbour_list = []
        self.VRUneighbour_list = []  #adding the list of neighbout for VRU
        self.VRUreception = []  # To check message reception 
        self.PDR_VRUreception_pair = []
        self.transmission_statistic = []
        self.VRUtransmission_statistic = [] # Collecting the statistic for VRU neigbohrs
        self.target_distance = target_distance
        self.reselection_counter = random.randint(RCrange[0], RCrange[1])
        self.RBGs_in_selection_window = []
        self.num_tran = 0
        self.num_rec = 0
        self.VRUnum_tran = 0 # Special metrics for VRU
        self.VRUnum_rec = 0 # Special metrics for VRU
        self.p_resource_keeping = p_resource_keeping
        self.RSRP_th = -110.35564074964655
        self.max_upper_bound = 0
        self.n_sample = 0        
        self.RSRPth_selected=[]
        self.RSRPth_index_selected = []
        self.candidate_ratio_selected = []
        self.candidate_ratio_index_selected = []
        self.features_list = []
        self.features_decision_mapping = {}
        self.k=0
        self.candidate_chosen_list = []
        self.bm_reception_record = {}
        self.v_RBG_last_one=None
        self.obstacles_bool=obstacles_bool
        self.obstacles=obstacles # Getting obstacles from main class
        self.lastSel_t=float('inf')
        self.nr_bool = nr

  

        
        
    def initial_statistic_pdr_multi_dis(self,distance_list):
        for i in distance_list:
            self.statistic_pdr_multi_dis[i]=0
            self.statistic_all_packet_multi_dis[i]=0
        
        
    def initial_RBGs_selection(self,RBG_list,interval):
        self.v_RBG = random.choice(transfer_2Dlist_to_1Dlist(RBG_list[:interval]))

    def initial_RBGs_selection_em(self,RBG_list):
        #self.v_em_RBG = RGBs_set(0,[0,1])
        self.v_em_RBGs_set = [RBG_list[0][0],RBG_list[0][1]]
        self.v_em_RBGs_multiple = [RGBs_set(0,[0,1])]
        self.choose_RBGs_multiple=[[RBG_list[0][0],RBG_list[0][1]]]
        
    def generate_RBGlist_in_slot(self,current_time, RBG_list):
        self.RBGlist_in_slot = RBG_list[current_time]
    
    def update_reselection_counter(self,current_time,interval,RCrange):
        if current_time % (int(interval)) == 0:
            self.reselection_counter -= 1
            if self.reselection_counter < 0:
                self.reselection_counter = random.randint(RCrange[0],RCrange[1])
    
    def generate_RBGlist_1100ms(self,current_time, RBG_list, sensing_window):
        if current_time>=sensing_window:
            self.RBGlist_1100ms = RBG_list[current_time-sensing_window:current_time]
        else:
            self.RBGlist_1100ms = RBG_list[:current_time]
    


    def generate_RBGs_in_selection_window(self,current_time,RBG_list,window_size):
        self.RBGs_in_selection_window = transfer_2Dlist_to_1Dlist(RBG_list[current_time:current_time+window_size])

        
    def update_power(self,newpower):
        self.power = newpower
        
    def update_location(self,newlocation):
        self.location = newlocation
        
    def update_RBG(self,newv_RBG):
        self.v_RBG = newv_RBG
    
    def message_list_ini(self,time_period):
        self.message_list = [None]*time_period
        
    def generate_beacon(self,interval,mdelay,time_period):
        for i in range(0,int(time_period/interval)):
            if int(i*interval) >= time_period:
                break
            mID=str(self.index)+'-'+ str(self.type) +'-'+str(i)
            ## print('The ID and type for the beacon is: '+mID)
            self.message_list[int(i*interval)] = Beacon(0, mdelay, int(i*interval), None, interval,mID)


    def genearate_vehicles(num_vehicle, num_slot, vehicle_location, transmit_power):
        vehicle_instance_list = []
        for i in range(num_vehicle):
            vehicle_instance_list.append(Vehicle(i,vehicle_location[i],transmit_power))
        return vehicle_instance_list    


    def distance(self,v2):
        v1_location = self.location
        v2_location = v2.location
        distance = math.sqrt(math.pow((v2_location[0] - v1_location[0]), 2) + math.pow((v2_location[1] - v1_location[1]), 2))
        return distance
    
    def receive_power(self,vehicle):        
        k0 = 10**(-4.38)
        if self.distance(vehicle) != 0:
            # Substract losses from obstacles in the receive power
            if self.obstacles_bool==True:
                obs_loss = self.obstacles.getObsaclesLossess(self.location,vehicle.location)
                Total_loss_dB = np.log10(k0*vehicle.power*self.distance(vehicle)**(-3.68))*10 - obs_loss
                Total_loss_mw = 10**(Total_loss_dB/10)
                if Total_loss_mw>=0: 
                    return Total_loss_mw
                else: 
                    return 0
            else:   
                return k0*vehicle.power*self.distance(vehicle)**(-3.68)
        else:
            #if self.obstacles_bool==True:
            #    obs_loss = self.obstacles.getObsaclesLossess(self.location,vehicle.location)
            #    return k0*vehicle.power*0.1**(-3.68) - obs_loss
            #else:   
            return k0*vehicle.power*0.1**(-3.68)
            
    
    # check if the slot can be measured by the object vehicle, due to the half duplex
    def observation_boolean(self, v_RBG):
        timeslot = v_RBG.timeslot
        if timeslot == self.v_RBG.timeslot:
            return False
        else:
            return True    

    def sense_single_RBG(self, v_RBG, vehicles):
        sum_power = 0
        vehicles_copy=copy.copy(vehicles)
        vehicles_copy.remove(self)
        timeslot = v_RBG.timeslot
        subchannel = v_RBG.subchannel
        if self.observation_boolean(v_RBG) == True:
            for vehicle in vehicles_copy:
                #print(vehicle.v_RBG.subchannel,subchannel,vehicle.v_RBG.timeslot,timeslot)
                if vehicle.v_RBG.subchannel == subchannel and vehicle.v_RBG.timeslot == timeslot:
                    sum_power += self.receive_power(vehicle)
        else:
            sum_power = float("inf")
        return sum_power
 
        
    def sensing_single_slot(self, time, vehicles, RBG_list):
        self.sensingpower_current_slot = {}
        self.generate_RBGlist_in_slot(time, RBG_list)
        for RB in self.RBGlist_in_slot:
             self.sensingpower_current_slot[RB]=self.sense_single_RBG(RB, vehicles)

    def remove_outofdate_sensing(self,current_time, RBG_list, sensing_window):
        outofdate_RBGs = RBG_list[current_time-sensing_window-1]
        if current_time>sensing_window:
            for RB in outofdate_RBGs:
                self.sensepower_1100ms.pop(RB)
                
            
    def add_uptodate_sensing(self,current_time, vehicles, RBG_list):
        self.sensing_single_slot(current_time-1, vehicles, RBG_list)
        self.sensepower_1100ms.update(self.sensingpower_current_slot)
    
    def update_sensing_result(self, current_time, vehicles, RBG_list, sensing_window):
        self.remove_outofdate_sensing(current_time, RBG_list,sensing_window)
        self.add_uptodate_sensing(current_time, vehicles, RBG_list)     
                
    def evaluate_average_power(self,observed_RBG, channel):
        ####################### Important #########################################
        ## As shown in https://ieeexplore.ieee.org/document/9579000, there are no more average evaluation over 5G-NR
        ###########################################################################
        sum_power_list = []
        RBGlist_1100ms_temp=transfer_2Dlist_to_1Dlist(self.RBGlist_1100ms)
        for RB in RBGlist_1100ms_temp:
            if self.nr_bool:
                if RB.subchannel == observed_RBG.subchannel: # and (observed_RBG.timeslot - RB.timeslot)%(channel.interval) == 0:  
                    sum_power_list.append(self.sensepower_1100ms[RB])
            else:
                if RB.subchannel == observed_RBG.subchannel and (observed_RBG.timeslot - RB.timeslot)%(channel.interval) == 0:  
                    sum_power_list.append(self.sensepower_1100ms[RB])
        if self.nr_bool:
            self.prepower_in_selection_window[observed_RBG] = sum_power_list[0] # np.average(sum_power_list)
        else:
            self.prepower_in_selection_window[observed_RBG] = np.average(sum_power_list)

    def evaluate_power_in_selection_window(self, channel):
        self.prepower_in_selection_window={}
        for RB in self.RBGs_in_selection_window:
            self.evaluate_average_power(RB, channel)
                    
    def find_accessible_RBGs_for_beacon(self, RSRP_ratio_beacon):
        temp = copy.copy(self.prepower_in_selection_window)
        self.best_RBG_list_beacon = []
        num_picked_RBGs = int(RSRP_ratio_beacon * len(temp))
        
        for i in range(num_picked_RBGs):
            min_power_RBG = min(temp.items(), key=lambda x: x[1])[0]
            self.best_RBG_list_beacon.append(min_power_RBG)
            temp.pop(min_power_RBG)
            
    def RBG_selection_beacon(self, RSRP_ratio_beacon, RBG_list, current_time, channel):
        #observed_RBG_in_selection_window = RBG_list[current_time:current_time+channel.interval]
        self.v_RBG_last_one = self.v_RBG # for reward calculation in em generation, in case new rbg is selected but not yet statistic
        p = random.random()
        if p>self.p_resource_keeping and self.reselection_counter == 0:
            self.evaluate_power_in_selection_window(channel)
            self.find_accessible_RBGs_for_beacon(RSRP_ratio_beacon)
            self.v_RBG = random.choice(self.best_RBG_list_beacon)
            #print(self.v_RBG)
        else:
            self.v_RBG = RBG_list[self.v_RBG.timeslot+channel.interval][self.v_RBG.subchannel]
    
    def generate_neighbour_set(self,vehicles):
        self.neighbour_list = []
        self.VRUneighbour_list = []
        #self.VRUreception = []
        vehicles_copy = copy.copy(vehicles)
        vehicles_copy.remove(self)

        for vehicle in vehicles_copy:
            if self.distance(vehicle)<=self.target_distance:
                self.neighbour_list.append(vehicle)
                if vehicle.type == 1 and self.type == 2: 
                    self.VRUneighbour_list.append(vehicle)
                    #self.VRUreception.append(0)                            
                                
    def sum_interference_power(self,receive_vehicle,vehicles):
        sum_interference = 0
        vehicles_copy=copy.copy(vehicles)
        vehicles_copy.remove(self)
        vehicles_copy.remove(receive_vehicle)

        if self.v_RBG.timeslot == receive_vehicle.v_RBG.timeslot:
            sum_interference = float("inf")
        else:
            for vehicle in vehicles_copy:
                if vehicle.v_RBG.timeslot == self.v_RBG.timeslot and vehicle.v_RBG.subchannel == self.v_RBG.subchannel:
                    sum_interference += receive_vehicle.receive_power(vehicle)
        return sum_interference

    
    def sum_interference_power_em(self,receive_vehicle,vehicles,RB):
        sum_interference = 0
        vehicles_copy=copy.copy(vehicles)
        vehicles_copy.remove(self)
        vehicles_copy.remove(receive_vehicle)
        
        # check half-duplex errors
        if RB.timeslot == receive_vehicle.v_RBG.timeslot:
            sum_interference = float("inf")
            return sum_interference
        # if no half-duplex errors, accumulate the interference power
        for vehicle in vehicles_copy:                
            if vehicle.v_RBG.timeslot == RB.timeslot and vehicle.v_RBG.subchannel == RB.subchannel:
                sum_interference += receive_vehicle.receive_power(vehicle)                    
        return sum_interference    

    def sinr_calculate(self,receive_vehicle,vehicles,noise):
        useful_power = receive_vehicle.receive_power(self)
        interference_power = self.sum_interference_power(receive_vehicle,vehicles)
        sinr = useful_power/(interference_power+noise)
        return sinr
 
    def check_message_reception(self,receive_vehicle,vehicles,sinr_th,noise):
        sinr = self.sinr_calculate(receive_vehicle,vehicles,noise)
        if sinr >= sinr_th:
            reception = True
        else:
            reception = False
        return reception

        
    def statistic_for_reception(self,vehicles,sinr_th,noise,current_time,start_sampling_time):
        reception = 0     
        num_packet = len(self.neighbour_list)
        if current_time>start_sampling_time:
            self.num_tran += len(self.neighbour_list)
        #print('t=',current_time,self.index,'neighbour_list',self.neighbour_list)
        for vehicle in self.neighbour_list:
            
            # shorten vehicle.bm_reception_record
            len_record = len(vehicle.bm_reception_record)
            popkeys = list(vehicle.bm_reception_record.keys())[:min(len_record-400,0)]
            [vehicle.bm_reception_record.pop(k) for k in popkeys]    

            if self.check_message_reception(vehicle,vehicles,sinr_th,noise) == True:
                reception += 1
                vehicle.bm_reception_record[str([self.index,self.v_RBG.timeslot])]=1
                
                if current_time>start_sampling_time:
                    self.num_rec += 1

                    if self.type == 1 and vehicle.type == 2:  # Type 1 corresponds to VRU, and Type 2 is Car
                        if self in vehicle.VRUneighbour_list:
                            vehicle.VRUreception.append(self.index)
                            
                        
                        #if self in VRU_List:
                        #    VRU_index = VRU_List.index(self)
                        #    vehicle.VRUreception[VRU_index]=1
                    #print("VRU index: ",self.index)
                    #print("VRU List: ",vehicle.VRUneighbour_list)
                    #print("VRU recception List: ",vehicle.VRUreception)


            else:
                vehicle.bm_reception_record[str([self.index,self.v_RBG.timeslot])]=0
        if num_packet==0:
            self.transmission_statistic.append(None)
        else:
            self.transmission_statistic.append(reception/num_packet)


        #repeat the process for VRU neighbours

"""         reception = 0     
        num_packet = len(self.VRUneighbour_list)
        if current_time>start_sampling_time:
            self.VRUnum_tran += len(self.VRUneighbour_list)
        #print('t=',current_time,self.index,'neighbour_list',self.neighbour_list)
            
        for vehicle in self.VRUneighbour_list:
            # shorten vehicle.bm_reception_record
            len_record = len(vehicle.bm_reception_record)
            popkeys = list(vehicle.bm_reception_record.keys())[:min(len_record-400,0)]
            [vehicle.bm_reception_record.pop(k) for k in popkeys]    

            if self.check_message_reception(vehicle,vehicles,sinr_th,noise) == True:
                reception += 1
                vehicle.bm_reception_record[str([self.index,self.v_RBG.timeslot])]=1
                
                if current_time>start_sampling_time:
                    self.VRUnum_rec += 1

                # This is the Empiric VAP
                if self.type == 1 and vehicle.type == 2:
                    VRU_List = vehicle.VRUneighbour_list
                    if self in VRU_List:
                        VRU_index = VRU_List.index(self)
                        vehicle.VRUreception[VRU_index]=1
                    #print("VRU index: ",self.index)
                    #print("VRU List: ",vehicle.VRUneighbour_list)
                    #print("VRU recception List: ",vehicle.VRUreception)
            else:
                vehicle.bm_reception_record[str([self.index,self.v_RBG.timeslot])]=0
        if num_packet==0:
            self.VRUtransmission_statistic.append(None)
        else:
            self.VRUtransmission_statistic.append(reception/num_packet)
        
 """