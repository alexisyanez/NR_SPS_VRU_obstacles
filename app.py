import streamlit as st
import json
import pandas as pd
import plotly.express as px

def main():
    st.set_page_config(layout='wide')
    st.title('Results visualization for OOP for SPS')
    df = load_data()
    with st.expander('Show data'):
        st.write(df)
    with st.expander('Some plots', expanded=True):
        #lets filter by obstacles and nr
        obstacles = st.toggle('Obstacles', False)
        nr = st.toggle('NR', False)
        plot_scatter(df, obstacles, nr)


def plot_scatter(df, obstacles, nr):
    df_toplot = df.query(f'obstacles == {obstacles} and nr == {nr}').melt(value_vars=['emp_VAP_avg'], id_vars=['target_distance', 'awareness_window'])
    st.write(df_toplot.head())
    fig = px.scatter(df_toplot, x='target_distance', y='value', color='awareness_window', symbol='awareness_window')
    fig.update_xaxes(title_text='Tx-Rx Distance (m)')
    fig.update_yaxes(title_text='VAP')
    st.plotly_chart(fig)


def load_data():
    # I need to read some json files
    with open('OOP_for_SPS/Final_results_group1.json') as f:
        data = json.load(f)
    return pd.DataFrame(data).T


if __name__ == '__main__':
    main()