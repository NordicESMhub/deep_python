import pandas as pd
import matplotlib.pyplot as plt # 
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.widgets import RectangleSelector
import csv

#===============================================================
#Files to read data from

MCD = np.array(pd.read_excel(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG-age-model-220219.xlsx", index_col=None, na_values=['NA'], parse_cols = "A"))
Ti = np.array(pd.read_excel(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG-mastercore-XRF.xlsx", index_col=None, na_values=['NA'], parse_cols = "N"))
xrfdep = np.array(pd.read_excel(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG-mastercore-XRF.xlsx", index_col=None, na_values=['NA'], parse_cols = "C"))
Age = np.array(pd.read_excel(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG-age-model-220219.xlsx", index_col=None, na_values=['NA'], parse_cols = "F"))
# MSdepth = np.array(pd.read_csv(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG-118-1av2-0-38-scan2.csv", index_col=None, na_values=['NA'], usecols = "Core Pos. (cm)"))
# MSdata = np.array(pd.read_csv(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG-118-1av2-0-38-scan2.csv", index_col=None, na_values=['NA'], usecols = "Raw Data"))

#===============================================================
#Figure details

def cm2inch(*tupl):                             # Makes it possible to size figure in cm
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)

fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, sharey=True, sharex=False,
 figsize=cm2inch(30, 9.6))           #sharey makes all subplots dependent on same y-axis. This removes the scale numbers on all but the first one

#===============================================================
# Subplots

#Image

# Subplot 1 - Age model
ax1.plot(Age, MCD)
ax1.set_title("Age model")
ax1.set_ylabel("Depth (mm)")
ax1.set_xlabel("Years cal. AD")
ax1.invert_yaxis()  #inverts y axis
ax1.invert_xaxis()  #inverts x axis

#Subplot 2 - XRF
ax2.plot(Ti, xrfdep)
ax2.set_title("Titanium")
ax2.set_ylabel("Depth (mm)")
ax2.set_xlabel("Ti (cps)")
ax2.invert_yaxis()  #inverts y axis

# # Subplot 3 - MS
# ax3.plot(MSdata, MSdepth)
# ax3.set_title("Magnetic Susceptibility")
# ax3.set_ylabel("Depth (mm)")
# ax3.set_xlabel("MS")
# ax3.invert_yaxis()  #inverts y axis

# Subplot 4 - Age scale
ax4 = ax1.twinx()                                         # ax4 shares the x-axis with ax1
ymn = Age[0]                                              # first element in Age array
ymx = Age[-1]                                             # last element in Age array
ax4.set_ylim(ymin=ymx, ymax=ymn)                          # sets the limits of the secondary y-axis
ax4.spines['left'].set_position(('axes', -0.3))           # Moves the secondary axis                     #
ax4.yaxis.set_label_position('left')
ax4.yaxis.set_ticks_position('left')
ax4.set_ylabel("Years AD")

# Subplot 5 - LOI
# LOI = np.array(pd.read_excel(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG118-2of2-W-LOI.xls", index_col=None, na_values=['NA'], parse_cols = "N"))
# LOIdepth = np.array(pd.read_excel(r"C:\Users\emballo\Google Drive\VIKINGS\Lakes\Nordbytjernet\1 Main data plotting\NTG118-2of2-W-LOI.xls", index_col=None, na_values=['NA'], parse_cols = "A"))
# ax5.plot(LOI, LOIdepth)
# ax5.set_title("LOI")
# ax5.set_ylabel("Depth (mm)")
# ax5.set_xlabel("LOI")
# ax5.invert_yaxis()  #inverts y axis

# Figure attributes
#ax1.patches.Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none')

# ax2.patches.extend([plt.Rectangle((0.2,0.5),0.5,0.25,
#                                   fill=True, color='g', alpha=0.5, zorder=1000,
#                                   transform=fig.transFigure, figure=fig)])

#===============================================================
#Figure attributes

ax1.margins(x=0,y=0)                        #removes the margin between bounding box and plot
plt.subplots_adjust(wspace=0.5 )            # Tweak spacing between subplots to prevent labels from overlapping
plt.show(block=True)                                 # Print plot

# par2.spines["right"].set_position(("axes", 1.2))          #moves the spine of the axis away from the actual plot
# plt.savefig("NTG-compiled.svg", bbox_inches='tight')