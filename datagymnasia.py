from IPython.display import SVG, display
def show(fig):
    filename = "my-figure.svg"
    fig.write_image(filename)
    return display(SVG(filename))
