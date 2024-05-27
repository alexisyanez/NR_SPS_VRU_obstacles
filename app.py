import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
import numpy as np
from scipy.optimize import curve_fit

def main():

    st.set_page_config(layout='centered')
    st.title('Results visualization for OOP for SPS')

    path_data7_1 = 'OOP_for_SPS/Final_results_group9_Fitting_20Hz.json'
    df_7_1 = load_data(path_data7_1)

    path_data7_2 = 'OOP_for_SPS/Final_results_group10_Fitting_20Hz.json'
    df_7_2 = load_data(path_data7_2)
    
    df_7 = pd.concat([df_7_1,df_7_2])

    path_data8 = 'OOP_for_SPS/Final_results_group11_Fitting_10Hz.json'
    df_8 = load_data(path_data8)

    path_data9 = 'OOP_for_SPS/Final_results_group12_Fitting_20Hz_aw500.json'
    df_9 = load_data(path_data9)

    path_data10 = 'OOP_for_SPS/Final_results_group13_Fitting_10Hz_aw500.json'
    df_10 = load_data(path_data10)

    with st.expander('Show data 20 Hz Fitting Results'):
        st.write("Box Plot para 20Hz aw=200 ms")
        df_20Hz_1=plot_scatter4(df_7)
        #st.write(df_7)
    
    with st.expander('Show data 10 Hz Fitting Results'):

        st.write("Box Plot para 20Hz aw=200 ms")
        df_10Hz_1=plot_scatter4(df_8)
        #st.write(df_8)

    with st.expander('Show data 20 Hz Fitting Results AW=500 ms'):

        st.write("Box Plot para 20Hz aw=500 ms")
        df_20Hz_2=plot_scatter4(df_9)
        #st.write(df_8)
    with st.expander('Show data 10 Hz Fitting Results AW=500 ms'):

        st.write("Box Plot para 10Hz aw=500 ms")
        df_10Hz_2=plot_scatter4(df_10)
        #st.write(df_8)

    with st.expander('Scatter Plot VAP v/s AVG VRU PDR'):

        fig6 = make_subplots(rows=1, cols=1) #px.scatter(df_20Hz_1, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
        fig6.update_traces(hovertemplate=None)
        fig6.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
        fig6.update_yaxes(title_text='VAP', range=[0,1])

        df_20Hz_1_obs= df_20Hz_1[df_20Hz_1['obstacles']]
        df_20Hz_2_obs= df_20Hz_2[df_20Hz_2['obstacles']]
        df_10Hz_1_obs= df_10Hz_1[df_10Hz_1['obstacles']]
        df_10Hz_2_obs= df_10Hz_2[df_10Hz_2['obstacles']]

        df_20Hz_1_noobs= df_20Hz_1[~df_20Hz_1['obstacles']]
        df_20Hz_2_noobs= df_20Hz_2[~df_20Hz_2['obstacles']]
        df_10Hz_1_noobs= df_10Hz_1[~df_10Hz_1['obstacles']]
        df_10Hz_2_noobs= df_10Hz_2[~df_10Hz_2['obstacles']]

        fig6.add_trace(go.Scatter(x=df_20Hz_1_obs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_obs['All_indv_emp_VAP'],mode='markers', name='20Hz_aw200_obs'))
        fig6.add_trace(go.Scatter(x=df_20Hz_2_obs['All_indv_VRU_AVGPDR'], y=df_20Hz_2_obs['All_indv_emp_VAP'],mode='markers', name='20Hz_aw500_obs'))
        fig6.add_trace(go.Scatter(x=df_10Hz_1_obs['All_indv_VRU_AVGPDR'], y=df_10Hz_1_obs['All_indv_emp_VAP'],mode='markers', name='10Hz_aw200_obs'))
        fig6.add_trace(go.Scatter(x=df_10Hz_2_obs['All_indv_VRU_AVGPDR'], y=df_10Hz_2_obs['All_indv_emp_VAP'],mode='markers', name='10Hz_aw500_obs'))
        
        
        fig6.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_noobs['All_indv_emp_VAP'],mode='markers', name='20Hz_aw200_no-obs'))
        fig6.add_trace(go.Scatter(x=df_20Hz_2_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_2_noobs['All_indv_emp_VAP'],mode='markers', name='20Hz_aw500_no-obs'))
        fig6.add_trace(go.Scatter(x=df_10Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_10Hz_1_noobs['All_indv_emp_VAP'],mode='markers', name='10Hz_aw200_no-obs'))
        fig6.add_trace(go.Scatter(x=df_10Hz_2_noobs['All_indv_VRU_AVGPDR'], y=df_10Hz_2_noobs['All_indv_emp_VAP'],mode='markers', name='10Hz_aw500_no-obs'))

        st.plotly_chart(fig6)     
@st.cache_data
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
    #st.write(df)
    
    df_7_3 = df_7[['density_scenario','All_PDR_Vector','obstacles','Total_cumulative_PDR']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_PDR_Vector']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_PDR_Vector',color='obstacles', notched=True,title='ALL PDR Boxplot with 95% Confidence Interval')
    fig7.update_traces(hovertemplate=None)

    #st.write(df_7_3)
    #df3_obs= df_7_3[df_7_3['obstacles']]
    #df3_noobs= df_7_3[~df_7_3['obstacles']]
    
    #fig7.add_trace(go.Bar(x=df3_obs['density_scenario'], y=df3_obs['Total_cumulative_PDR'], name='obs-cum'))
    #fig7.add_trace(go.Bar(x=df3_noobs['density_scenario'], y=df3_noobs['Total_cumulative_PDR'], name='no-obs-cum'))
    
    st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_VRU_AVGPDR','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_VRU_AVGPDR']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_VRU_AVGPDR',color='obstacles', notched=True, title='ALL VRU PDR Boxplot with 95% Confidence Interval') #
    fig7.update_traces(hovertemplate=None)
    st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_emp_VAP','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_emp_VAP']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_emp_VAP',color='obstacles', notched=True,title='ALL VAP PDR Boxplot with 95% Confidence Interval') # 
    fig7.update_traces(hovertemplate=None)
    st.plotly_chart(fig7)

    return df

             
     

@st.cache_data
def plot_scatter(df, obstacles): #,nr):[]
    #df_toplot = (df.query(f'obstacles == {obstacles} and nr == {nr}')
    df_toplot = (df.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['emp_VAP_avg'], id_vars=['target_distance', 'awareness_window'])
                   .sort_values('awareness_window'))
    fig = px.scatter(df_toplot, x='target_distance', y='value', color='awareness_window', symbol='awareness_window', title='VAP vs Tx-Rx Distance',hover_data=False)
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
