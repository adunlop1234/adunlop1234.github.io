import matplotlib.animation as animation
import matplotlib.pyplot as plt
import sys, os
import csv

# Flag dict
flag_dict = {
    'Slovakia' : 'sk.png',
    'North Macedonia' : 'mk.png',
    'Hungary' : 'hu.png',
    'Sweden' : 'se.png',
    'Denmark' : 'dk.png',
    'Russia' : 'ru.png',
    'France' : 'fr.png',
    'Czech Republic' : 'cz.png',
    'Wales' : 'gb-wls.png',
    'Belgium' : 'be.png',
    'Germany' : 'de.png',
    'Turkey' : 'tr.png',
    'Austria' : 'at.png',
    'Ukraine' : 'ua.png',
    'Netherlands' : 'nl.png',
    'Portugal' : 'pt.png',
    'Scotland' : 'gb-sct.png',
    'Spain' : 'es.png',
    'England' : 'gb-eng.png',
    'Switzerland' : 'ch.png',
    'Poland' : 'pl.png',
    'Italy' : 'it.png',
    'Finland' : 'fi.png',
    'Croatia' : 'hr.png'
}

# Get data in
with open(os.path.join("data", "draw.csv"), "r") as f:
    reader = csv.reader(f)
    data = list(reader)

for i, (team, person), in enumerate(data):
    flag_png = flag_dict[team]
    img = plt.imread(os.path.join("data", "flags", flag_png))
    data[i].append(img)

# Create subplots
fig, axs = plt.subplots(6,4)
fig.set_figwidth(8)
fig.set_figheight(8)
fig.tight_layout(pad=3.0)
for axx in axs:
    for ax in axx:
        ax.axis('off')

def index():
    return iter(range(0,24))

def updatefig(i):
    ax = axs.flatten()[i]

    # Get person, team and flag
    team, person, flag = data[i]

    ax.imshow(flag, origin="upper", extent=[0, 2, 0, 1])
    ax.set_title(person + " - " + team)

    plt.draw()

anim = animation.FuncAnimation(fig, updatefig, index)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
anim.save(os.path.join("data", "draw.mp4"), writer=writer)
plt.show()