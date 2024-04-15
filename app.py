import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
#import sys
#from itertools import cycle,chain
#import numpy as np

def main():
    #st.set_option('server.maxMessageSize', 600)
    st.set_page_config(layout='centered')
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
        #obstacles3 = st.toggle('Obstacles3', False)
        # nr = st.toggle('NR', False)
        plot_scatter2(df_4)

def plot_scatter(df, obstacles): #,nr):
    #df_toplot = (df.query(f'obstacles == {obstacles} and nr == {nr}')
    df_toplot = (df.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['emp_VAP_avg'], id_vars=['target_distance', 'awareness_window'])
                   .sort_values('awareness_window'))
    fig = px.scatter(df_toplot, x='target_distance', y='value', color='awareness_window', symbol='awareness_window', title='VAP vs Tx-Rx Distance')
    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    fig.update_yaxes(title_text='VAP')
    st.plotly_chart(fig)


def plot_scatter2(df):    
    fig2 = make_subplots(rows=1, cols=1)

    # Primer subplot (gráfico de dispersión)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][0], y=df['All_indv_emp_VAP'][0], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][3], y=df['All_indv_emp_VAP'][3], mode='markers',marker=dict(symbol='star'), name='obs'), row=1, col=1)
    # Segundo subplot (gráfico de dispersión)
    fig2.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig2.update_yaxes(title_text='VAP', range=[0,1])

    # Compute LOWESS fit
    lowess_1 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][3], df['All_indv_VRU_AVGPDR'][3], frac=0.2)
    #st.write(lowess_1)
    fig2.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))
    
    fig2.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario = 1, LOWESS Fit for obs',
                        autosize=False,
                        width=800,
                        height=800,)
    st.plotly_chart(fig2)


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
                        width=800,
                        height=800,)
    
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
                        width=800,
                        height=800,)
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
                        width=800,
                        height=800,)
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
                        height=800,)
    st.plotly_chart(fig6)


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