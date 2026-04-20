import plotly.express as px

def create_price_chart(df, coin_name, time_label, change,
                       show_now=True,
                       show_avg=True,
                       show_high_low=False):

    fig = px.line(df, x="time", y="price")

    line_color = "#16c784" if change > 0 else "#ea3943"

    fig.update_traces(
        line=dict(color=line_color, width=2),
        hovertemplate="<b>%{y:.2f} USD</b><br>%{x|%Y-%m-%d %H:%M:%S}<extra></extra>"
    )

    latest = df["price"].iloc[-1]
    avg = df["price"].mean()
    high = df["price"].max()
    low = df["price"].min()

    if show_now:
        fig.add_hline(y=latest, line_color="#16c784", annotation_text="Now")

    if show_avg:
        fig.add_hline(y=avg, line_color="gray", line_dash="dash", annotation_text="Avg")

    if show_high_low:
        fig.add_hline(y=high, line_color="orange", line_dash="dot", annotation_text="High")
        fig.add_hline(y=low, line_color="red", line_dash="dot", annotation_text="Low")



    fig.update_layout(
        title=dict(
            text=time_label,
            x=0.5,
            font=dict(size=18, color="white")
        ),
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#e5e7eb"),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False)
    )

    return fig