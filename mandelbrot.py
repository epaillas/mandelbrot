import numpy
import pylab

def mandelbrot(z, c):
    return z ** 2 + c

maxiter = 100 # Maximum number of iterations to discard point

ncell = 600 # Number of grid cells per dimension
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5
x = numpy.linspace(xmin, xmax, ncell)
y = numpy.linspace(ymin, ymax, ncell)

grid = numpy.zeros([ncell, ncell])

for l in range(ncell):
    for k in range(ncell):
        c = complex(x[l], y[k])
        z = c
        bailout = 0
        while z.real <= 2 and z.imag <= 2 and bailout <= maxiter:
            z = mandelbrot(z, c)
            bailout += 1

        grid[l, k] = bailout

fig = pylab.figure(figsize=(8,8))
ax = pylab.subplot()

ax.imshow(grid.T, cmap='gist_ncar_r', interpolation='bicubic', origin='lower',
extent=(xmin, xmax, ymin, ymax))

ax.set_xlabel(r'$\mathcal{Re}$', fontsize=15)
ax.set_ylabel(r'$\mathcal{Im}$', fontsize=15)

pylab.savefig('mandelbrot.png')
pylab.show()
