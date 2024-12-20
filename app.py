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
    st.title('Results visualization for OOP for SPS')

    path_data7_1 = 'OOP_for_SPS/Final_results_group9_Fitting_20Hz.json'
    df_7_1 = load_data(path_data7_1)

    path_data7_2 = 'OOP_for_SPS/Final_results_group10_Fitting_20Hz.json'
    df_7_2 = load_data(path_data7_2)
    
    

    path_data8 = 'OOP_for_SPS/Final_results_group11_Fitting_10Hz.json'
    df_8 = load_data(path_data8)

    path_data9 = 'OOP_for_SPS/Final_results_group12_Fitting_20Hz_aw500.json'
    df_9 = load_data(path_data9)

    path_data10 = 'OOP_for_SPS/Final_results_group13_Fitting_10Hz_aw500.json'
    df_10 = load_data(path_data10)

    path_data11 = 'OOP_for_SPS/Copy1_Final_resutls_group14_Fitting_20Hz_aw200.json'
    df_11 = load_data(path_data11)

    path_data12 = 'OOP_for_SPS/Final_results_group14_Fitting_20Hz_aw200.json'
    df_12 = load_data(path_data12)

    df_7 = pd.concat([df_7_1,df_7_2,df_11,df_12])

    if not os.path.exists("images"):
        os.mkdir("images")

    with st.expander('Show data 20 Hz Fitting Results'):
        st.write("Box Plot para 20Hz aw=200 ms")
        df_20Hz_1=plot_scatter4(df_7)
        #st.write(df_11)
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
        #fig6.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
        #fig6.update_yaxes(title_text='VAP', range=[0,1])

        df_20Hz_1_obs= df_20Hz_1[df_20Hz_1['obstacles']]
        df_20Hz_2_obs= df_20Hz_2[df_20Hz_2['obstacles']]
        df_10Hz_1_obs= df_10Hz_1[df_10Hz_1['obstacles']]
        df_10Hz_2_obs= df_10Hz_2[df_10Hz_2['obstacles']]

        df_20Hz_1_noobs= df_20Hz_1[~df_20Hz_1['obstacles']]
        df_20Hz_2_noobs= df_20Hz_2[~df_20Hz_2['obstacles']]
        df_10Hz_1_noobs= df_10Hz_1[~df_10Hz_1['obstacles']]
        df_10Hz_2_noobs= df_10Hz_2[~df_10Hz_2['obstacles']]

        fig6.add_trace(go.Scatter3d(y=df_20Hz_1_obs['All_indv_VRU_AVGPDR'], z=df_20Hz_1_obs['All_indv_emp_VAP'], x=df_20Hz_1_obs['density_scenario'], mode='markers', name='20Hz_aw200_obs'))
        
        fig6.add_trace(go.Scatter3d(y=df_20Hz_2_obs['All_indv_VRU_AVGPDR'], z=df_20Hz_2_obs['All_indv_emp_VAP'], x=df_20Hz_2_obs['density_scenario'], mode='markers', name='20Hz_aw500_obs'))
        fig6.add_trace(go.Scatter3d(y=df_10Hz_1_obs['All_indv_VRU_AVGPDR'], z=df_10Hz_1_obs['All_indv_emp_VAP'], x=df_10Hz_1_obs['density_scenario'], mode='markers', name='10Hz_aw200_obs'))
        fig6.add_trace(go.Scatter3d(y=df_10Hz_2_obs['All_indv_VRU_AVGPDR'], z=df_10Hz_2_obs['All_indv_emp_VAP'], x=df_10Hz_2_obs['density_scenario'], mode='markers', name='10Hz_aw500_obs'))
        
        
        fig6.add_trace(go.Scatter3d(y=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], z=df_20Hz_1_noobs['All_indv_emp_VAP'], x=df_20Hz_1_noobs['density_scenario'], mode='markers', name='20Hz_aw200_no-obs'))
        
        fig6.add_trace(go.Scatter3d(y=df_20Hz_2_noobs['All_indv_VRU_AVGPDR'], z=df_20Hz_2_noobs['All_indv_emp_VAP'], x=df_20Hz_2_noobs['density_scenario'], mode='markers', name='20Hz_aw500_no-obs'))
        fig6.add_trace(go.Scatter3d(y=df_10Hz_1_noobs['All_indv_VRU_AVGPDR'], z=df_10Hz_1_noobs['All_indv_emp_VAP'], x=df_10Hz_1_noobs['density_scenario'], mode='markers', name='10Hz_aw200_no-obs'))
        fig6.add_trace(go.Scatter3d(y=df_10Hz_2_noobs['All_indv_VRU_AVGPDR'], z=df_10Hz_2_noobs['All_indv_emp_VAP'], x=df_10Hz_2_noobs['density_scenario'], mode='markers', name='10Hz_aw500_no-obs'))
        
        fig6.update_xaxes(title_text='VRU PDR AVG', range=[0,1],tickfont_size=16, title_font=dict(size=18))
        fig6.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16, title_font=dict(size=18))
        #fig6.update_zaxes(title_text='Density Scenario')
        
        fig6.update_xaxes(autorange="reversed")

        fig6.update_layout(
            scene=dict(
                xaxis_title='Denisty Scenario',
                yaxis_title='VRU PDR AVG',
                zaxis_title='VAP',
                zaxis_range=[0,1],
                yaxis_range=[0,1],
                xaxis_autorange="reversed"
            )
            
        )

        st.plotly_chart(fig6)    
        fig6.write_image("images/fig1.pdf")

        fig9 = make_subplots(rows=1, cols=1) #px.scatter(df_20Hz_1, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
        fig9.update_traces(hovertemplate=None)

        fig9.update_xaxes(title_text='VRU PDR AVG', range=[0,1], tickfont_size=16)
        fig9.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16)
        
        fig9.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_noobs['All_indv_emp_VAP'], mode='markers', name='20Hz_aw200_no-obs', marker_color=df_20Hz_1_obs['density_scenario'], marker_colorscale='Viridis', marker_cmin=100, marker_cmax=400, marker_coloraxis='coloraxis1'))
        #fig9.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_noobs['All_indv_emp_VAP'], mode='markers', name='20Hz_aw200_no-obs', marker_color=df_20Hz_1_noobs['density_scenario']))

        fig9.add_trace(go.Scatter(x=df_20Hz_2_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_2_noobs['All_indv_emp_VAP'], marker_color=df_20Hz_2_noobs['density_scenario'], mode='markers',marker_symbol='x', name='20Hz_aw500_no-obs', marker_colorscale='Viridis', marker_coloraxis='coloraxis1'))
        fig9.add_trace(go.Scatter(x=df_10Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_10Hz_1_noobs['All_indv_emp_VAP'], marker_color=df_10Hz_1_noobs['density_scenario'], mode='markers',marker_symbol='square', name='10Hz_aw200_no-obs', marker_colorscale='Viridis', marker_coloraxis='coloraxis1'))
        fig9.add_trace(go.Scatter(x=df_10Hz_2_noobs['All_indv_VRU_AVGPDR'], y=df_10Hz_2_noobs['All_indv_emp_VAP'], marker_color=df_10Hz_2_noobs['density_scenario'], mode='markers',marker_symbol='cross', name='10Hz_aw500_no-obs', marker_colorscale='Viridis', marker_coloraxis='coloraxis1'))
        
        #lowess_1 = sm.nonparametric.lowess(df_20Hz_1_obs['All_indv_emp_VAP'], df_20Hz_1_obs['All_indv_VRU_AVGPDR'], frac=0.2)
        #lowess_2 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][no_obs], df['All_indv_VRU_AVGPDR'][no_obs], frac=0.2)
        #st.write(lowess_1)
        #fig9.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))
        #fig2.add_trace(go.Scatter(x=lowess_2[:, 0], y=lowess_2[:, 1], mode='lines', name='LOWESS Fit for no_obs', line=dict(color='blue')))
        
        # Fit the model to the data
        initial_guess = [1, 1, 1, 2]  # Initial parameter guesses
        limites_inferiores = [0, 1, 1, 0]
        limites_superiores = [2, 2, 2, 8]
        limites = (limites_inferiores, limites_superiores)
        optimized_params, _ = curve_fit(my_model,df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], df_20Hz_1_noobs['All_indv_emp_VAP'], p0=initial_guess, bounds=limites)

        
        st.write("Obtimized Parameters for model $VAP = A-B (C-PDR_{VRU})^z$",optimized_params)

        # Plot the data and the fitted curve
        #fig9.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=my_model(df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], *optimized_params), mode='lines', name='Fitted Curve model for noobs', line=dict(color='orange')))
        
        fig9.update_layout(
            width=600,
            height=500,
            legend=dict(
                x=0,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal",
                
                #font=dict(
                #    family="sans-serif",
                #    size=12,
                #    color="black"
                #),
                #bgcolor='rgba(255,255,255,0.5)',  # semi-transparent background
                #bordercolor='Black',
                #borderwidth=2
            )
        )

        st.plotly_chart(fig9)  
        fig9.write_image("images/fig1.pdf")

        fig11=fig9
        fig11.data[1].visible = False
        fig11.data[2].visible = False
        fig11.data[3].visible = False
        fig11.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=my_model(df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], *optimized_params), mode='lines', name='Fitted Curve model for noobs', line=dict(color='orange')))
        
        
        fig11.write_image("images/fig11.pdf")
        st.plotly_chart(fig11)  

        fig10 = make_subplots(rows=1, cols=1) #px.scatter(df_20Hz_1, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
        #fig10.update_traces(hovertemplate=None)

        fig10.update_xaxes(title_text='VRU PDR AVG', range=[0,1], tickfont_size=16)
        fig10.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16)
        
        fig10.add_trace(go.Scatter(x=df_20Hz_1_obs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_obs['All_indv_emp_VAP'], mode='markers', name='empiric 20Hz_aw200_obs', 
                                       marker=dict(
                                            color=df_20Hz_1_obs['density_scenario'],  # Data values for coloring
                                            colorscale='RdYlgn',  # Colorscale
                                            #cmin=100,  # Minimum bound for the colorscale
                                            #cmax=400,  # Maximum bound for the colorscale
                                            showscale=True  # Show colorscale legend
                                        )
                                    )
        )
                                  # marker_color=df_20Hz_1_obs['density_scenario'], marker_colorscale='Viridis', marker_cmin=100, marker_cmax=200)) #, marker_coloraxis='coloraxis1'))
        fig10.add_trace(go.Scatter(x=df_20Hz_1_obs['All_indv_VRU_AVGPDR'], y=my_model(df_20Hz_1_obs['All_indv_VRU_AVGPDR'], *optimized_params), mode='markers', name='Theoretical', marker_symbol='x', line=dict(color='orange')))
        fig10.update_layout(
            width=600,
            height=500,
            legend=dict(
                x=0,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                #traceorder="normal"
                
            )
        )
        st.plotly_chart(fig10)  
        fig10.write_image("images/fig1.pdf")

@st.cache_data
def plot_scatter4(df_7): 
    List_1= [[],[],[],[],[]] # density, AVG EMP VAP, AVGVRU, Obstacles        
    for item in df_7:
        #st.write(item)
        if 'density_scenario' in item:
            for j in df_7[item]:
                if j == 6:
                    List_1[0].append(800)     #Updating value in users/km^2                  
                if j == 5:
                    List_1[0].append(960)
                if j == 4:
                    List_1[0].append(1120)
                if j == 3:
                    List_1[0].append(1280)
                if j == 2:
                    List_1[0].append(1440)
                if j == 1:
                    List_1[0].append(1600)
                if j == 0:
                    List_1[0].append(1760)
                if j == 10:
                    List_1[0].append(2080)
                if j == 11:
                    List_1[0].append(2400)
                if j == 12:
                    List_1[0].append(2720)
                if j == 13:
                    List_1[0].append(3040)
                if j == 14:
                    List_1[0].append(3440)
                if j == 15:
                    List_1[0].append(3840)
                if j == 16:
                    List_1[0].append(4240)
                if j == 17:
                    List_1[0].append(4640)
                if j == 18:
                    List_1[0].append(5440)
                if j == 19:
                    List_1[0].append(6240)
                                    
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
    fig7 = px.box(df2, x='density_scenario', y='All_PDR_Vector',color='obstacles', notched=True) #,title='ALL PDR Boxplot with 95% Confidence Interval')
    fig7.update_traces(hovertemplate=None)

    #st.write(df_7_3)
    #df3_obs= df_7_3[df_7_3['obstacles']]
    #df3_noobs= df_7_3[~df_7_3['obstacles']]
    
    #fig7.add_trace(go.Bar(x=df3_obs['density_scenario'], y=df3_obs['Total_cumulative_PDR'], name='obs-cum'))
    #fig7.add_trace(go.Bar(x=df3_noobs['density_scenario'], y=df3_noobs['Total_cumulative_PDR'], name='no-obs-cum'))
    fig7.update_xaxes(title_text='Density Scenario', tickfont_size=16, title_font=dict(size=18))
    fig7.update_yaxes(title_text='PDR', range=[0,1], tickfont_size=16, title_font=dict(size=18))
    st.write('PDR for all')

    fig7.update_layout(
            legend=dict(
                x=0.9,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal")
    )
    #st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_VRU_AVGPDR','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_VRU_AVGPDR']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_VRU_AVGPDR',color='obstacles', notched=True) #, title='ALL VRU PDR Boxplot with 95% Confidence Interval') #
    fig7.update_traces(hovertemplate=None)
    fig7.update_xaxes(title_text='Density Scenario', tickfont_size=16, title_font=dict(size=18))
    fig7.update_yaxes(title_text='PDR', range=[0,1], tickfont_size=16, title_font=dict(size=18))
    st.write('PDR for VRU')

    fig7.update_layout(
            legend=dict(
                x=0.9,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal")
    )
    
    #st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_emp_VAP','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_emp_VAP']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_emp_VAP',color='obstacles', notched=True) #,title='ALL VAP PDR Boxplot with 95% Confidence Interval') # 
    fig7.update_traces(hovertemplate=None)

    fig7.update_xaxes(title_text='Density Scenario', tickfont_size=16, title_font=dict(size=18))
    fig7.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16, title_font=dict(size=18))
    st.write('VAP')

    fig7.update_layout(
            legend=dict(
                x=0.9,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal")
    )

    #st.plotly_chart(fig7)

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
