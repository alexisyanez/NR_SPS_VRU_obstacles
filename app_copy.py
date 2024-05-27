import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
import numpy as np
from scipy.optimize import curve_fit
#import matplotlib.pyplot as plt


def main():

    st.set_page_config(layout='centered')
    st.title('Results visualization for OOP for SPS')

    path_data1 = 'OOP_for_SPS/Final_results_group1.json'
    df_1 = load_data(path_data1)

    path_data2 = 'OOP_for_SPS/Final_results_group2_50Hz.json'
    df_2 = load_data(path_data2)

    path_data3 = 'OOP_for_SPS/Final_results_group3_10Hz.json'
    df_3 = load_data(path_data3)

    path_data4 = 'OOP_for_SPS/Final_results_group4_Fitting_20Hz_old_14-04-2024.json'
    df_4 = load_data(path_data4)

    path_data5 = 'OOP_for_SPS/Final_results_group4_Fitting_20Hz.json'
    df_5 = load_data(path_data5)

    path_data6 = 'OOP_for_SPS/Final_results_group5_ds_1_0_Fitting_20Hz.json'
    df_6 = load_data(path_data6)

    path_data7_1 = 'OOP_for_SPS/Final_results_group9_Fitting_20Hz.json'
    df_7_1 = load_data(path_data7_1)

    path_data7_2 = 'OOP_for_SPS/Final_results_group10_Fitting_20Hz.json'
    df_7_2 = load_data(path_data7_2)
    
    df_7 = pd.concat([df_7_1,df_7_2])

    path_data8 = 'OOP_for_SPS/Final_results_group11_Fitting_10Hz.json'
    df_8 = load_data(path_data8)

    '''
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
    '''
    with st.expander('Show data 20 Hz Fitting Results'):
        #st.write("First group results")
        #st.write(df_4)
        #st.write("Second group results")
        #st.write(df_5)
        #st.write("Third group results")
        #st.write(df_6)
        #st.write("Results")
        #st.write(df_7)

        st.write("Box Plot para 20Hz aw=200 ms")
        plot_scatter4(df_7)
    
    with st.expander('Show data 10 Hz Fitting Results'):

        st.write("Box Plot para 20Hz aw=200 ms")
        plot_scatter4(df_8)

def plot_scatter4(df_7): 
    List_1= [[],[],[],[],[]] # density, AVG EMP VAP, AVGVRU, Obstacles        
    for item in df_7:
        #st.write(item)
        if 'density_scenario' in item:
            for j in df_7[item]:
                if j == 6:
                    List_1[0].append(0)                        
                if j == 5:
                    List_1[0].append(1)
                if j == 4:
                    List_1[0].append(2)
                if j == 3:
                    List_1[0].append(3)
                if j == 2:
                    List_1[0].append(4)
                if j == 1:
                    List_1[0].append(5)
                if j == 0:
                    List_1[0].append(6)
                if j == 10:
                    List_1[0].append(7)
                if j == 11:
                    List_1[0].append(8)
                if j == 12:
                    List_1[0].append(9)
                if j == 13:
                    List_1[0].append(10)
                                    
            #st.write(List_1[0])
        if 'All_indv_VRU_AVGPDR' in item and not 'All_indv_VRU_AVGPDR_pair' in item :
            for j in df_7[item]:
                List_1[1].append(np.mean(j))
            #st.write(List_1[1])
        if 'All_indv_emp_VAP' in item:
            for k in df_7[item]:
                List_1[2].append(np.mean(k))
            #st.write(List_1[2])
        if 'obstacles' in item:
            for l in df_7[item]:
                List_1[3].append(l)
            #st.write(List_1[3])
        if 'VRU_PDR_avg' in item and not 'All_indv_VRU_AVGPDR_pair' in item :
            for j in df_7[item]:
                List_1[4].append(j)
        

    df = pd.DataFrame({'density_scenario': List_1[0], 'All_indv_VRU_AVGPDR': List_1[1], 'All_indv_emp_VAP': List_1[2],'obstacles': List_1[3],'VRU_PDR_avg': List_1[4]})
    # Create the boxplot
    st.write(df)
    

    #fig5 = px.scatter(df, x='VRU_PDR_avg', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
    #fig5.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    #fig5.update_yaxes(title_text='VAP', range=[0,1])
    #st.plotly_chart(fig5)
    df_7_3 = df_7[['density_scenario','All_PDR_Vector','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_PDR_Vector']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_PDR_Vector',color='obstacles', notched=True,title='ALL PDR Boxplot with 95% Confidence Interval')
    st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_VRU_AVGPDR','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_VRU_AVGPDR']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_VRU_AVGPDR',color='obstacles', notched=True, title='ALL VRU PDR Boxplot with 95% Confidence Interval') #
    st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_emp_VAP','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_emp_VAP']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_emp_VAP',color='obstacles', notched=True,title='ALL VAP PDR Boxplot with 95% Confidence Interval') # 
    st.plotly_chart(fig7)

    fig6 = px.scatter(df, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
    fig6.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig6.update_yaxes(title_text='VAP', range=[0,1])
    st.plotly_chart(fig6)              
     
    '''
    with st.expander('PDR Bar figures', expanded=True):
        # Sample data
        x_values = np.linspace(0, 6, 7)
        y_values_no_obs = [df_7['VRU_PDR_avg'][0],df_7['VRU_PDR_avg'][1],df_7['VRU_PDR_avg'][2],df_7['VRU_PDR_avg'][3],df_7['VRU_PDR_avg'][4],df_7['VRU_PDR_avg'][6],df_7['VRU_PDR_avg'][7]] #[df_4['VRU_PDR_avg'][0],df_5['VRU_PDR_avg'][1],df_5['VRU_PDR_avg'][2],df_5['VRU_PDR_avg'][5],df_5['VRU_PDR_avg'][7],df_6['VRU_PDR_avg'][0],df_6['VRU_PDR_avg'][1]]
        error_values_no_obs = [df_7['VRU_PDR_std'][0],df_7['VRU_PDR_std'][1],df_7['VRU_PDR_std'][2],df_7['VRU_PDR_std'][3],df_7['VRU_PDR_std'][4],df_7['VRU_PDR_std'][6],df_7['VRU_PDR_std'][7]]#[df_4['VRU_PDR_std'][0],df_5['VRU_PDR_std'][1],df_5['VRU_PDR_std'][2],df_5['VRU_PDR_std'][5],df_5['VRU_PDR_std'][7],df_6['VRU_PDR_std'][0],df_6['VRU_PDR_std'][1]]
        

        y_values_obs =  [df_7['VRU_PDR_avg'][5],df_7['VRU_PDR_avg'][8],df_7['VRU_PDR_avg'][9],df_7['VRU_PDR_avg'][10],df_7['VRU_PDR_avg'][11],df_7['VRU_PDR_avg'][12],df_7['VRU_PDR_avg'][13]]#[df_4['VRU_PDR_avg'][3],df_5['VRU_PDR_avg'][4],df_5['VRU_PDR_avg'][6],df_5['VRU_PDR_avg'][8],df_5['VRU_PDR_avg'][9],df_6['VRU_PDR_avg'][2],df_6['VRU_PDR_avg'][3]]
        error_values_obs =  [df_7['VRU_PDR_std'][5],df_7['VRU_PDR_std'][8],df_7['VRU_PDR_std'][9],df_7['VRU_PDR_std'][10],df_7['VRU_PDR_std'][11],df_7['VRU_PDR_std'][12],df_7['VRU_PDR_std'][13]]#[df_4['VRU_PDR_std'][3],df_5['VRU_PDR_std'][4],df_5['VRU_PDR_std'][6],df_5['VRU_PDR_std'][8],df_5['VRU_PDR_std'][9],df_6['VRU_PDR_std'][2],df_6['VRU_PDR_std'][3]]
        
               

        fig3 = make_subplots(rows=1, cols=1)
        # Create the bar chart with error bars
        
        fig3.add_trace(go.Bar(x=x_values, y=y_values_no_obs, error_y=dict(type='data', array=error_values_no_obs, visible=True), name='no_obs'), row=1, col=1)
        fig3.add_trace(go.Bar(x=x_values, y=y_values_obs, error_y=dict(type='data', array=error_values_obs, visible=True), name='obs'), row=1, col=1)

        fig3.update_layout(title='Bar Plot Figures VRU AVGPDR, density_scenario = [0,1,2,3,4,5,6]',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
        st.plotly_chart(fig3)
        
        x_values = np.linspace(0, 6, 7)
        y_values_no_obs = [df_7['ALL_PDR_avg'][0],df_7['ALL_PDR_avg'][1],df_7['ALL_PDR_avg'][2],df_7['ALL_PDR_avg'][3],df_7['ALL_PDR_avg'][4],df_7['ALL_PDR_avg'][6],df_7['ALL_PDR_avg'][7]]
        #[df_4['ALL_PDR_avg'][0],df_5['ALL_PDR_avg'][1],df_5['ALL_PDR_avg'][2],df_5['ALL_PDR_avg'][5],df_5['ALL_PDR_avg'][7],df_6['ALL_PDR_avg'][0],df_6['ALL_PDR_avg'][1]]
        error_values_no_obs = [df_7['ALL_PDR_std'][0],df_7['ALL_PDR_std'][1],df_7['ALL_PDR_std'][2],df_7['ALL_PDR_std'][3],df_7['ALL_PDR_std'][4],df_7['ALL_PDR_std'][6],df_7['ALL_PDR_std'][7]]
        #[df_4['ALL_PDR_std'][0],df_5['ALL_PDR_std'][1],df_5['ALL_PDR_std'][2],df_5['ALL_PDR_std'][5],df_5['ALL_PDR_std'][7],df_6['ALL_PDR_std'][0],df_6['ALL_PDR_std'][1]]

        y_values_no_obs_g4 = [df_7['Total_cumulative_PDR'][0],df_7['Total_cumulative_PDR'][1],df_7['Total_cumulative_PDR'][2],df_7['Total_cumulative_PDR'][3],df_7['Total_cumulative_PDR'][4],df_7['Total_cumulative_PDR'][6],df_7['Total_cumulative_PDR'][7]]
        y_values_obs_g4 = [df_7['Total_cumulative_PDR'][5],df_7['Total_cumulative_PDR'][8],df_7['Total_cumulative_PDR'][9],df_7['Total_cumulative_PDR'][10],df_7['Total_cumulative_PDR'][11],df_7['Total_cumulative_PDR'][12],df_7['Total_cumulative_PDR'][13]]
        
        #y_values_no_obs_g4 = [df_7['Total_PDR_avg'][0],df_7['Total_PDR_avg'][1],df_7['Total_PDR_avg'][2],df_7['Total_PDR_avg'][5],df_7['Total_PDR_avg'][7],df_7['Total_PDR_avg'][8],df_7['Total_PDR_avg'][10]]
        #error_values_no_obs_g4 = [df_7['Total_PDR_std'][0],df_7['Total_PDR_std'][1],df_7['Total_PDR_std'][2],df_7['Total_PDR_std'][5],df_7['Total_PDR_std'][7],df_7['Total_PDR_std'][8],df_7['Total_PDR_std'][10]]

        
        y_values_obs =  [df_7['ALL_PDR_avg'][5],df_7['ALL_PDR_avg'][8],df_7['ALL_PDR_avg'][9],df_7['ALL_PDR_avg'][10],df_7['ALL_PDR_avg'][11],df_7['ALL_PDR_avg'][12],df_7['ALL_PDR_avg'][13]]
        #[df_4['ALL_PDR_avg'][3],df_5['ALL_PDR_avg'][4],df_5['ALL_PDR_avg'][6],df_5['ALL_PDR_avg'][8],df_5['ALL_PDR_avg'][9],df_6['ALL_PDR_avg'][2],df_6['ALL_PDR_avg'][3]]
        error_values_obs =  [df_7['ALL_PDR_std'][5],df_7['ALL_PDR_std'][8],df_7['ALL_PDR_std'][9],df_7['ALL_PDR_std'][10],df_7['ALL_PDR_std'][11],df_7['ALL_PDR_std'][12],df_7['ALL_PDR_std'][13]]
        #[df_4['ALL_PDR_std'][3],df_5['ALL_PDR_std'][4],df_5['ALL_PDR_std'][6],df_5['ALL_PDR_std'][8],df_5['ALL_PDR_std'][9],df_6['ALL_PDR_std'][2],df_6['ALL_PDR_std'][3]]
        
        
        #y_values_obs_g4 = [df_7['Total_PDR_avg'][3],df_7['Total_PDR_avg'][4],df_7['Total_PDR_avg'][6],df_7['Total_PDR_avg'][9],df_7['Total_PDR_avg'][11],df_7['Total_PDR_avg'][12],df_7['Total_PDR_avg'][13]]
        #error_values_obs_g4 = [df_7['Total_PDR_std'][3],df_7['Total_PDR_std'][4],df_5['VRU_PDR_std'][6],df_7['Total_PDR_std'][9],df_7['Total_PDR_std'][11],df_7['Total_PDR_std'][12],df_7['Total_PDR_std'][13]]

        y_values_boxplot_no_obs = [df_7['All_PDR_Vector'][0],df_7['All_PDR_Vector'][1],df_7['All_PDR_Vector'][2],df_7['All_PDR_Vector'][3],df_7['All_PDR_Vector'][4],df_7['All_PDR_Vector'][6],df_7['All_PDR_Vector'][7]]
        y_values_boxplot_obs =[df_7['All_PDR_Vector'][5],df_7['All_PDR_Vector'][8],df_7['All_PDR_Vector'][9],df_7['All_PDR_Vector'][10],df_7['All_PDR_Vector'][11],df_7['All_PDR_Vector'][12],df_7['All_PDR_Vector'][13]]
        
        fig4 = make_subplots(rows=1, cols=1)
        # Create the bar chart with error bars
        
        fig4.add_trace(go.Bar(x=x_values, y=y_values_no_obs, error_y=dict(type='data', array=error_values_no_obs, visible=True), name='no_obs'), row=1, col=1)
        fig4.add_trace(go.Bar(x=x_values, y=y_values_obs, error_y=dict(type='data', array=error_values_obs, visible=True), name='obs'), row=1, col=1)
        
        fig4.add_trace(go.Bar(x=x_values, y=y_values_no_obs_g4, name='no_obs-cum'), row=1, col=1) #, error_y=dict(type='data', array=error_values_no_obs_g4, visible=True), name='no_obs-g6'), row=1, col=1)
        fig4.add_trace(go.Bar(x=x_values, y=y_values_obs_g4, name='obs-cum'), row=1, col=1) #,error_y=dict(type='data', array=error_values_obs_g4, visible=True), name='obs-g6'), row=1, col=1)

        

        fig4.update_layout(title='Bar Plot Figures ALL AVGPDR, density_scenario = [0,1,2,3,4,5,6]',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
        st.plotly_chart(fig4)
        

        list=[[],[],[]]
        for i in y_values_boxplot_no_obs:
            index=y_values_boxplot_no_obs.index(i)

            for j in i:
                list[0].append(j)
                list[1].append(index)
                list[2].append(False)

        for i in y_values_boxplot_obs:
            index=y_values_boxplot_obs.index(i)

            for j in i:
                list[0].append(j)
                list[1].append(index)
                list[2].append(True)

        df = pd.DataFrame({'val': list[0], 'den': list[1], 'obs': list[2]})
        # Create the boxplot
        fig5 = px.box(df, x='den', y='val',color='obs', notched=True,title='Boxplot with 95% Confidence Interval')
        st.plotly_chart(fig5)


      

    with st.expander('Scatter and fittings figures', expanded=True):
        
        st.write("Scatter plot for Density Scenario=6 usign pair PDR")
        plot_scatter2(df_7,0,5,6)

        st.write("Scatter plot for Density Scenario=6 using VRU centered PDR")
        plot_scatter3(df_7,0,5,6)

        #st.write("Scatter plot for PDR-VAP macro evaluation")
        #plot_scatter4(df_7,0,5,6)

        
        #st.write("Scatter plot for Density Scenario=5")
        #plot_scatter2(df_7,1,8,5)
        #st.write("Scatter plot for Density Scenario=4")
        #plot_scatter2(df_7,2,9,4)
        #st.write("Scatter plot for Density Scenario=3")
        #plot_scatter2(df_7,3,10,3)
        #st.write("Scatter plot for Density Scenario=2")
        #plot_scatter2(df_7,4,11,2)
        #st.write("Scatter plot for Density Scenario=1")
        #plot_scatter2(df_7,6,12,1)
        #st.write("Scatter plot for Density Scenario=0")
        #plot_scatter2(df_7,7,13,0)
        
        #st.write("FROM PREVIOUS RESULTS")
        
        #st.write("Scatter plot for Density Scenario=6")
        #plot_scatter2(df_4,0,3,6)
        #st.write("Scatter plot for Density Scenario=5")
        #plot_scatter2(df_5,1,4,5)
        #st.write("Scatter plot for Density Scenario=4")
        #plot_scatter2(df_5,2,6,4)
        #st.write("Scatter plot for Density Scenario=3")
        #plot_scatter2(df_5,5,8,3)
        #st.write("Scatter plot for Density Scenario=2")
        #plot_scatter2(df_5,7,9,2)
        #st.write("Scatter plot for Density Scenario=1")
        #plot_scatter2(df_6,0,2,1)
        #st.write("Scatter plot for Density Scenario=0")
        #plot_scatter2(df_6,1,3,0)
    '''

def plot_scatter(df, obstacles): #,nr):[]
    #df_toplot = (df.query(f'obstacles == {obstacles} and nr == {nr}')
    df_toplot = (df.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['emp_VAP_avg'], id_vars=['target_distance', 'awareness_window'])
                   .sort_values('awareness_window'))
    fig = px.scatter(df_toplot, x='target_distance', y='value', color='awareness_window', symbol='awareness_window', title='VAP vs Tx-Rx Distance')
    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    fig.update_yaxes(title_text='VAP')
    st.plotly_chart(fig)

def plot_scatter2(df,no_obs,obs,ds):    
    fig2 = make_subplots(rows=1, cols=1)

    # Primer subplot (gráfico de dispersión)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR_pair'][no_obs], y=df['All_indv_emp_VAP'][no_obs], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR_pair'][obs], y=df['All_indv_emp_VAP'][obs], mode='markers',marker=dict(symbol='star'), name='obs'), row=1, col=1)
    # Segundo subplot (gráfico de dispersión)
    fig2.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig2.update_yaxes(title_text='VAP', range=[0,1])
    st.write('tamaño de vectores para AVGPDR VRU'+str(len(df['All_indv_VRU_AVGPDR'][no_obs]))+'All indv emp VAP'+str(len(df['All_indv_emp_VAP'][no_obs])))

    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][obs], df['All_indv_VRU_AVGPDR_pair'][obs], frac=0.2)
    lowess_2 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][no_obs], df['All_indv_VRU_AVGPDR_pair'][no_obs], frac=0.2)
    #st.write(lowess_1)
    fig2.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))
    fig2.add_trace(go.Scatter(x=lowess_2[:, 0], y=lowess_2[:, 1], mode='lines', name='LOWESS Fit for no_obs', line=dict(color='blue')))
    
    # Fit the model to the data
    initial_guess = [1, 1, 1, 2]  # Initial parameter guesses
    limites_inferiores = [0, 1, 1, 0]
    limites_superiores = [2, 2, 2, 8]
    limites = (limites_inferiores, limites_superiores)
    optimized_params, _ = curve_fit(my_model,df['All_indv_VRU_AVGPDR_pair'][obs], df['All_indv_emp_VAP'][obs], p0=initial_guess, bounds=limites)

       
    st.write("Obtimized Parameters for model $VAP = A-B (C-PDR_{VRU})^z$",optimized_params)

    # Plot the data and the fitted curve
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR_pair'][obs], y=my_model(df['All_indv_VRU_AVGPDR_pair'][obs], *optimized_params), mode='lines', name='Fitted Curve model for obs', line=dict(color='orange')))

    fig2.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario ='+str(ds)+', LOWESS Fit for obs',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
    st.plotly_chart(fig2)

def plot_scatter3(df,no_obs,obs,ds):    
    fig2 = make_subplots(rows=1, cols=1)

    # Primer subplot (gráfico de dispersión)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][no_obs], y=df['All_indv_emp_VAP'][no_obs], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][obs], y=df['All_indv_emp_VAP'][obs], mode='markers',marker=dict(symbol='star'), name='obs'), row=1, col=1)
    # Segundo subplot (gráfico de dispersión)
    fig2.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig2.update_yaxes(title_text='VAP', range=[0,1])
    st.write('tamaño de vectores para AVGPDR VRU'+str(len(df['All_indv_VRU_AVGPDR'][no_obs]))+'All indv emp VAP'+str(len(df['All_indv_emp_VAP'][no_obs])))

    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][obs], df['All_indv_VRU_AVGPDR'][obs], frac=0.2)
    lowess_2 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][no_obs], df['All_indv_VRU_AVGPDR'][no_obs], frac=0.2)
    #st.write(lowess_1)
    fig2.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))
    fig2.add_trace(go.Scatter(x=lowess_2[:, 0], y=lowess_2[:, 1], mode='lines', name='LOWESS Fit for no_obs', line=dict(color='blue')))
    
    # Fit the model to the data
    initial_guess = [1, 1, 1, 2]  # Initial parameter guesses
    limites_inferiores = [0, 1, 1, 0]
    limites_superiores = [2, 2, 2, 8]
    limites = (limites_inferiores, limites_superiores)
    optimized_params, _ = curve_fit(my_model,df['All_indv_VRU_AVGPDR'][obs], df['All_indv_emp_VAP'][obs], p0=initial_guess, bounds=limites)

       
    st.write("Obtimized Parameters for model $VAP = A-B (C-PDR_{VRU})^z$",optimized_params)

    # Plot the data and the fitted curve
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][obs], y=my_model(df['All_indv_VRU_AVGPDR'][obs], *optimized_params), mode='lines', name='Fitted Curve model for obs', line=dict(color='orange')))

    fig2.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario ='+str(ds)+', LOWESS Fit for obs',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
    st.plotly_chart(fig2)

def my_model(x, a,b,c,z):
    return a-b*((c-x)**z)

def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T

if __name__ == '__main__':
    main()

""" import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define your model function (e.g., a polynomial, exponential, etc.)
def my_model(x, a, b, c):
    return a * np.exp(b * x) + c

# Generate some example data (replace with your actual data)
xdata = np.linspace(0, 10, 100)
ydata = my_model(xdata, 2, 0.5, 1) + np.random.normal(0, 0.1, len(xdata))

# Fit the model to the data
initial_guess = [1, 0.1, 0.5]  # Initial parameter guesses
optimized_params, _ = curve_fit(my_model, xdata, ydata, p0=initial_guess)

# Plot the data and the fitted curve
plt.scatter(xdata, ydata, label='Data')
plt.plot(xdata, my_model(xdata, *optimized_params), label='Fitted Curve', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show() 
def my_model(x, a, b, c, z):
return a-b*np.float_power((c-x),z)


#####
    fig3 = make_subplots(rows=1, cols=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][1], y=df['All_indv_emp_VAP'][1], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][4], y=df['All_indv_emp_VAP'][4], mode='markers', name='obs'), row=1, col=1)
    fig3.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig3.update_yaxes(title_text='VAP', range=[0,1])
    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][4], df['All_indv_VRU_AVGPDR'][4], frac=0.2)
    #st.write(lowess_1)
    fig3.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))

    #st.title('Grafico Scatter para Scenarios nivel de densidad = 2')
    fig3.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario = 2, LOWESS Fit for obs',
                        autosize=False,
                        width=400,
                        height=400)
    
    st.plotly_chart(fig3)
    
#####
    fig4 = make_subplots(rows=1, cols=1)
    fig4.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][2], y=df['All_indv_emp_VAP'][2], mode='markers', name='no-obs'), row=1, col=1)
    fig4.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][6], y=df['All_indv_emp_VAP'][6], mode='markers', name='obs'), row=1, col=1)
    # Tercer subplot (gráfico de dispersión)
    #fig2.add_trace(go.Scatter(x=[0, 1, 2], y=[10, 20, 30]), row=1, col=3)
    fig4.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig4.update_yaxes(title_text='VAP', range=[0,1])
    # Mostrar los subplots en Streamlit
    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][6], df['All_indv_VRU_AVGPDR'][6], frac=0.2)
    #st.write(lowess_1)
    fig4.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))

    #st.title('Grafico Scatter para Scenarios nivel de densidad = 3')
    fig4.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario = 3, LOWESS Fit for obs',
                        autosize=False,
                        width=500,
                        height=500)
    st.plotly_chart(fig4)

#####
    fig5 = make_subplots(rows=1, cols=1)
    fig5.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][5], y=df['All_indv_emp_VAP'][5], mode='markers', name='no-obs'), row=1, col=1)
    fig5.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][8], y=df['All_indv_emp_VAP'][8], mode='markers', name='obs'), row=1, col=1)
    # Tercer subplot (gráfico de dispersión)
    #fig2.add_trace(go.Scatter(x=[0, 1, 2], y=[10, 20, 30]), row=1, col=3)
    fig5.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig5.update_yaxes(title_text='VAP', range=[0,1])
    # Mostrar los subplots en Streamlit
    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][8], df['All_indv_VRU_AVGPDR'][8], frac=0.2)
    #st.write(lowess_1)
    fig5.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))

    #st.title('Grafico Scatter para Scenarios nivel de densidad = 3')
    fig5.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario = 4, LOWESS Fit for obs',
                        autosize=False,
                        width=500,
                        height=500)
    st.plotly_chart(fig5)

#####
    fig6 = make_subplots(rows=1, cols=1)
    fig6.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][7], y=df['All_indv_emp_VAP'][7], mode='markers', name='no-obs'), row=1, col=1)
    fig6.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][9], y=df['All_indv_emp_VAP'][9], mode='markers', name='obs'), row=1, col=1)
    # Tercer subplot (gráfico de dispersión)
    #fig2.add_trace(go.Scatter(x=[0, 1, 2], y=[10, 20, 30]), row=1, col=3)
    fig6.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig6.update_yaxes(title_text='VAP', range=[0,1])
    # Mostrar los subplots en Streamlit
    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][9], df['All_indv_VRU_AVGPDR'][9], frac=0.2)
    #st.write(lowess_1)
    fig6.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))

    #st.title('Grafico Scatter para Scenarios nivel de densidad = 3')
    fig6.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario = 5, LOWESS Fit for obs',
                        autosize=False,
                        width=800,
                        height=800)
    st.plotly_chart(fig6)

"""