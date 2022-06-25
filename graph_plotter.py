import matplotlib.pyplot as plt

# histogram plotter
def hist_plotter(data, x_label, y_label, save_name, save_format):
    plt.hist(data)
    plt.xlabel = x_label
    plt.ylabel = y_label
    plt.savefig(save_name + '.' + save_format)