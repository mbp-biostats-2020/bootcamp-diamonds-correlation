import pandas as pd
from plotnine import ggplot, aes, geom_point, geom_histogram

diamonds = pd.read_csv("Data/diamonds-data.tsv", sep="\t")
print(diamonds)

# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
print("Saving scatter plot")
g = (
	ggplot(
		data=diamonds,
		mapping=aes(x="carat", y="price", colour="clarity")
	)
	+ geom_point()
)

g.save(
	filename="Plots/diamonds.carat-vs-price.png",
	height=8,
	width=12,
	verbose=False
)
