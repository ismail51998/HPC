@types('float[:,:]','float[:,:]','float[:,:]','float[:,:]','int','float','float','float','float')
def solve_2d_nonlinearconv_pyccel(u, un, v, vn, nt, dt, dx, dy, c):

    ###Assign initial conditions
    ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
    u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    ##set hat function I.C. : v(.5<=x<=1 && .5<=y<=1 ) is 2
    v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
    row, col = u.shape
    for t in range(nt):
        for i in range(1,row):
                for j in range(1,col):
                    un[i,j]=u[i,j]
                    vn[i,j]=v[i,j]
        for i in range(1,row):
                for j in range(1,col):
                    u[i,j]=un[i,j]-un[i,j]*dt*(un[i,j]-un[i-1,j])/dx-vn[i,j]*dt*(un[i,j]-un[i,j-1])/dy
                    v[i,j]=vn[i,j]-un[i,j]*dt*(vn[i,j]-vn[i-1,j])/dx-vn[i,j]*dt*(vn[i,j]-vn[i,j-1])/dy
    return 0
