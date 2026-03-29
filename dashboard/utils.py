import streamlit as st
import plotly.express as px


def plot_bar_chart(df=None, x=None, y=None, subheader=None, info=None, is_orientation_h=False, key=None):
    st.subheader(subheader)
    if is_orientation_h:
        fig = px.bar(
            data_frame=df, x=x, y=y, orientation='h', 
            title="", template="plotly_white", color=x, color_continuous_scale='Blues'
        ) 
    else:
        fig = px.bar(
            data_frame=df, x=x, y=y,
            title="", template="plotly_white", color=x, color_continuous_scale='Blues'
        )
    fig.update_xaxes(title_text=None)
    fig.update_yaxes(title_text=None)
    fig.update_layout(yaxis=dict(autorange="reversed"))
    
    event_prod = st.plotly_chart(fig, on_select="rerun", selection_mode="points", key=key)
    
    if len(event_prod.selection["points"]) > 0:
        idx = event_prod.selection["points"][0]["point_index"]
        filter = df.iloc[idx][y]
        st.info(f"{info}: **{filter}**")
        st.dataframe(df[df[y] == filter].head(50), height=300)