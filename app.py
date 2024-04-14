import streamlit as st
import json
import pandas as pd
import plotly.express as px
#from itertools import cycle,chain
#import numpy as np

def main():
    st.set_page_config(layout='wide')
    st.title('Results visualization for OOP for SPS')

    path_data1 = 'OOP_for_SPS/Final_results_group1.json'
    df_1 = load_data(path_data1)

    path_data2 = 'OOP_for_SPS/Final_results_group2_50Hz.json'
    df_2 = load_data(path_data2)

    path_data3 = 'OOP_for_SPS/Final_results_group3_10Hz.json'
    df_3 = load_data(path_data3)

    path_data4 = 'OOP_for_SPS/Final_results_group4_Fitting_20Hz.json'
    df_4 = load_data(path_data4)

    with st.expander('Show data 10 Hz'):
        st.write(df_3)
    with st.expander('Some plots 10 Hz', expanded=True):
        #lets filter by obstacles and nr
        obstacles = st.toggle('Obstacles', False)
        #nr = st.toggle('NR', False)
        plot_scatter(df_3, obstacles)

    with st.expander('Some plots 20 Hz ', expanded=True):
        #lets filter by obstacles and nr
        obstacles1 = st.toggle('Obstacles1', False)
        #nr = st.toggle('NR', False)
        plot_scatter(df_1, obstacles1)

    with st.expander('Some plots 50 Hz', expanded=True):
        #lets filter by obstacles and nr
        obstacles2 = st.toggle('Obstacles2', False)
        #nr = st.toggle('NR', False)
        plot_scatter(df_2, obstacles2)

    with st.expander('Show data 20 Hz Fitting Results'):
        st.write(df_4)
    with st.expander('Some plots 4', expanded=True):
        #lets filter by obstacles and nr
        obstacles3 = st.toggle('Obstacles3', False)
        # nr = st.toggle('NR', False)
        plot_scatter2(df_4, obstacles3)

def plot_scatter(df, obstacles): #,nr):
    #df_toplot = (df.query(f'obstacles == {obstacles} and nr == {nr}')
    df_toplot = (df.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['emp_VAP_avg'], id_vars=['target_distance', 'awareness_window'])
                   .sort_values('awareness_window'))
    fig = px.scatter(df_toplot, x='target_distance', y='value', color='awareness_window', symbol='awareness_window', title='VAP vs Tx-Rx Distance')
    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    fig.update_yaxes(title_text='VAP')
    st.plotly_chart(fig)


def plot_scatter2(df, obstacles):
    df2=df.explode('All_indv_emp_VAP','All_indv_VRU_AVGPDR')
    #print(df2['All_indv_emp_VAP'])
    #print(df['All_indv_emp_VAP'])
    #print(df2['All_indv_VRU_AVGPDR'])
    #print(df['All_indv_VRU_AVGPDR'])
    #print(df2['obstacles'])
    #print(df['obstacles'])
    #print(df2['density_scenario'])
    #print(df['density_scenario'])

    df_toplot = (df2.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['All_indv_emp_VAP'], id_vars=['All_indv_VRU_AVGPDR', 'density_scenario'])
                   .sort_values('density_scenario'))
    fig = px.scatter(df_toplot, x='All_indv_VRU_AVGPDR', y='value', color='density_scenario', symbol='density_scenario', title='VAP vs AVG PDR Sourronding VRU')
    fig.update_xaxes(title_text='AVG PDR VRU')
    fig.update_yaxes(title_text='VAP')
    st.plotly_chart(fig)

#print()
#df_expand=df.explode('')
#a=df['All_indv_VRU_AVGPDR'][0]
#b=df['All_indv_emp_VAP'][0]
#fig = px.scatter(x=a, y=b,title='VAP vs PDR_VRU_AVG')

#fig.update_xaxes(title_text='VRU PDR AVG')
#fig.update_yaxes(title_text='VAP')
        
#st.plotly_chart(fig)


def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T


if __name__ == '__main__':
    main()