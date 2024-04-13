import streamlit as st
import json
import pandas as pd
import plotly.express as px

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
        #obstacles2 = st.toggle('Obstacles', False)
        #nr = st.toggle('NR', False)
        plot_scatter(df_2, obstacles)

    with st.expander('Some plots 4', expanded=True):
        #lets filter by obstacles and nr
        #obstacles3 = st.toggle('Obstacles', False)
        # nr = st.toggle('NR', False)
        plot_scatter2(df_4, obstacles)

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
    df_toplot = (df.query(f'obstacles == {obstacles}')
                   .melt(value_vars=['All_indv_emp_VAP'][0], id_vars=['All_indv_VRU_AVGPD'][0])) 
    fig = px.scatter(df_toplot, x='All_indv_VRU_AVGPD', y='value', title='VAP vs Tx-Rx Distance')
    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    fig.update_yaxes(title_text='VAP')
    st.plotly_chart(fig)    


def load_data(data_path):
    # I need to read some json files
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T


if __name__ == '__main__':
    main()