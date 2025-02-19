import streamlit as st
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

    st.set_page_config(layout='centered')
    st.title('Results visualization for Clustering in OOP for SPS')

    path_data_1 = 'OOP_for_SPS/Final_results_noCluster_0_28-11-91.json'
    df_1 = load_data(path_data_1)

    path_data_2 = 'OOP_for_SPS/Final_results_V3Cluster_15.json'
    df_2 = load_data(path_data_2)


    path_data_3 = 'OOP_for_SPS/Final_results_V3Cluster_16.json'
    df_3 = load_data(path_data_3)


    if not os.path.exists("images"):
        os.mkdir("images")

    with st.expander('Show data Cluster Results'):
        st.write("No-Cluster")
        st.write(df_1)
        st.write("Density Scenario 15")
        st.write(df_2)
        st.write("Density Scenario 16")
        st.write(df_3)
    
    with st.expander('Show PDR Box Plot for PDR'):

        st.write("No-Cluster")

        if st.session_state.get('fig') is None:
            st.session_state['speed'] = [5,10,15] #np.arange(0.0, 5.1, 0.1).round(2)    
            f = st.session_state['speed'][2]
            df_1 = df_1[df_1['max_speed_diff'] == f]
            st.session_state['fig'] = px.box(df_1, x='max_dist_clust', y='All_PDR_Vector', notched=True,
                    title='ALL PDR Average',
                    labels={'ALL_PDR_avg': 'Average ALL_PDR', 'max_dist_clust': 'maximum distance to cluster head'},
                    points='all')  # 'all' to show all points    
     
                    #fig.update_layout(xaxis_title='Maximum Distance for Cluster member [m]', yaxis_title='Average ALL_PDR', font_size=12, title_x=0.5,))

        def sldier_callback():
            f = st.session_state['slider_speed']
            x = st.session_state['fig'].data[0].x
            st.session_state['fig'].data[0].y = np.sin(f*x)
            st.session_state['fig'].data[0].name = str(f)


        f = st.select_slider(
            label='max_speed_diff', 
            options=st.session_state['speed'],
            value=2,
            on_change=sldier_callback,
            key='slider_speed'
        )

        st.plotly_chart(st.session_state['fig'])

        

        #plot_box(df_1)

        st.write("Density Scenario 15")
        obstacles = st.toggle('Obstacles', False)
        plot_box(df_2)

        st.write("Density Scenario 16")
        obstacles = st.toggle('Obstacles', False)
        plot_box(df_3)
        #st.write(df_8)

   

@st.cache_data
def plot_box(df):   
    
    #Crear el gráfico Boxplot color='density_scenario',
    #min_cl=[2,3,4,5,6]
    #max_speed_diff_list=[5,10,15] #,3,4,5,6]
    #max_distance_cl=[3,4,5,10,15] #,3,4,5,6]
    #"cluster": cl_bool,
    #"clusters_info":clusters_info,
    #"min_cl": int(mincl),
    #"max_cl": int(maxcl),
    #"max_speed_diff": int(msdcl),
    #"max_dist_clust": int(mdcl),
    #"density_scenario": int(ds_index)
    
    fig = px.box(df, x='max_dist_clust', y='All_PDR_Vector', notched=True,
                title='ALL PDR Average',
                labels={'ALL_PDR_avg': 'Average ALL_PDR', 'index': 'Index'},
                points='all')  # 'all' to show all points    
    #fig = px.scatter(df,x='index', y='ALL_PDR_avg', range_y=[0, 1], color='max_cl', title='Error Bar Plot') 
    fig.update_layout(xaxis_title='Maximum Distance for Cluster member [m]', yaxis_title='Average ALL_PDR', font_size=12, title_x=0.5,)
    #val = df['index'].unique()
    #print(val)
    fig.update_xaxes(tickvals=df['index'].unique(), ticktext=['N/A','3', '4', '5', '10', '15'])
    fig.update_yaxes(range=[0.5,1])


    #name="images/cluster_ds_"+str(ds-14)+"_mincl_"+str(mcl)+"_PDRALLL.pdf"
    #fig.write_image(name, format='pdf')

def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T

if __name__ == '__main__':
    main()
