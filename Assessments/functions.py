# functions

def SRW(p, L, N_sim, tmax, init):
    Y = np.ones((N_sim, tmax+1))*init
    for i in range(0, N_sim):
        t = 0
        while t < tmax:
            r = np.random.rand()
            if r<p:
                x = math.ceil((L-Y[i,t])/L)
            else:
                x = math.floor((1-Y[i,t])/L)
            Y[i, t+1] = Y[i,t] + x
            t +=1    
    return Y