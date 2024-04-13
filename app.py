import streamlit as st
import json
import pandas as pd
import plotly.express as px
import ast 

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
    # Convertir la cadena en una lista real
    df_toplot = (df.query(f'obstacles == {obstacles}')
                    .melt(value_vars=['All_indv_emp_VAP'], id_vars=['All_indv_VRU_AVGPDR', 'density_scenario'])
                    .sort_values('density_scenario'))
    fig = px.scatter(df_toplot, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP', trendline="linear", exponent=-1, color='density_scenario', symbol='density_scenario', title='VAP vs PDR VRU average')
    fig.update_xaxes(range=[0, 1],title_text='PDR')
    fig.update_yaxes(range=[0, 1],title_text='VAP')
    st.plotly_chart(fig)

    #df['All_indv_emp_VAP'] = df['All_indv_emp_VAP'].apply(ast.literal_eval)
    #a = df['All_indv_emp_VAP'].iloc[0]
    
    #df['All_indv_VRU_AVGPDR'] = df['All_indv_VRU_AVGPDR'].apply(ast.literal_eval)
    #b=df['All_indv_VRU_AVGPDR'].iloc[0]

    #a_concatenated = [item for sublist in a for item in sublist]
    #b_concatenated = [item for sublist in b for item in sublist]
    # Crear el gráfico de dispersión con Plotly
    #fig = px.scatter(x=b[0], y=[0], title='VAP vs Tx-Rx Distance')
    #fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    #fig.update_yaxes(title_text='VAP')

    # Mostrar el gráfico
    #st.plotly_chart(fig)

#def plot_scatter2(df, obstacles):
#    df_toplot = [df['All_indv_emp_VAP'][0],['All_indv_VRU_AVGPDR'][0]]#(df.query(f'obstacles == {obstacles}')
                #   .melt(value_vars=['All_indv_emp_VAP'][0], id_vars=['All_indv_VRU_AVGPDR'][0])) 
#    fig = px.scatter(df_toplot, x='All_indv_VRU_AVGPDR', y='All_indv_emp_VAP', title='VAP vs Tx-Rx Distance')
#    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
#    fig.update_yaxes(title_text='VAP')
#    st.plotly_chart(fig)    


def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T


if __name__ == '__main__':
    main()