# mandelbrot
Shiny App for plotting the Mandelbrot set.

Running App.py using Shiny runs the app with the local machine as a server. The app allows a user to select a range in the xy-plane, the resolution of the plot, and the number of iterations of the Mandelbrot algorithm to try, and then plots a heatmap showing the Mandelbrot set based on those parameters.

Mandelbrot.py contains functions for building a grid in the xz-plane and then determining how many iterations of the Mandelbrot algorithm are needed for that point to diverge.
