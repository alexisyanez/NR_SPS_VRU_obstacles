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
    #st.set_option('server.maxMessageSize', 600)
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

    path_data7 = 'OOP_for_SPS/Final_results_group6_Fitting_20Hz.json'
    df_7 = load_data(path_data7)




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
        st.write("First group results")
        st.write(df_4)
        st.write("Second group results")
        st.write(df_5)
        st.write("Third group results")
        st.write(df_6)
        st.write("Fourth group results")
        st.write(df_7)

    with st.expander('PDR Bar figures', expanded=True):
        # Sample data
        x_values = np.linspace(0, 6, 7)
        y_values_no_obs = [df_4['VRU_PDR_avg'][0],df_5['VRU_PDR_avg'][1],df_5['VRU_PDR_avg'][2],df_5['VRU_PDR_avg'][5],df_5['VRU_PDR_avg'][7],df_6['VRU_PDR_avg'][0],df_6['VRU_PDR_avg'][1]]
        error_values_no_obs = [df_4['VRU_PDR_std'][0],df_5['VRU_PDR_std'][1],df_5['VRU_PDR_std'][2],df_5['VRU_PDR_std'][5],df_5['VRU_PDR_std'][7],df_6['VRU_PDR_std'][0],df_6['VRU_PDR_std'][1]]
        

        y_values_obs = [df_4['VRU_PDR_avg'][3],df_5['VRU_PDR_avg'][4],df_5['VRU_PDR_avg'][6],df_5['VRU_PDR_avg'][8],df_5['VRU_PDR_avg'][9],df_6['VRU_PDR_avg'][2],df_6['VRU_PDR_avg'][3]]
        error_values_obs = [df_4['VRU_PDR_std'][3],df_5['VRU_PDR_std'][4],df_5['VRU_PDR_std'][6],df_5['VRU_PDR_std'][8],df_5['VRU_PDR_std'][9],df_6['VRU_PDR_std'][2],df_6['VRU_PDR_std'][3]]
        
               

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
        y_values_no_obs = [df_4['ALL_PDR_avg'][0],df_5['ALL_PDR_avg'][1],df_5['ALL_PDR_avg'][2],df_5['ALL_PDR_avg'][5],df_5['ALL_PDR_avg'][7],df_6['ALL_PDR_avg'][0],df_6['ALL_PDR_avg'][1]]
        error_values_no_obs = [df_4['ALL_PDR_std'][0],df_5['ALL_PDR_std'][1],df_5['ALL_PDR_std'][2],df_5['ALL_PDR_std'][5],df_5['ALL_PDR_std'][7],df_6['ALL_PDR_std'][0],df_6['ALL_PDR_std'][1]]

        y_values_no_obs_g4 = [df_7['Total_PDR_avg'][0],df_7['Total_PDR_avg'][1],df_7['Total_PDR_avg'][2],df_7['Total_PDR_avg'][5],df_7['Total_PDR_avg'][7],df_7['Total_PDR_avg'][8],df_7['Total_PDR_avg'][10]]
        error_values_no_obs_g4 = [df_7['Total_PDR_std'][0],df_7['Total_PDR_std'][1],df_7['Total_PDR_std'][2],df_7['Total_PDR_std'][5],df_7['Total_PDR_std'][7],df_7['Total_PDR_std'][8],df_7['Total_PDR_std'][10]]

        
        y_values_obs = [df_4['ALL_PDR_avg'][3],df_5['ALL_PDR_avg'][4],df_5['ALL_PDR_avg'][6],df_5['ALL_PDR_avg'][8],df_5['ALL_PDR_avg'][9],df_6['ALL_PDR_avg'][2],df_6['ALL_PDR_avg'][3]]
        error_values_obs = [df_4['ALL_PDR_std'][3],df_5['ALL_PDR_std'][4],df_5['ALL_PDR_std'][6],df_5['ALL_PDR_std'][8],df_5['ALL_PDR_std'][9],df_6['ALL_PDR_std'][2],df_6['ALL_PDR_std'][3]]
        
        y_values_obs_g4 = [df_7['Total_PDR_avg'][3],df_7['Total_PDR_avg'][4],df_7['Total_PDR_avg'][6],df_7['Total_PDR_avg'][9],df_7['Total_PDR_avg'][11],df_7['Total_PDR_avg'][12],df_7['Total_PDR_avg'][13]]
        error_values_obs_g4 = [df_7['Total_PDR_std'][3],df_7['Total_PDR_std'][4],df_5['VRU_PDR_std'][6],df_7['Total_PDR_std'][9],df_7['Total_PDR_std'][11],df_7['Total_PDR_std'][12],df_7['Total_PDR_std'][13]]

        fig4 = make_subplots(rows=1, cols=1)
        # Create the bar chart with error bars
        
        fig4.add_trace(go.Bar(x=x_values, y=y_values_no_obs, error_y=dict(type='data', array=error_values_no_obs, visible=True), name='no_obs'), row=1, col=1)
        fig4.add_trace(go.Bar(x=x_values, y=y_values_obs, error_y=dict(type='data', array=error_values_obs, visible=True), name='obs'), row=1, col=1)
        
        fig4.add_trace(go.Bar(x=x_values, y=y_values_no_obs_g4, error_y=dict(type='data', array=error_values_no_obs_g4, visible=True), name='no_obs-g6'), row=1, col=1)
        fig4.add_trace(go.Bar(x=x_values, y=y_values_obs_g4, error_y=dict(type='data', array=error_values_obs_g4, visible=True), name='obs-g6'), row=1, col=1)


        fig4.update_layout(title='Bar Plot Figures ALL AVGPDR, density_scenario = [0,1,2,3,4,5,6]',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
        st.plotly_chart(fig4)

    with st.expander('Scatter and fittings figures', expanded=True):
        
        st.write("Scatter plot for Density Scenario=6")
        plot_scatter2(df_7,0,3,6)
        st.write("Scatter plot for Density Scenario=5")
        plot_scatter2(df_7,1,4,5)
        st.write("Scatter plot for Density Scenario=4")
        plot_scatter2(df_7,2,6,4)
        st.write("Scatter plot for Density Scenario=3")
        plot_scatter2(df_7,5,9,3)
        st.write("Scatter plot for Density Scenario=2")
        plot_scatter2(df_7,7,11,2)
        st.write("Scatter plot for Density Scenario=1")
        plot_scatter2(df_7,8,12,1)
        st.write("Scatter plot for Density Scenario=0")
        plot_scatter2(df_7,10,13,0)
        
        '''
        st.write("Scatter plot for Density Scenario=6")
        plot_scatter2(df_4,0,3,6)
        st.write("Scatter plot for Density Scenario=5")
        plot_scatter2(df_5,1,4,5)
        st.write("Scatter plot for Density Scenario=4")
        plot_scatter2(df_5,2,6,4)
        st.write("Scatter plot for Density Scenario=3")
        plot_scatter2(df_5,5,8,3)
        st.write("Scatter plot for Density Scenario=2")
        plot_scatter2(df_5,7,9,2)
        st.write("Scatter plot for Density Scenario=1")
        plot_scatter2(df_6,0,2,1)
        st.write("Scatter plot for Density Scenario=0")
        plot_scatter2(df_6,1,3,0)
        '''

def plot_scatter(df, obstacles): #,nr):
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
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][no_obs], y=df['All_indv_emp_VAP'][no_obs], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][obs], y=df['All_indv_emp_VAP'][obs], mode='markers',marker=dict(symbol='star'), name='obs'), row=1, col=1)
    # Segundo subplot (gráfico de dispersión)
    fig2.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig2.update_yaxes(title_text='VAP', range=[0,1])

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