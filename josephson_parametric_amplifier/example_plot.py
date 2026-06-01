import numpy as np
import matplotlib.pyplot as plt


# example for importing data
# data = np.genfromtxt("./data/measurement_1.csv")

# generate some example data to plot
xs = np.linspace(-3, 3, 100)
ys = np.exp(-xs**2)

# use the fopraplot stylesheet
plt.style.use("../fopraplot_no_latex.mplstyle")

fig, ax = plt.subplots()
ax.plot(xs, ys)
ax.set(xlabel="xlabel", ylabel="ylabel")

# save the figure as pdf in the figs folder
fig.savefig("./figs/example_plot.pdf")
