#import modules
import seaborn as sns

#shadow plot
def shadow_plot(df,title=None,angle=45):
    """Create shadow/missingness plot. 

    Args:
        df (df): Pandas dataframe to create plot for.
        title (str, optional): Add title to plot. Defaults to None.
        angle (int, optional): Change angle of variable names at top of plot. Defaults to 45 degrees.

    Returns:
        Shadow/missingness plot.
    """
    
    fig = sns.heatmap(df.isnull(),cmap="binary",cbar_kws={"label":"Black square (1) = NaN"})
    fig.xaxis.tick_top()
    fig.set_xticklabels(fig.get_xticklabels(),rotation=angle,ha="left")
    if title != None:
        fig.set_title(title)
    return fig