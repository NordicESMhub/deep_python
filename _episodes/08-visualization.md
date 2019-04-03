---
title: Making plots with python
teaching: 0
exercises: 0
questions:
- "What is matplotlib?"
- "What are the differences between imshow, pcolor and pcorlormesh?"
- "How to customize plot?"
- "How to create maps with python?"
- "How to change map projection?"
---

# Making plots with python

# What is matplotlib?

I hope I don’t have to detail why data visualization is important. Data visualization helps you to better understand your data, discover things that you wouldn’t discover in raw format and communicate your findings more efficiently to others. The best and most well-known Python data visualization library is Matplotlib. I wouldn’t say it’s easy to use… But usually if you save for yourself the 4 or 5 most commonly used code blocks for basic line charts and scatter plots, you can create your charts pretty fast.


Gallery of examples:
https://matplotlib.org/2.0.2/gallery.html


```python
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
```

It's important to specify that you would like to have figures plotted in the notebook (otherwise, you will not be able to see the plots). You can do this by typing the command ```%matplotlib inline```


```python
%matplotlib inline
```

The option below allows for higher resolution plots


```python
%config InlineBackend.figure_format ='retina'
```

# Most common 2D-plot functions

```plt.plot```, ```plt.scatter```, ```plt.contour```, ```plt.hist```

Let's test those functions on the dataset provided by Isabel


```python
path = '../data/Isabel/'
filename = 'Edmundson_data_python_DEEP.xlsx'

# let's load the data with the help of the pandas function
data = pd.read_excel(path + filename)

data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area</th>
      <th>Overburden</th>
      <th>HC_column</th>
      <th>Trap_height</th>
      <th>Trap_fill_%</th>
      <th>Trap_fill_normalised_%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1281</td>
      <td>89</td>
      <td>153</td>
      <td>58</td>
      <td>58</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2292</td>
      <td>151</td>
      <td>160</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2806</td>
      <td>77</td>
      <td>320</td>
      <td>24</td>
      <td>24</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1278</td>
      <td>18</td>
      <td>18</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1281</td>
      <td>40</td>
      <td>40</td>
      <td>100</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>



### plt.plot


```python
#plt.plot? # I advice you to run the help function to look at all the available flags
plt.plot(data.Overburden, data.Trap_height,"ko")
plt.xlabel("Overburden")
plt.ylabel("Trap height")
```




    Text(0,0.5,'Trap height')




![png](../fig/output_10_1.png)



```python
#plt.plot? # I advice you to run the help function to look at all the available flags
plt.plot(data.Overburden, data.Trap_height,color='green', marker='o', linestyle='dashed',
        linewidth=2, markersize=12)
plt.xlabel("Overburden")
plt.ylabel("Trap height")
```




    [<matplotlib.lines.Line2D at 0x27bd0ef57f0>]




![png](../fig/output_11_1.png)


### plt.scatter


```python
plt.scatter(data.Overburden, data.Trap_height, c = data.HC_column)
plt.xlabel("Overburden")
plt.ylabel("Trap height")
clb = plt.colorbar()
clb.set_label('HC_column', labelpad=-38, y=1.1, rotation=0)
plt.tight_layout()
```


![png](../fig/output_13_0.png)


### plt.hist


```python
#plt.hist?
plt.hist(data.HC_column, bins = np.arange(0, 650, 25))
plt.xlabel('HC_column')
plt.ylabel('n of values')
```




    Text(0,0.5,'n of values')




![png](../fig/output_15_1.png)


### plt.contour


```python
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

plt.contour(X, Y, Z)
```




    <matplotlib.contour.QuadContourSet at 0x27bc9373860>




![png](../fig/output_17_1.png)


# Visualization of an image


```python
import matplotlib.image as mpimg #if only interested in a specific function in the matplotlib module 
```


```python
image = '../data/mars.png'

img = mpimg.imread(image)

# number of rows, columns, and channels (so actually 3D-array!, channels: red, green, blue, transparency)
print (np.shape(img))
```

    (500, 500, 4)



```python
# plotting with all the channels (4 channels)
plt.imshow(img)
```




    <matplotlib.image.AxesImage at 0x14d82881518>




![png](../fig/output_21_1.png)



```python
# plotting with all the channels (channel 1: Red)
plt.imshow(img[:,:,0], cmap = 'Reds')
plt.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x14d8120d1d0>




![png](../fig/output_22_1.png)


### More information about available colormaps can be found here
https://matplotlib.org/examples/color/colormaps_reference.html


```python
# plotting with all the channels (channel 2: Green)
plt.imshow(img[:,:,1], cmap = 'Greens')
plt.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x14d82314048>




![png](../fig/output_24_1.png)



```python
# plotting with all the channels (channel 3: Blue)
plt.imshow(img[:,:,2], cmap = 'Blues')
plt.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x14d823a7128>




![png](../fig/output_25_1.png)



```python
# plotting with all the channels (channel 4: Transparency)
plt.imshow(img[:,:,3], cmap = 'binary')
plt.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x14d82cdbc18>




![png](../fig/output_26_1.png)


## Differences between plotting directly with plt and defining figure(s) and axes

There are two different ways of plotting things in python
- the "quick and dirty" direct way (using plt.plot or plt.some_other_plotting_functions)
- by defining figure, axis and plot variables that can be used to tune in a more accurate way your plots

Be aware that the function attached to plt.xxx is different from ax1.xxx
For example for writing a title, you will use ```plt.title("write title here")``` but when you work with axes, it will be ```ax.set_title("write title here")```

The more serious way: defining figure, axis and plot variables that can be used to tune in a more accurate way your plots


```python
from mpl_toolkits.axes_grid1 import make_axes_locatable #to specify the locations of colorbars in subplots

# size of the figure in inch
fig = plt.figure(figsize=(8,8))

# geometry of subplots (2 rows and 2 columns)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# make a list of subtitles and colormaps used
titles = ['Red channel', 'Green channel', 'Blue channel', 'Transparency channel']
cbars = ['Reds', 'Greens', 'Blues', 'binary']

ax1.set_title('Red channel')
ax2.set_title('Green channel')
ax3.set_title('Blue channel')
ax4.set_title('Transparency channel')

# Figure 1
im1 = ax1.imshow(img[:,:,0], cmap = cbars[0])

divider = make_axes_locatable(ax1)
cax1 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im1, cax=cax1, orientation='vertical')

# Figure 2
im2 = ax2.imshow(img[:,:,1], cmap = cbars[1])

divider = make_axes_locatable(ax2)
cax2 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im2, cax=cax2, orientation='vertical')

# Figure 3
im3 = ax3.imshow(img[:,:,2], cmap = cbars[2])

divider = make_axes_locatable(ax3)
cax2 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im3, cax=cax2, orientation='vertical')

# Figure 4
im4 = ax4.imshow(img[:,:,3], cmap = cbars[3])

divider = make_axes_locatable(ax4)
cax4 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im4, cax=cax4, orientation='vertical')

fig.tight_layout() # avoid overlap between colorbars, titles, figures and so on...
```


![png](../fig/output_29_0.png)


## How can you save the figure you have just created?

**Other tweaks you can use**
- **format** : can be specified in the name of the figure (here .png)
- **dpi** : resolution of the image
- **background color** : either on fig.savefig or option on axes (see https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color/23907866)  
- **transparency** : transparent=True in fig.savefig



```python
# fig.savefig? #for info
# %pwd # to see where the .png files are saved to
fig.savefig("filename_figure_normal.png", dpi = 300)
```

# How to customize your plots?

**Transparent background**


```python
#need to rerun the script to recreate the plot
fig.savefig("filename_figure_transparent.png", dpi = 300, transparent=True)
```

**Background filled with specific color**


```python
# size of the figure in inch
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1)
im1 = ax1.imshow(img[:,:,0], cmap = cbars[0])

divider = make_axes_locatable(ax1)
cax1 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im1, cax=cax1, orientation='vertical')

fig.patch.set_facecolor('xkcd:mint green')
```


![png](../fig/output_35_0.png)


## How to Plot Only One Colorbar for Multiple Plot Using Matplotlib
https://jdhao.github.io/2017/06/11/mpl_multiplot_one_colorbar/


```python
# size of the figure in inch
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,8))

for ax in axes.flat:
    
    im = ax.imshow(img[:,:,i], cmap='viridis',
                       vmin=0, vmax=1)
        

fig.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.8, wspace=0.02, hspace=0.02)

# add an axes, lower left corner in [0.83, 0.1] measured in figure coordinate with axes width 0.02 and height 0.8

cb_ax = fig.add_axes([0.83, 0.1, 0.05, 0.8])
cbar = fig.colorbar(im, cax=cb_ax)
fig.tight_layout()

```

![png](../fig/output_37_1.png)


## Subfigures of different sizes


```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(16,8))

gs=GridSpec(2,4) # 2 rows, 4 columns

ax1=fig.add_subplot(gs[0,0]) # First row, first column (from the top)
ax2=fig.add_subplot(gs[0,1]) # First row, second column
ax3=fig.add_subplot(gs[1,0]) # Second row, first column
ax4=fig.add_subplot(gs[1,1]) # Second row, second column
ax5=fig.add_subplot(gs[:,2:]) # Span all rows, third and fourth column

# make a list of subtitles and colormaps used
titles = ['Red channel', 'Green channel', 'Blue channel', 'Transparency channel']
cbars = ['Reds', 'Greens', 'Blues', 'binary']

ax1.set_title('Red channel')
ax2.set_title('Green channel')
ax3.set_title('Blue channel')
ax4.set_title('Transparency channel')
ax5.set_title('Composite')

# Figure 1
im1 = ax1.imshow(img[:,:,0], cmap = cbars[0])

divider = make_axes_locatable(ax1)
cax1 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im1, cax=cax1, orientation='vertical')

# Figure 2
im2 = ax2.imshow(img[:,:,1], cmap = cbars[1])

divider = make_axes_locatable(ax2)
cax2 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im2, cax=cax2, orientation='vertical')

# Figure 3
im3 = ax3.imshow(img[:,:,2], cmap = cbars[2])

divider = make_axes_locatable(ax3)
cax2 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im3, cax=cax2, orientation='vertical')

# Figure 4
im4 = ax4.imshow(img[:,:,3], cmap = cbars[3])

divider = make_axes_locatable(ax4)
cax4 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im4, cax=cax4, orientation='vertical')

# Figure 5
im5 = ax5.imshow(img)

fig.tight_layout() # avoid overlap between colorbars, titles, figures and so on...
```


![png](../fig/output_39_0.png)


## Subscript, special characters

More info here: https://matplotlib.org/users/mathtext.html


```python
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1)
im1 = ax1.imshow(img[:,:,0], cmap = cbars[0])

divider = make_axes_locatable(ax1)
cax1 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im1, cax=cax1, orientation='vertical')

# math text
ax1.set_title(r'$\alpha > \beta$')
```




    Text(0.5,1,'$\\alpha > \\beta$')




![png](../fig/output_41_1.png)


## Texts of different sizes
If you want to place text in different locations (see https://matplotlib.org/users/text_props.html)


```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(16,8))

gs=GridSpec(2,4) # 2 rows, 4 columns

ax1=fig.add_subplot(gs[0,0]) # First row, first column (from the top)
ax2=fig.add_subplot(gs[0,1]) # First row, second column
ax3=fig.add_subplot(gs[1,0]) # Second row, first column
ax4=fig.add_subplot(gs[1,1]) # Second row, second column
ax5=fig.add_subplot(gs[:,2:]) # Span all rows, third and fourth column

# make a list of subtitles and colormaps used
titles = ['Red channel', 'Green channel', 'Blue channel', 'Transparency channel']
cbars = ['Reds', 'Greens', 'Blues', 'binary']

ax1.set_title('Red channel', fontsize = 16)
ax2.set_title('Green channel', fontsize = 16)
ax3.set_title('Blue channel', fontsize = 16)
ax4.set_title('Transparency channel', fontsize = 16)
ax5.set_title('Composite', fontsize = 16)

# Figure 1
im1 = ax1.imshow(img[:,:,0], cmap = cbars[0])

divider = make_axes_locatable(ax1)
cax1 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im1, cax=cax1, orientation='vertical')

# Figure 2
im2 = ax2.imshow(img[:,:,1], cmap = cbars[1])

divider = make_axes_locatable(ax2)
cax2 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im2, cax=cax2, orientation='vertical')

# Figure 3
im3 = ax3.imshow(img[:,:,2], cmap = cbars[2])

divider = make_axes_locatable(ax3)
cax2 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im3, cax=cax2, orientation='vertical')

# Figure 4
im4 = ax4.imshow(img[:,:,3], cmap = cbars[3])

divider = make_axes_locatable(ax4)
cax4 = divider.append_axes('right', size='5%', pad=0.10)
fig.colorbar(im4, cax=cax4, orientation='vertical')

# Figure 5
im5 = ax5.imshow(img)

fig.suptitle('Mars.png', fontsize = 24)
fig.tight_layout(pad=3) # add extra white space

```


![png](../fig/output_43_0.png)


## Avoid the automatic plotting of a figure (useful if you save lot of snapshots)


```python
#plt.ioff() #don't run otherwise you will not see your figures from now on!
```

# Visualization of an image (3D-array)

https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

## imshow
Minimum value is in the lower left


```python
# example with a crater in 3D

h = plt.imshow(img[:,:,0])

```


![png](../fig/output_47_0.png)


## pcolor
The y-axis is turned upside down


```python
plt.pcolor(np.arange(500),np.arange(500), img[:,:,0])
plt.axis('equal')
```




    (0.0, 499.0, 0.0, 499.0)




![png](../fig/output_49_1.png)


This can be fixed by swaping the y-axis with the help of ```[::-1]``` (reverse the array)


```python
plt.pcolor(np.arange(500),np.arange(500)[::-1], img[:,:,0])
plt.axis('equal')
```




    (0.0, 499.0, 0.0, 499.0)




![png](../fig/output_51_1.png)


## pcolormesh
```pcolormesh``` should be used over ```pcolor``` (much faster to plot the figure)


```python
plt.pcolormesh(np.arange(500),np.arange(500)[::-1], img[:,:,0])
plt.axis('equal')
```




    (0.0, 499.0, 0.0, 499.0)




![png](../fig/output_53_1.png)


## Scatter plots (3D-axes)


```python
# let's load a new example
path = '../data/Nils/'
filename = 'crater0000.asc'

# let's load the data with the help of numpy
topography_crater = np.loadtxt(path + filename, skiprows=6)

topography_crater
```




    array([[-5852., -5851., -5842., ...,   839.,   826.,   813.],
           [-5877., -5874., -5862., ...,   839.,   830.,   817.],
           [-5901., -5901., -5886., ...,   835.,   827.,   818.],
           ...,
           [ 3177.,  3186.,  3206., ..., -7088., -7092., -7091.],
           [ 3182.,  3193.,  3208., ..., -7090., -7089., -7087.],
           [ 3185.,  3191.,  3212., ..., -7092., -7092., -7083.]])




```python
np.shape(topography_crater) # 1540 rows and columns
```




    (1540, 1540)




```python
cellsize = 60 # meters
xs = np.arange(0,1540)*cellsize # along x-axis
ys = np.arange(0,1540)*cellsize # along y-axis

xc, yc = np.meshgrid(xs, ys) # create a meshgrid
```


```python
from mpl_toolkits.mplot3d import Axes3D

# maybe need to do this part in Spyder
%matplotlib notebook

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xc[:500], yc[:500], topography_crater[:500])
```

## Wireframe plots (3D-axes)


```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(xc[:500], yc[:500], topography_crater[:500])
```

## Surface plots (3D-axes)


```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xc[:500], yc[:500], topography_crater[:500])
```

## Triangular surface plots (3D-axes)


```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(xc[:500], yc[:500], topography_crater[:500])
```

## Contour plots (3D-axes)


```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.contour(xc[:500], yc[:500], topography_crater[:500])
```

# How to create maps with python? (advanced part)

- [Geospatial Data Visualization](https://geohackweek.github.io/visualization/)
- [Working with Spatio-temporal data in Python](https://annefou.github.io/metos_python/)


{% include links.md %}
