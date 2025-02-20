import streamlit as st
import json
import pandas as pd
import plotly.express as px
import numpy as np
import os

def main():
    st.set_page_config(layout='centered')
    st.title('Results visualization for Clustering in OOP for SPS')

    path_data_1 = 'OOP_for_SPS/Final_results_noCluster_0_28-11-91.json'
    df_1 = load_data(path_data_1)

    path_data_2 = 'OOP_for_SPS/Final_results_V3Cluster_15.json'
    df_2 = load_data(path_data_2)

    path_data_3 = 'OOP_for_SPS/Final_results_V3Cluster_16.json'
    df_3 = load_data(path_data_3)

    if not os.path.exists("images"):
        os.mkdir("images")

    with st.expander('Show data Cluster Results'):
        st.write("No-Cluster")
        st.write(df_1)
        st.write("Density Scenario 15")
        st.write(df_2)
        st.write("Density Scenario 16")
        st.write(df_3)
    
    with st.expander('Show PDR Box Plot for PDR'):
        st.write("No-Cluster")

        df_1=df_1.explode(['All_PDR_Vector'])   

        df_1['index'] = df_1.index 

        fig2 = px.box(
            df_1, 
            x='index', 
            y='All_PDR_Vector', 
            notched=True,
            title='ALL PDR Average for no-clustering',
            labels={'ALL_PDR_avg': 'Average ALL_PDR','index': 'Index'},
            points='all'
        )
        fig2.update_layout(
            xaxis_title='index', 
            yaxis_title='Average ALL_PDR', 
            font_size=12, 
            title_x=0.5
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.write("Trying Explode VAP Only for No-cluster")

        # Mostrar spinner mientras se carga el gráfico
        #with st.spinner('Generando el gráfico, por favor espera...'):
        # df_1_2=df_1.explode(['All_indv_emp_VAP'])   

        # df_1_2['index'] = df_1_2.index 

        # fig2_1 = px.box(
        #     df_1_2, 
        #     x='index', 
        #     y='All_indv_emp_VAP', 
        #     notched=True,
        #     title='ALL Individual Empiric VAP for no-clustering',
        #     labels={'All_indv_emp_VAP': 'Average All_indv_emp_VAP','index': 'Index'},
        #     points= False
        # )
        # fig2_1.update_layout(
        #     xaxis_title='index', 
        #     yaxis_title='Emp VAP', 
        #     font_size=12, 
        #     title_x=0.5
        # )

        # st.plotly_chart(fig2_1,use_container_width=True)
        # #st.success('¡Gráfico generado con éxito!')

        st.write("Density Scenario 15")

        df_2=df_2.explode(['All_PDR_Vector'])   

        # Slider for selecting max_speed_diff
        selected_speed = st.select_slider(
            label='Select max_speed_diff', 
            options=[5, 10, 15], 
            value=10,
            key='slider_speed'
        )

        # Filter the DataFrame based on the slider value
        filtered_df = df_2[df_2['max_speed_diff'] == selected_speed]

        # Check for missing columns or NaN values
        #print(filtered_df.columns)  # Debugging line
        if filtered_df.empty:
            st.error("No data available for the selected speed.")
            return

        # Ensure correct data types
        filtered_df.loc[:, 'max_dist_clust'] = pd.to_numeric(filtered_df['max_dist_clust'], errors='coerce')
        filtered_df.loc[:, 'All_PDR_Vector'] = pd.to_numeric(filtered_df['All_PDR_Vector'], errors='coerce')

        # Drop rows with NaN values in important columns
        filtered_df = filtered_df.dropna(subset=['max_dist_clust', 'All_PDR_Vector'])

        # For to show a better X-axis
        #mapping = {3: 1, 4: 2, 5: 3, 10: 4, 15: 5}

        # Plot the Boxplot
        fig = px.box(
            filtered_df, 
            x='max_dist_clust', 
            y='All_PDR_Vector', 
            notched=True,
            title=f'ALL PDR Average for max_speed_diff = {selected_speed}',
            labels={'ALL_PDR_avg': 'Average ALL_PDR', 'max_dist_clust': 'Maximum Distance to Cluster Head'},
            points='all'
        )
        fig.update_layout(
            xaxis_title='Maximum Distance for Cluster member [m]', 
            yaxis_title='Average ALL_PDR', 
            font_size=12, 
            title_x=0.5
        )

        fig.update_xaxes(
            tickvals=[3, 4, 5, 10, 15],  # Values to appear on X-axis
            ticktext=[str(val) for val in [3, 4, 5, 10, 15]],  # Corresponding tick labels
            tickmode='array',  # Ensure you are using the specified tickvals and ticktext
            type='category'  # This will treat the x-axis as categorical, bringing ticks closer together
        )

        fig.update_yaxes(range=[0.8,1.05])

        st.plotly_chart(fig,use_container_width=True)

        ## VAP metric

        df_2_1=df_2.explode(['All_indv_emp_VAP'])   

        # # Slider for selecting max_speed_diff
        # selected_speed_1 = st.select_slider(
        #     label='Select max_speed_diff', 
        #     options=[5, 10, 15], 
        #     value=10,
        #     key='slider_speed_1'
        # )

        # # Filter the DataFrame based on the slider value
        # filtered_df_1_2 = df_2_1[df_2_1['max_speed_diff'] == selected_speed_1]

        # # Check for missing columns or NaN values
        # print(filtered_df_1_2.columns)  # Debugging line
        # if filtered_df_1_2.empty:
        #     st.error("No data available for the selected speed.")
        #     return

        # # Ensure correct data types
        # filtered_df_1_2.loc[:, 'max_dist_clust'] = pd.to_numeric(filtered_df_1_2['max_dist_clust'], errors='coerce')
        # filtered_df_1_2.loc[:, 'All_indv_emp_VAP'] = pd.to_numeric(filtered_df_1_2['All_indv_emp_VAP'], errors='coerce')

        # # Drop rows with NaN values in important columns
        # filtered_df_1_2 = filtered_df_1_2.dropna(subset=['max_dist_clust', 'All_indv_emp_VAP'])

        # # For to show a better X-axis
        # #mapping = {3: 1, 4: 2, 5: 3, 10: 4, 15: 5}

        # # Plot the Boxplot
        # fig_1 = px.box(
        #     filtered_df_1_2, 
        #     x='max_dist_clust', 
        #     y='All_indv_emp_VAP', 
        #     notched=True,
        #     title=f'ALL PDR Average for max_speed_diff = {selected_speed_1}',
        #     labels={'All_indv_emp_VAP': 'Average ALL_PDR_indv_emp_VAP', 'max_dist_clust': 'Maximum Distance to Cluster Head'},
        #     points='all'
        # )
        # fig_1.update_layout(
        #     xaxis_title='Maximum Distance for Cluster member [m]', 
        #     yaxis_title='Average All_indv_emp_VAP', 
        #     font_size=12, 
        #     title_x=0.5
        # )

        # fig_1.update_xaxes(
        #     tickvals=[3, 4, 5, 10, 15],  # Values to appear on X-axis
        #     ticktext=[str(val) for val in [3, 4, 5, 10, 15]],  # Corresponding tick labels
        #     tickmode='array',  # Ensure you are using the specified tickvals and ticktext
        #     type='category'  # This will treat the x-axis as categorical, bringing ticks closer together
        # )

        # fig_1.update_yaxes(range=[0.9,1.1])

        # st.plotly_chart(fig_1)

        
        #plot_box(df_2)

        st.write("Density Scenario 16")

        df_3=df_3.explode(['All_PDR_Vector'])   

        # Slider for selecting max_speed_diff
        selected_speed_2 = st.select_slider(
            label='Select max_speed_diff', 
            options=[5, 10, 15], 
            value=10,
            key='slider_speed_2'
        )

        # Filter the DataFrame based on the slider value
        filtered_df_2 = df_3[df_3['max_speed_diff'] == selected_speed_2]

        # Check for missing columns or NaN values
        #print(filtered_df_2.columns)  # Debugging line
        if filtered_df_2.empty:
            st.error("No data available for the selected speed.")
            return

        # Ensure correct data types
        filtered_df_2.loc[:, 'max_dist_clust'] = pd.to_numeric(filtered_df_2['max_dist_clust'], errors='coerce')
        filtered_df_2.loc[:, 'All_PDR_Vector'] = pd.to_numeric(filtered_df_2['All_PDR_Vector'], errors='coerce')

        # Drop rows with NaN values in important columns
        filtered_df_2 = filtered_df_2.dropna(subset=['max_dist_clust', 'All_PDR_Vector'])

        # Plot the Boxplot
        fig3 = px.box(
            filtered_df_2, 
            x='max_dist_clust', 
            y='All_PDR_Vector', 
            notched=True,
            title=f'ALL PDR Average for max_speed_diff = {selected_speed_2}',
            labels={'ALL_PDR_avg': 'Average ALL_PDR', 'max_dist_clust': 'Maximum Distance to Cluster Head'},
            points='all'
        )
        fig3.update_layout(
            xaxis_title='Maximum Distance for Cluster member [m]', 
            yaxis_title='Average ALL_PDR', 
            font_size=12, 
            title_x=0.5
        )

        fig3.update_xaxes(
            tickvals=[3, 4, 5, 10, 15],  # Values to appear on X-axis
            ticktext=[str(val) for val in [3, 4, 5, 10, 15]],  # Corresponding tick labels
            tickmode='array',  # Ensure you are using the specified tickvals and ticktext
            type='category'  # This will treat the x-axis as categorical, bringing ticks closer together
        )

        fig3.update_yaxes(range=[0.8,1.05])

        st.plotly_chart(fig3,use_container_width=True)
        #plot_box(df_3)

        ## VAP metric

        # df_3_1=df_3.explode(['All_indv_emp_VAP'])   

        # # Slider for selecting max_speed_diff
        # selected_speed_2_1 = st.select_slider(
        #     label='Select max_speed_diff', 
        #     options=[5, 10, 15], 
        #     value=10,
        #     key='slider_speed_2_1'
        # )

        # # Filter the DataFrame based on the slider value
        # filtered_df_2_1 = df_3_1[df_3_1['max_speed_diff'] == selected_speed_2_1]

        # # Check for missing columns or NaN values
        # print(filtered_df_2_1.columns)  # Debugging line
        # if filtered_df_2_1.empty:
        #     st.error("No data available for the selected speed.")
        #     return

        # # Ensure correct data types
        # filtered_df_2_1.loc[:, 'max_dist_clust'] = pd.to_numeric(filtered_df_1_2['max_dist_clust'], errors='coerce')
        # filtered_df_2_1.loc[:, 'All_indv_emp_VAP'] = pd.to_numeric(filtered_df_1_2['All_indv_emp_VAP'], errors='coerce')

        # # Drop rows with NaN values in important columns
        # filtered_df_2_1 = filtered_df_2_1.dropna(subset=['max_dist_clust', 'All_indv_emp_VAP'])

        # # For to show a better X-axis
        # #mapping = {3: 1, 4: 2, 5: 3, 10: 4, 15: 5}

        # # Plot the Boxplot
        # fig3_1 = px.box(
        #     filtered_df_2_1, 
        #     x='max_dist_clust', 
        #     y='All_indv_emp_VAP', 
        #     notched=True,
        #     title=f'ALL PDR Average for max_speed_diff = {selected_speed_2_1}',
        #     labels={'All_indv_emp_VAP': 'Average ALL_PDR_indv_emp_VAP', 'max_dist_clust': 'Maximum Distance to Cluster Head'},
        #     points='all'
        # )
        # fig3_1.update_layout(
        #     xaxis_title='Maximum Distance for Cluster member [m]', 
        #     yaxis_title='Average All_indv_emp_VAP', 
        #     font_size=12, 
        #     title_x=0.5
        # )

        # fig3_1.update_xaxes(
        #     tickvals=[3, 4, 5, 10, 15],  # Values to appear on X-axis
        #     ticktext=[str(val) for val in [3, 4, 5, 10, 15]],  # Corresponding tick labels
        #     tickmode='array',  # Ensure you are using the specified tickvals and ticktext
        #     type='category'  # This will treat the x-axis as categorical, bringing ticks closer together
        # )

        # fig3_1.update_yaxes(range=[0.9,1.1])

        # st.plotly_chart(fig3_1)





@st.cache_data
def plot_box(df):   
    fig = px.box(df, x='max_dist_clust', y='All_PDR_Vector', notched=True,
                title='ALL PDR Average',
                labels={'ALL_PDR_avg': 'Average ALL_PDR', 'max_dist_clust': 'Maximum Distance to Cluster Head'},
                points='all')  
    fig.update_layout(xaxis_title='Maximum Distance for Cluster member [m]', yaxis_title='Average ALL_PDR', font_size=12, title_x=0.5)
    fig.update_yaxes(range=[0.5,1])
    st.plotly_chart(fig)


def load_data(data_path):
    with open(data_path) as f:
        data = json.load(f)
    return pd.DataFrame(data).T


if __name__ == '__main__':
    main()
