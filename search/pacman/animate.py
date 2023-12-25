import matplotlib.pyplot as plt
import matplotlib.animation as anim

patches = []

def init():
    return []

def animate(i, path, ax):
    global patches
    for patch in patches:
        patch.remove()

    st = i % len(path)
    nums = path[st].split('-')
    nums = [int(n) for n in nums]

    if st==len(path)-1:
        patches = []
        pacman = ax.add_patch(plt.Circle((nums[0]+0.5,nums[1]+0.5), radius=0.4, color='royalblue'))
        patches.append(pacman)
        return patches
    
    patches = []
    pacman = ax.add_patch(plt.Circle((nums[0]+0.5,nums[1]+0.5), radius=0.4, color='gold'))
    mspacman = ax.add_patch(plt.Circle((nums[2]+0.5,nums[3]+0.5), radius=0.4, color='hotpink'))
    patches.append(pacman)
    patches.append(mspacman)

    return patches

def run_animation(size, path, alg):
    plt.style.use('seaborn')
    nx, ny = size, size
    fig = plt.figure()
    plt.axis([0,nx,0,ny])

    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])        
    ax.xaxis.tick_top()                         
    ax.yaxis.tick_left() 
    if alg=='BFS':
        ax.set_title(f'BFS - A Normal Maze', fontsize=20)
    if alg=='DFS':
        ax.set_title(f'DFS - Its not a Maze, this is just Ikea', fontsize=20)
    if alg=='A*':
        ax.set_title(f'A* - A Normal Maze but Pacman is too lazy to turn', fontsize=20)

    ax.set_aspect(1)

    ani = anim.FuncAnimation(fig, animate, init_func=init,
                                frames=len(path), interval=400, blit=True, fargs=(path,ax,))
    ani.save(f"pacman-{size}-{alg}.gif", writer="pillow", dpi=200)