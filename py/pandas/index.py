import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [10, 20, 30, 40, 50, 40],
    'Bounce_Rate': [20, 13, 52, 12, 53, 24]
}
stats_df = pd.DataFrame(web_stats)

print(stats_df.tail(2))

stats_df = stats_df.set_index('Day');

print(stats_df)
