import plotly.express as px

def plot_price_trend(data, crop):
    if data.empty:
        return None
    fig = px.line(data, x="date", y="price", title=f"Price Trend for {crop}")
    return fig