import matplotlib.pyplot as plt
import matplotlib.animation as anim

goals = {'012345678', '123456780'}

plt.style.use('seaborn')
fig = plt.figure()
plt.axis([0,3,0,3])
ax = plt.gca()
ax.set_ylim(ax.get_ylim()[::-1])    
ax.set_title('8-Puzzle', fontsize=25)

ax.set_xticks([0,1,2,3])
ax.set_yticks([0,1,2,3])
ax.tick_params(
    axis='both',          
    which='both',      
    bottom=False,      
    top=False, 
    left=False,
    right=False,
    labelbottom=False,
    labelleft=False
)          

ax.set_aspect(1)
patches = []

def init():
    return []

def animate(k, path):
    global patches
    for patch in patches:
        patch.remove()

    st = k % len(path)
    state = path[st]

    n = state.index('0')
    y,x = n//3, n%3

    patches = []

    if state in goals:
        for i in range(0,3):
            for j in range(0,3):
                num = 3*j + i
                if i==x and j==y:
                    continue
                tile = ax.add_patch(plt.Rectangle((i+0.05,j+0.05), width=0.9, height=0.9, color='royalblue'))
                number = ax.text(i+0.5, j+0.52, state[num], fontsize=50, ha='center', va='center', color='gold', fontfamily='serif')
                patches.append(tile)
                patches.append(number)

        return patches

    for i in range(0,3):
        for j in range(0,3):
            num = 3*j + i
            if i==x and j==y:
                continue
            tile = ax.add_patch(plt.Rectangle((i+0.05,j+0.05), width=0.9, height=0.9, color='royalblue'))
            number = ax.text(i+0.5, j+0.52, state[num], fontsize=50, ha='center', va='center', color='white', fontfamily='serif')
            patches.append(tile)
            patches.append(number)

    return patches

def run_animation(path):
    ani = anim.FuncAnimation(fig, animate, init_func=init,
                                frames=len(path)+1, interval=400, blit=True, fargs=(path,))
    ani.save("8test.gif", writer="pillow", dpi=200)