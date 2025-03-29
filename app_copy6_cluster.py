#import streamlit as st
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
    i=0

    path_data_1 = 'OOP_for_SPS/Final_results_noCluster_0_28-11-91.json'
    df_1 = load_data(path_data_1)

    path_data_2 = 'OOP_for_SPS/Final_results_V3Cluster_15.json'
    df_2 = load_data(path_data_2)

    path_data_3 = 'OOP_for_SPS/Final_results_V3Cluster_16.json'
    df_3 = load_data(path_data_3)

    path_data_4 = 'OOP_for_SPS/Final_results_V3Cluster_17.json'
    df_4 = load_data(path_data_4)

    path_data_5 = 'OOP_for_SPS/Final_results_V3Cluster_18-19.json'
    df_5 = load_data(path_data_5)

    path_data_6 = 'OOP_for_SPS/Final_results_V4Cluster_20Hz.json'
    df_6 = load_data(path_data_6)

    path_data_6_LD = 'OOP_for_SPS/Final_results_V5-Cluster_20Hz_LD.json'
    df_6_LD_1 = load_data(path_data_6_LD)

    path_data_7_LD = 'OOP_for_SPS/Final_results_V6-No-Cluster_20Hz_LD.json'
    df_7_LD_1 = load_data(path_data_7_LD)

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

    path_data13 = 'OOP_for_SPS/Final_results_group15_Fitting_20Hz_aw200_half_build.json' #Copy1_Final_resutls_group14_Fitting_20Hz_aw200.json'
    df_13 = load_data(path_data13)

    path_data14 = 'OOP_for_SPS/Final_results_group17_Fitting_20Hz_aw200_half_build_saturation.json' #Final_results_group14_Fitting_20Hz_aw200.json'

    df_14 = load_data(path_data14)
    
    df_14_group = df_14.groupby('density_scenario').agg({'All_indv_VRU_AVGPDR': lambda x: list(x), 'All_indv_emp_VAP': lambda x: list(x), 'obstacles': lambda x: list(x), 'VRU_PDR_avg': lambda x: list(x)}).reset_index()
    
    #print(df_14_group['All_indv_emp_VAP'][1])
    Sat_mean=[[],[]]
    for item in df_14_group['All_indv_emp_VAP'][0]:
        Sat_mean[0].append(np.mean(item))
    for item in df_14_group['All_indv_emp_VAP'][1]:
        Sat_mean[1].append(np.mean(item))
    
    Sat_18=np.mean(Sat_mean[0])
    Sat_19=np.mean(Sat_mean[1])

    #print(Sat_18)
    #print(Sat_19)

    Sat_mean_x=[[],[]]
    for item in df_14_group['All_indv_VRU_AVGPDR'][0]:
        Sat_mean_x[0].append(np.mean(item))
    for item in df_14_group['All_indv_VRU_AVGPDR'][1]:
        Sat_mean_x[1].append(np.mean(item))
    Sat_x18=np.mean(Sat_mean_x[0])
    Sat_x19=np.mean(Sat_mean_x[1])
    

    df_7 = pd.concat([df_7_1,df_7_2,df_11,df_12])
    fil_7 = df_7[(df_7['obstacles'] == True) & (df_7['density_scenario'] < 15) ]

    df_7_1=fil_7.explode(['All_PDR_Vector'])
    df_7_1['index'] = df_7_1.index 

    df_7_LD=ds_KM(df_7_LD_1)
    df_7_LD=df_7_LD.explode(['All_PDR_Vector'])
    df_7_LD['index'] = df_7_LD.index 
    df_s_7LD=df_7_LD.sort_values(by='density_scenario')

    df_s=df_6.sort_values(by='density_scenario')
    
    fil_df6=df_s.explode(['All_PDR_Vector'])
    fil_df6['index'] = fil_df6.index 

    df_s_LD=df_6_LD_1.sort_values(by='density_scenario')
    
    fil_df6_LD=df_s_LD.explode(['All_PDR_Vector'])
    fil_df6_LD['index'] = fil_df6_LD.index       

    fig2_7 = px.box(
        df_s_7LD, 
        x='density_scenario', 
        y='All_PDR_Vector', 
        notched=True,
        #title='ALL PDR Average for no-clustering',
        labels={'ALL_PDR_avg': 'Average ALL_PDR','index': 'Index'}
        #points='all'
    )
    fig2_7.update_layout(
        xaxis_title='Density x 10^3 [users/Km^2]', 
        yaxis_title='Average ALL_PDR', 
        font_size=12, 
        title_x=0.5
    )

    #fig2_7.update_xaxes(
    #tickvals=['15','16','17','18','19'],
    #ticktext=['3.84','4.24','4.64','5.44','6.24']
    #)
    
    name="images/fig7.pdf"
    #fig2_7.write_image(name, format='pdf')
    fig2_7.show()
    #fil_df6=df_6.explode(['All_PDR_Vector'])
    #fil_df6['index'] = fil_df6.index 

    fig4 = px.box(
        fil_df6_LD, 
        x='min_cl', 
        y='All_PDR_Vector', 
        notched=True,
        #title='ALL PDR Average for max_speed_diff DS 18-19 ',
        labels={'ALL_PDR_avg': 'Average ALL_PDR', 'min_cl': 'Cluster Size'},
        #points='all',
        color='density_scenario'
    )
    fig4.update_layout(
        xaxis_title='Cluster Size [Min,Max] members', 
        yaxis_title='Average ALL_PDR',         
        font_size=12, 
        title_x=0.5,
        legend_title_text='Density x10^3 <br>[users/Km^2]',
        legend=dict(
            x=0.05,  # x=0.5 and y=0.5 will place the legend in the center
            y=0.2,
            orientation='h',
        )
    )
  
    '''
    fig4.update_yaxes(range=[0.85,1])
    fig4.update_traces(name='3.84', selector=dict(name='15'))
    fig4.update_traces(name='4.24', selector=dict(name='16'))
    fig4.update_traces(name='4.64', selector=dict(name='17'))
    fig4.update_traces(name='5.44', selector=dict(name='18'))
    fig4.update_traces(name='6.24', selector=dict(name='19'))

    fig4.update_xaxes(
    tickvals=['2','3','4','5','6'],
    ticktext=['[2,10]','[3,15]','[4,20]','[5,25]','[6,30]']
    )
    name="images/fig8.pdf"
    fig4.write_image(name, format='pdf')
    '''
    fig4.show()
    fil_df6_LD = fil_df6_LD[fil_df6_LD['density_scenario'] != 3]
    fil_df6_LD = fil_df6_LD[fil_df6_LD['density_scenario'] != 5]
    fil_df6_LD = fil_df6_LD[fil_df6_LD['density_scenario'] != 1]
    fil_df6_LD = fil_df6_LD[fil_df6_LD['min_cl'] == 2]
    fil_df6_LD['cluster'] = True 
    fil_df6_LD=ds_KM(fil_df6_LD)
    df_s_7LD['cluster'] = False     
    df_fil2 = pd.concat([df_s_7LD,fil_df6_LD])


  

    fig2_8 = px.box(
        df_fil2, 
        x='density_scenario', 
        y='All_PDR_Vector', 
        notched=True,
        #title='ALL PDR Average for no-clustering',
        labels={'ALL_PDR_avg': 'Average ALL_PDR','index': 'Index'},
        color='cluster'
        #points='all'
    )
    fig2_8.update_layout(
        xaxis_title='Density x 10^3 [users/Km^2]', 
        yaxis_title='Average ALL_PDR', 
        font_size=12, 
        title_x=0.5
    )

    fig2_8.show()

    
    #min_cl=[2,3,4,5,6]
    #max_cl=[10,15,20,25,30]
    

    fil_8 = df_7_LD_1 #[(df_7_LD_1['obstacles'] == False)]

    fil_9=plot_scatter4(fil_8,2)

    fil_44 = df_6_LD_1[(df_6_LD_1['min_cl'] == 5)]
    fil_10 = plot_scatter4(fil_44,3)
    #fil_10 = plot_scatter4(fil_df6_LD,3)
    initial_guess = [1, 1, 1, 2]  # Initial parameter guesses
    limites_inferiores = [0, 1, 1, 0]
    limites_superiores = [2, 2, 2, 8]
    limites = (limites_inferiores, limites_superiores)
    optimized_params, _ = curve_fit(my_model,fil_9['All_indv_VRU_AVGPDR'], fil_9['All_indv_emp_VAP'], p0=initial_guess, bounds=limites)

    print(optimized_params)
    #st.write("Obtimized Parameters for model $VAP = A-B (C-PDR_{VRU})^z$",optimized_params)

    data = {'All_indv_VRU_AVGPDR': np.linspace(0, 1, num=50)}
    a2 = pd.DataFrame(data)

    fig15 = make_subplots(rows=1, cols=1)
    fig15.update_xaxes(title_text='VRU PDR AVG', range=[0,1], tickfont_size=16)
    fig15.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16)   

    fig15.add_trace(go.Scatter(x=a2['All_indv_VRU_AVGPDR'], y=my_model(a2['All_indv_VRU_AVGPDR'], *optimized_params), mode='lines', name='Model', line=dict(color='orange')))
    
    

    
    x2=fil_10['All_indv_VRU_AVGPDR']
    a=my_model(x2, *optimized_params)
    #print(fil_10)

    fig15.add_trace(go.Scatter(x=x2, y=a, mode='markers', name='cluster', 
                                    marker=dict(
                                        color=fil_10['density_scenario'],  # Data values for coloring
                                        colorscale='bluered',  # Colorscale
                                        showscale=True,  # Show colorscale legend
                                        size = 12,
                                        symbol='x'
                                    )
                                )
    )

    n_f9=fil_9[(fil_9['density_scenario'] < 3.8)]
    #print(n_f9)
    x3=n_f9['All_indv_VRU_AVGPDR']
    a5=my_model(x3, *optimized_params)

    fig15.add_trace(go.Scatter(x=x3, y=a5, mode='markers', name='no-cluster', 
                                    marker=dict(
                                        color=n_f9['density_scenario'],  # Data values for coloring
                                        colorscale='bluered',  # Colorscale
                                        showscale=True,  # Show colorscale legend
                                        size = 8
                                    )
                                )
    )

    fig15.update_layout(
        width=600,
        height=500,
        legend=dict(
            x=0,  # x=0.5 and y=0.5 will place the legend in the center
            y=1,
            #traceorder="normal",            
            #font=dict(
            #    family="sans-serif",
            #    size=12,
            #    color="black"
            #),
            #bgcolor='rgba(255,255,255,0.5)',  # semi-transparent background
            #bordercolor='Black',
            #borderwidth=2
        ),
        margin=dict(l=50, r=100, b=100, t=100, pad=4),
        coloraxis_colorbar=dict(
            title= "Density x10^3 [users/Km^2]"#, #dict(
                #text=
                #side="right",                  
                #side='right',
                #orientation= "v"
            #tickvals=[1,2,3,4,5,6],
            #ticktext=["1","2","3","4","5","6"],
            #lenmode="pixels", len=100,
            #)
        ),
        annotations=[
            dict(
                x=1.21,
                y=0.5,
                xref="paper",
                yref="paper",
                text="Density x 10^3 [users/Km^2]",
                textangle= -90,
                showarrow=False,
                #arrowhead=2
            )
        ]
    )
    name="images/fig9.pdf"
    #fig15.write_image(name, format='pdf')
    
    fig15.show()

    #fig4.show()
    #fig2_7.show()
    #fig15.show()


    # Plot the data and the fitted curve
    """ fig9 = go.Figure(data=go.Scatter(x=fil_9['All_indv_VRU_AVGPDR'], y=my_model(fil_9['All_indv_VRU_AVGPDR'], *optimized_params), mode='lines', name='Fitted Curve model for noobs', line=dict(color='orange')))
 
"""
   
    
def ds_KM(df):
    #Will remove the ds: {1.6,1.28,0.96}    
    df=df[df['density_scenario'] != 3]
    df=df[df['density_scenario'] != 5]
    df=df[df['density_scenario'] != 1]

    for i in range(len(df['density_scenario'])):
        if df['density_scenario'][i] == 6:
            df['density_scenario'][i] = 0.800
        #if df['density_scenario'][i] == 5:
            #df=df[df['density_scenario'] != 5]
            #df['density_scenario'][i] = 0.960
        if df['density_scenario'][i] == 4:
            df['density_scenario'][i] = 1.120
        #if df['density_scenario'][i] == 3:            
            #df['density_scenario'][i] = 1.280
        if df['density_scenario'][i] == 2:
            df['density_scenario'][i] = 1.440
        #if df['density_scenario'][i] == 1:            
            #df['density_scenario'][i] = 1.600
        if df['density_scenario'][i] == 0:
            df['density_scenario'][i] = 1.760
        if df['density_scenario'][i] == 10:
            df['density_scenario'][i] = 2.080
        if df['density_scenario'][i] == 11:
            df['density_scenario'][i] = 2.400
        if df['density_scenario'][i] == 12:
            df['density_scenario'][i] = 2.720
        if df['density_scenario'][i] == 13:
            df['density_scenario'][i] = 3.040
        if df['density_scenario'][i] == 14:
            df['density_scenario'][i] = 3.440
        if df['density_scenario'][i] == 15:
            df['density_scenario'][i] = 3.840
        if df['density_scenario'][i] == 16:
            df['density_scenario'][i] = 4.240
        if df['density_scenario'][i] == 17:
            df['density_scenario'][i] = 4.640
        if df['density_scenario'][i] == 18:
            df['density_scenario'][i] = 5.440
        if df['density_scenario'][i] == 19:
            df['density_scenario'][i] = 6.240            
    return df

def plot_scatter4(df_7,ind): 
    List_1= [[],[],[],[],[]] # density, AVG EMP VAP, AVGVRU, Obstacles     
    df_7=df_7[df_7['density_scenario'] != 3]
    df_7=df_7[df_7['density_scenario'] != 5]
    df_7=df_7[df_7['density_scenario'] != 1]   
    for item in df_7:
        #st.write(item)
        if 'density_scenario' in item:
            for j in df_7[item]:
                if j == 6:
                    List_1[0].append(0.800)     #Updating value in users/km^2                  
                if j == 5:
                    List_1[0].append(0.960) #9.960) #0.960
                if j == 4:
                    List_1[0].append(1.120)
                if j == 3:
                    List_1[0].append(1.280) #10.280) #1.280
                if j == 2:
                    List_1[0].append(1.440)
                if j == 1:
                    List_1[0].append(1.600) #10.600) #1.600
                if j == 0:
                    List_1[0].append(1.760)
                if j == 10:
                    List_1[0].append(2.080)
                if j == 11:
                    List_1[0].append(2.400)
                if j == 12:
                    List_1[0].append(2.720)
                if j == 13:
                    List_1[0].append(3.040)
                if j == 14:
                    List_1[0].append(3.440)
                if j == 15:
                    List_1[0].append(3.840)
                if j == 16:
                    List_1[0].append(4.240)
                if j == 17:
                    List_1[0].append(4.640)
                if j == 18:
                    List_1[0].append(5.440)
                if j == 19:
                    List_1[0].append(6.240)
                                    
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
    fig7.update_xaxes(title_text='Density x10^3 [users/Km^2]',range=[0.5,6.5], tickfont_size=16, title_font=dict(size=18))
    fig7.update_yaxes(title_text='PDR', range=[0,1], tickfont_size=16, title_font=dict(size=18))
    #st.write('PDR for all')

    fig7.update_layout(
            legend=dict(
                x=0.8,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal")
    )
    #st.plotly_chart(fig7)
    name="images/-fig6-"+str(ind)+"_PDRALLL.pdf"
    #fig7.write_image(name, format='pdf')
    #fig7.show()

    df_7_3 = df_7[['density_scenario','All_indv_VRU_AVGPDR','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_VRU_AVGPDR']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_VRU_AVGPDR',color='obstacles', notched=True) #, title='ALL VRU PDR Boxplot with 95% Confidence Interval') #
    fig7.update_traces(hovertemplate=None)
    fig7.update_xaxes(title_text='Density Scenario', tickfont_size=16, title_font=dict(size=18))
    fig7.update_yaxes(title_text='PDR', range=[0,1], tickfont_size=16, title_font=dict(size=18))
    #st.write('PDR for VRU')

    fig7.update_layout(
            legend=dict(
                x=0.8,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal")
    )
    #name="images/fig6-"+ind+"_1.pdf"
    #fig7.write_image("name", format='pdf')
    #st.plotly_chart(fig7)

    df_7_3 = df_7[['density_scenario','All_indv_emp_VAP','obstacles']] #'All_indv_emp_VAP','All_indv_VRU_AVGPDR',        
    df_7_3.loc[:,'density_scenario']=df['density_scenario'].values                   
    df2 = df_7_3.explode(['All_indv_emp_VAP']) #,'All_indv_emp_VAP']) #pd.DataFrame({'density_scenario': [[0, 1], [3, 4]], 'All_indv_VRU_AVGPDR': [1, 3], 'All_indv_emp_VAP': [[2, 4], [6, 8]],'obstacles': [True, False],'VRU_PDR_avg':[5,6]})
    fig7 = px.box(df2, x='density_scenario', y='All_indv_emp_VAP',color='obstacles', notched=True) #,title='ALL VAP PDR Boxplot with 95% Confidence Interval') # 
    fig7.update_traces(hovertemplate=None)

    fig7.update_xaxes(title_text='Density x10^3 [users/Km^2]', range=[0.5,6.5], tickfont_size=16, title_font=dict(size=18))
    fig7.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16, title_font=dict(size=18))
    #st.write('VAP')

    fig7.update_layout(
            legend=dict(
                x=0.8,  # x=0.5 and y=0.5 will place the legend in the center
                y=1,
                traceorder="normal")
    )

    #st.plotly_chart(fig7)
    name="images/4-fig6-"+str(ind)+"_VAPVRU.pdf"
    #fig7.write_image(name, format='pdf')
    #fig7.show()

    return df


'''     

    df_20Hz_1=plot_scatter4(df_7,i)
    i=i+1
        #st.write(df_11)
        #st.write(df_7)
    
    #with st.expander('Show data 10 Hz Fitting Results'):

    #st.write("Box Plot para 20Hz aw=200 ms")
    df_10Hz_1=plot_scatter4(df_8,i)
    i=i+1
        #st.write(df_8)

    #with st.expander('Show data 20 Hz Fitting Results AW=500 ms'):

    #st.write("Box Plot para 20Hz aw=500 ms")
    df_20Hz_2=plot_scatter4(df_9,i)
    i=i+1
        #st.write(df_8)
    
    #with st.expander('Show data 10 Hz Fitting Results AW=500 ms'):

    #    st.write("Box Plot para 10Hz aw=500 ms")
    df_10Hz_2=plot_scatter4(df_10,i)
    i=i+1
        #st.write(df_8)
    
    #with st.expander('Scatter Plot VAP v/s AVG VRU PDR'):
    df_20Hz_HalfBuild_AW200=plot_scatter4(df_15,i)
    i=i+1

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
    
    fig6.add_trace(go.Scatter3d(y=df_20Hz_HalfBuild_AW200['All_indv_VRU_AVGPDR'], z=df_20Hz_HalfBuild_AW200['All_indv_emp_VAP'], x=df_20Hz_HalfBuild_AW200['density_scenario'], mode='markers', name='20Hz_aw200_half-obs'))
        
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

    #    st.plotly_chart(fig6)    

    #fig6.write_image("images/4-fig2.pdf", format='pdf')
    fig6.show()

    fig9 = make_subplots(rows=1, cols=1) #px.scatter(df_20Hz_1, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
    #fig9.update_traces(hovertemplate=None)

    fig9.update_xaxes(title_text='VRU PDR AVG', range=[0,1], tickfont_size=16)
    fig9.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16)
    
    fig9.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_noobs['All_indv_emp_VAP'],mode='markers', name='20Hz_aw200_no-obs',
                                marker=dict(
                                    color=df_20Hz_1_obs['density_scenario'],
                                    colorscale="bluered",  # Specify the color scale here
                                    #cmin=100,
                                    #cmax=400,
                                    showscale=True, 
                                    #coloraxis='coloraxis1',
                                    size=12,
                                    opacity=0.7
                                )
                            )
    ) 
    #mode='markers', name='20Hz_aw200_no-obs', marker_color=df_20Hz_1_obs['density_scenario'], marker_colorscale='RdYlgn', marker_coloraxis='coloraxis1',marker_size=12, marker_opacity=0.7)) #marker_cmin=100, marker_cmax=400,
    #fig9.add_trace(go.Scatter(x=df_20Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_noobs['All_indv_emp_VAP'], mode='markers', name='20Hz_aw200_no-obs', marker_color=df_20Hz_1_noobs['density_scenario']))

    fig9.add_trace(go.Scatter(x=df_20Hz_2_noobs['All_indv_VRU_AVGPDR'], y=df_20Hz_2_noobs['All_indv_emp_VAP'], marker_color=df_20Hz_2_noobs['density_scenario'], mode='markers',marker_symbol='x', name='20Hz_aw500_no-obs', marker_colorscale="bluered", marker_size=12, marker_opacity=0.7)) # marker_coloraxis='coloraxis1', Colorscale Viridis
    fig9.add_trace(go.Scatter(x=df_10Hz_1_noobs['All_indv_VRU_AVGPDR'], y=df_10Hz_1_noobs['All_indv_emp_VAP'], marker_color=df_10Hz_1_noobs['density_scenario'], mode='markers',marker_symbol='square', name='10Hz_aw200_no-obs', marker_colorscale="bluered", marker_size=12 , marker_opacity=0.7)) # marker_coloraxis='coloraxis1',
    fig9.add_trace(go.Scatter(x=df_10Hz_2_noobs['All_indv_VRU_AVGPDR'], y=df_10Hz_2_noobs['All_indv_emp_VAP'], marker_color=df_10Hz_2_noobs['density_scenario'], mode='markers',marker_symbol='cross', name='10Hz_aw500_no-obs', marker_colorscale="bluered", marker_size=12 , marker_opacity=0.7)) # marker_coloraxis='coloraxis1', 
    
    #fig9.add_trace(go.Scatter(x=df_20Hz_HalfBuild_AW200['All_indv_VRU_AVGPDR'], y=df_20Hz_HalfBuild_AW200['All_indv_emp_VAP'], marker_color=df_20Hz_HalfBuild_AW200['density_scenario'], mode='markers',marker_symbol='cross', name='20Hz_aw500_no-obs', marker_colorscale="bluered", marker_size=12 , marker_opacity=0.7)) # marker_coloraxis='coloraxis1', 
    

        #lowess_1 = sm.nonparametric.lowess(df_20Hz_1_obs['All_indv_emp_VAP'], df_20Hz_1_obs['All_indv_VRU_AVGPDR'], frac=0.2)
        #lowess_2 = sm.nonparametric.lowess(df['All_indv_emp_VAP'][no_obs], df['All_indv_VRU_AVGPDR'][no_obs], frac=0.2)
        #st.write(lowess_1)
        #fig9.add_trace(go.Scatter(x=lowess_1[:, 0], y=lowess_1[:, 1], mode='lines', name='LOWESS Fit for obs', line=dict(color='red')))
        #fig2.add_trace(go.Scatter(x=lowess_2[:, 0], y=lowess_2[:, 1], mode='lines', name='LOWESS Fit for no_obs', line=dict(color='blue')))
        
        # Fit the model to the data

    #st.plotly_chart(fig11)  

    fig10 = make_subplots(rows=1, cols=1) #px.scatter(df_20Hz_1, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
    #fig10.update_traces(hovertemplate=None)

    fig10.update_xaxes(title_text='VRU PDR AVG', range=[0,1], tickfont_size=16)
    fig10.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16)
    
    fig10.add_trace(go.Scatter(x=df_20Hz_1_obs['All_indv_VRU_AVGPDR'], y=df_20Hz_1_obs['All_indv_emp_VAP'], mode='markers', name='Empiric', 
                                    marker=dict(
                                        color=df_20Hz_1_obs['density_scenario'],  # Data values for coloring
                                        colorscale='bluered',  # Colorscale
                                        #cmin=100,  # Minimum bound for the colorscale
                                        #cmax=400,  # Maximum bound for the colorscale
                                        showscale=True,  # Show colorscale legend
                                        size = 12,
                                    )
                                )
    )
    
                                # marker_color=df_20Hz_1_obs['density_scenario'], marker_colorscale='Viridis', marker_cmin=100, marker_cmax=200)) #, marker_coloraxis='coloraxis1'))
    
    #fig10.add_trace(go.Scatter(x=df_20Hz_HalfBuild_AW200['All_indv_VRU_AVGPDR'], y=df_20Hz_HalfBuild_AW200['All_indv_emp_VAP'], mode='markers', name='empiric 20Hz_aw200_half-obs', 
    #                                marker=dict(
    #                                    color=df_20Hz_HalfBuild_AW200['density_scenario'],  # Data values for coloring
    #                                    colorscale='bluered',  # Colorscale
    #                                    #cmin=100,  # Minimum bound for the colorscale
    #                                    #cmax=400,  # Maximum bound for the colorscale
    #                                    showscale=True,  # Show colorscale legend
    #                                    size = 12,
    #                                    symbol='x'
    #                                )
    #                            )
    #)
       
    fig10.add_trace(go.Scatter(x=df_20Hz_1_obs['All_indv_VRU_AVGPDR'], y=my_model(df_20Hz_1_obs['All_indv_VRU_AVGPDR'], *optimized_params), mode='markers', name='Theoretical', marker_symbol='cross', marker_size = 10,line=dict(color='orange')))
    fig10.add_trace(go.Scatter(x=a['All_indv_VRU_AVGPDR'], y=my_model(a['All_indv_VRU_AVGPDR'], *optimized_params), mode='lines', name='Fitted curve', line=dict(color='orange')))
    fig10.update_layout(
        width=600,
        height=500,
        legend=dict(
            x=0,  # x=0.5 and y=0.5 will place the legend in the center
            y=1,
            traceorder="normal",            
        ),
        margin=dict(l=50, r=100, b=100, t=100, pad=4),
        annotations=[
            dict(
                x=1.2,
                y=0.5,
                xref="paper",
                yref="paper",
                text="Density x 10^3 [users/Km^2]",
                textangle= -90,
                showarrow=False,
                #arrowhead=2
            )
        ],
        #margin=dict(l=100, r=110, b=100, t=100, pad=4),
        #coloraxis_colorbar=dict(
        #    title=dict(
        #        text='Density x10^3 [users/Km^2]',
        #        side="right"                  
                #side='right',
                #orientation= "v"
            #tickvals=[1,2,3,4,5,6],
            #ticktext=["1","2","3","4","5","6"],
            #lenmode="pixels", len=100,
        #    )
        #)
    )
    #st.plotly_chart(fig10)  
    #fig10.write_image("images/4-fig5.pdf", format='pdf')
    fig10.show()


    a=my_model(df_20Hz_1_obs['All_indv_VRU_AVGPDR'], *optimized_params)
    x2=np.array(df_20Hz_HalfBuild_AW200['All_indv_VRU_AVGPDR'])
    x2=np.append(x2,[Sat_x18,Sat_x19])

    b=my_model(x2 , *optimized_params)
    
    P_o=df_20Hz_1_obs['All_indv_emp_VAP'].reset_index()
    P_h=df_20Hz_HalfBuild_AW200['All_indv_emp_VAP'].reset_index()

    predicted_obs=np.array(P_o['All_indv_emp_VAP'])

    predicted_half_obs=np.array(P_h['All_indv_emp_VAP'])

    predicted_half_obs= np.append(predicted_half_obs,[Sat_18,Sat_19])
    actual=np.array(a)
    actual_b=np.array(b)
    rmse_obs = np.sqrt(((predicted_obs - actual) ** 2).mean())
    rmse_half_obs = np.sqrt(((predicted_half_obs - actual_b) ** 2).mean())

    print("Vector half-building")
    print(len(predicted_half_obs))
    print("Vector all-building")
    print(len(df_20Hz_1_obs['All_indv_VRU_AVGPDR']))
    print("Vector theoretical")
    print(len(my_model(df_20Hz_1_obs['All_indv_VRU_AVGPDR'], *optimized_params)))
    print(len(actual_b))

    print(predicted_obs)
    print(predicted_half_obs)
    print(actual) #df_77['Predicted'])
    print(rmse_obs)
    print(rmse_half_obs)

    mse_1 = np.mean((actual - predicted_obs) ** 2)
    print("Mean Squared Error (MSE) obs:", mse_1)

# Calcular el Mean Absolute Error (MAE)
    mae_1 = np.mean(np.abs(actual - predicted_obs))
    print("Mean Absolute Error (MAE) obs:", mae_1)
    
    mse_2 = np.mean((actual_b - predicted_half_obs) ** 2)
    print("Mean Squared Error (MSE) half-obs:", mse_2)

# Calcular el Mean Absolute Error (MAE)
    mae_2 = np.mean(np.abs(actual_b - predicted_half_obs))
    print("Mean Absolute Error (MAE) half-obs:", mae_2)

# Mismo grafico pero con half-obs
    data = {'All_indv_VRU_AVGPDR': np.linspace(0, 1, num=50)}
    a2 = pd.DataFrame(data)

    fig15 = make_subplots(rows=1, cols=1) #px.scatter(df_20Hz_1, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP',color='obstacles', symbol='obstacles', title='VAP v/s VRU PDR through scenarios') # notched=True,
    #fig10.update_traces(hovertemplate=None)

    fig15.update_xaxes(title_text='VRU PDR AVG', range=[0,1], tickfont_size=16)
    fig15.update_yaxes(title_text='VAP', range=[0,1], tickfont_size=16)   
    
    #new_df=pd.DataFrame({'star_time':["0","0"], 'end_time':["0","0"], 'Total_cumulative_PDR':[0,0], 'All_PDR_Vector':[0,0], 'ALL_PDR_std': [0,0], 'VRU_PDR_avg':[0,0] ,'VRU_PDR_std':[0,0],'All_indv_emp_VAP':[0,0],'All_indv_VRU_AVGPDR':[0,0], 'All_indv_VRU_AVGPDR_pair': [0,0], 'All_VAP_emp_avg':[0,0], 'obstacles':[True, True], 'density_scenario':[5.440,6.240] })
    
    df_20Hz_HalfBuild_AW200.loc[len(df_20Hz_HalfBuild_AW200)] = [5.440, None, None, None, None]  # Agregar el primer valor
    df_20Hz_HalfBuild_AW200.loc[len(df_20Hz_HalfBuild_AW200)] = [6.240, None, None, None, None]  # Agregar el segundo valor
    
    fig15.add_trace(go.Scatter(x=x2, y=predicted_half_obs, mode='markers', name='Empiric', 
                                    marker=dict(
                                        color=df_20Hz_HalfBuild_AW200['density_scenario'],  # Data values for coloring
                                        colorscale='bluered',  # Colorscale
                                        showscale=True,  # Show colorscale legend
                                        size = 12,
                                        symbol='x'
                                    )
                                )
    )
       
    fig15.add_trace(go.Scatter(x=x2, y=my_model(x2, *optimized_params), mode='markers', name='Theoretical', marker_symbol='cross', marker_size = 10,line=dict(color='orange')))
    fig15.add_trace(go.Scatter(x=a2['All_indv_VRU_AVGPDR'], y=my_model(a2['All_indv_VRU_AVGPDR'], *optimized_params), mode='lines', name='Fitted curve', line=dict(color='orange')))
    fig15.update_layout(
        width=600,
        height=500,
        legend=dict(
            x=0,  
            y=1,
            traceorder="normal",            
        ),
        margin=dict(l=50, r=100, b=100, t=100, pad=4),
        annotations=[
            dict(
                x=1.2,
                y=0.5,
                xref="paper",
                yref="paper",
                text="Density x 10^3 [users/Km^2]",
                textangle= -90,
                showarrow=False,
            )
        ],
    )
    #fig15.write_image("images/4-fig6.pdf", format='pdf')
    fig15.show()

#@st.cache_data

             
     

#@st.cache_data
def plot_scatter(df, obstacles): #,nr):[]
    #df_toplot = (df.query(f'obstacles == {obstacles} and nr == {nr}')
    df_toplot = (df.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['emp_VAP_avg'], id_vars=['target_distance', 'awareness_window'])
                   .sort_values('awareness_window'))
    fig = px.scatter(df_toplot, x='target_distance', y='value', color='awareness_window', symbol='awareness_window', title='VAP vs Tx-Rx Distance',hover_data=False)
    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    fig.update_yaxes(title_text='VAP')
#    st.plotly_chart(fig)

def plot_scatter2(df,no_obs,obs,ds):    
    fig2 = make_subplots(rows=1, cols=1)

    # Primer subplot (gráfico de dispersión)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR_pair'][no_obs], y=df['All_indv_emp_VAP'][no_obs], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR_pair'][obs], y=df['All_indv_emp_VAP'][obs], mode='markers',marker=dict(symbol='star'), name='obs'), row=1, col=1)
    # Segundo subplot (gráfico de dispersión)
    fig2.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig2.update_yaxes(title_text='VAP', range=[0,1])
#    st.write('tamaño de vectores para AVGPDR VRU'+str(len(df['All_indv_VRU_AVGPDR'][no_obs]))+'All indv emp VAP'+str(len(df['All_indv_emp_VAP'][no_obs])))

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

       
#    st.write("Obtimized Parameters for model $VAP = A-B (C-PDR_{VRU})^z$",optimized_params)

    # Plot the data and the fitted curve
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR_pair'][obs], y=my_model(df['All_indv_VRU_AVGPDR_pair'][obs], *optimized_params), mode='lines', name='Fitted Curve model for obs', line=dict(color='orange')))

    fig2.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario ='+str(ds)+', LOWESS Fit for obs',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
#    st.plotly_chart(fig2)

def plot_scatter3(df,no_obs,obs,ds):    
    fig2 = make_subplots(rows=1, cols=1)

    # Primer subplot (gráfico de dispersión)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][no_obs], y=df['All_indv_emp_VAP'][no_obs], mode='markers', name='no-obs'), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][obs], y=df['All_indv_emp_VAP'][obs], mode='markers',marker=dict(symbol='star'), name='obs'), row=1, col=1)
    # Segundo subplot (gráfico de dispersión)
    fig2.update_xaxes(title_text='VRU PDR AVG', range=[0,1])
    fig2.update_yaxes(title_text='VAP', range=[0,1])
#    st.write('tamaño de vectores para AVGPDR VRU'+str(len(df['All_indv_VRU_AVGPDR'][no_obs]))+'All indv emp VAP'+str(len(df['All_indv_emp_VAP'][no_obs])))

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

       
#    st.write("Obtimized Parameters for model $VAP = A-B (C-PDR_{VRU})^z$",optimized_params)

    # Plot the data and the fitted curve
    fig2.add_trace(go.Scatter(x=df['All_indv_VRU_AVGPDR'][obs], y=my_model(df['All_indv_VRU_AVGPDR'][obs], *optimized_params), mode='lines', name='Fitted Curve model for obs', line=dict(color='orange')))

    fig2.update_layout(title='Scatter Plot Figures VAP v/s VRU AVGPDR, density_scenario ='+str(ds)+', LOWESS Fit for obs',
                        autosize=False,
                        width=600,
                        height=500)
                        #legend=dict(x=0.3, y=0.1))
       
#    st.plotly_chart(fig2)
'''

def my_model(x, a,b,c,z):
    return a-b*((c-x)**z)


def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T


if __name__ == '__main__':
    main()
