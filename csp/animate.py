import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# im = plt.imread('qimg.png')
# oi = OffsetImage(im, zoom = 0.15)
# box = AnnotationBbox(oi, (px, py), frameon=False)


patches = []

def init():
    return []

def animate(i, path, ax, size):
    global patches
    for patch in patches:
        patch.remove()

    st = i % len(path)
    board = path[st]

    colors = ['navajowhite', 'peru']
    patches = []

    for i in range(size):
        for j in range(size):
            rem = (i+j)%2
            square = ax.add_patch(plt.Rectangle((i,j), width=1, height=1, color=colors[rem]))
            patches.append(square)

    if st==len(path)-1:
        for i,j in enumerate(board):
            square = ax.add_patch(plt.Rectangle((i,j), width=1, height=1, color='forestgreen'))
            patches.append(square)
    
    for i,j in enumerate(board):
        im = plt.imread('qimg.png')
        oi = OffsetImage(im, zoom=(0.6*4/size))
        queen = AnnotationBbox(oi, (i+0.5, j+0.5), frameon=False)
        patches.append(ax.add_artist(queen))

    return patches

def run_animation(size, path):
    plt.style.use('seaborn')
    nx, ny = size, size
    fig = plt.figure()
    plt.axis([0,nx,0,ny])

    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])        
    ax.xaxis.tick_top()                         
    ax.yaxis.tick_left()                    
    ax.set_title(f'{size}-Queens', fontsize=25)

    ax.set_aspect(1)

    frames = list(range(len(path)))
    frames.extend([len(path)-1]*3)


    ani = anim.FuncAnimation(fig, animate, init_func=init,
                                frames=frames, interval=400, blit=True, fargs=(path,ax,size))
    ani.save(f"{size}-Queens.gif", writer="pillow", dpi=200)