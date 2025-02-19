import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
import numpy as np
from scipy.optimize import curve_fit
import os

def main():

    #st.set_page_config(layout='centered')
    #st.title('Results visualization for OOP for SPS')
    #i=0

    #path_data_1 = 'OOP_for_SPS/Final_results_Cluster0.json'
    

    #ds = 19
    #mcl = 2

    for ds in range(15,20):
        for mcl in range(2,7):
            path_data_1 = 'OOP_for_SPS/Final_results_noCluster_0_28-11-91.json'
            df_1 = load_data(path_data_1)

            path_data_2 = 'OOP_for_SPS/merged.json'
            df_2 = load_data(path_data_2)
            

            df_1 = df_1[df_1['density_scenario'] == ds]
            
            df_2 = df_2[df_2['max_speed_diff'] == 15]
            df_2 = df_2[df_2['min_cl'] == mcl]
            df_2 = df_2[df_2['density_scenario'] == ds]
            

            df_3 = pd.concat([df_1,df_2])


            plot_box(df_3,ds,mcl)
    #path_data_2 = 'OOP_for_SPS/Final_results_Cluster_v15.json'
    #df_2 = load_data(path_data_2)
    #df_2 = df_2[df_2['max_speed_diff'] == 15]
    #df_2 = df_2[df_2['min_cl'] == 2]

    #min_cl=[2,3,4,5,6] x*5 -> 10,15,20,25,30
    #max_cl=[10,15,20,25,30]
    #max_speed_diff_list=[5,10,15] 
    #max_distance_cl=[3,4,5,10,15]

    
    
    

    #df_2 = load_data(path_data_2)
    # Possibles combinaciones


    #print(df_1.head())
    #print(df_2.head())

    #print(df_1.columns)
    #print(df_2.columns)
    #print(df_2['clusters_info'][0][0])

    
    #df_3.reset_index(drop=True, inplace=True)
    #df_3['cluster'][0]=False

    #print(df_3['All_PDR_Vector'])
    #print(df_3['clusters_info'][1][1])

    

def plot_box(df,ds,mcl):
    #print(df['index'])
    df['index'] = df.index      
    
    df = df.sort_values(by='index') 
    df = df.sort_values(by='cluster') 
    
    #df=df.explode(['All_indv_VRU_AVGPDR'])         
                      
    df=df.explode(['All_PDR_Vector'])   
    
    #Crear el gráfico Boxplot color='density_scenario',
    fig = px.box(df, x='index', y='All_PDR_Vector', color='cluster' , notched=True,
                title='ALL PDR Average in Density Scenario '+ str(ds-14) +'<br> for max_speed_diff = 15%, Min Member = '+str(mcl) + ' and Max Member = '+str(mcl*5),
                labels={'ALL_PDR_avg': 'Average ALL_PDR', 'index': 'Index'},
                points='all')  # 'all' to show all points    
    #fig = px.scatter(df,x='index', y='ALL_PDR_avg', range_y=[0, 1], color='max_cl', title='Error Bar Plot') 
    fig.update_layout(xaxis_title='Maximum Distance for Cluster member [m]', yaxis_title='Average ALL_PDR', font_size=12, title_x=0.5,)
    #val = df['index'].unique()
    #print(val)
    fig.update_xaxes(tickvals=df['index'].unique(), ticktext=['N/A','3', '4', '5', '10', '15'])
    fig.update_yaxes(range=[0.5,1])


    name="images/cluster_ds_"+str(ds-14)+"_mincl_"+str(mcl)+"_PDRALLL.pdf"
    fig.write_image(name, format='pdf')
    
    #fig.show()       
    
    #fig.write_image(name, format='pdf')

 

def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T

if __name__ == '__main__':
    main()
