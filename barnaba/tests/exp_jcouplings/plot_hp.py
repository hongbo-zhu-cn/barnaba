import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
cp = sns.color_palette()

# sugar
bb=np.pi*(2./3.)
ee=0    
def hp_lankhorst(x):
    #x += 
    return 15.3*np.cos(x+ee)*np.cos(x+ee)-6.1*np.cos(x+ee) + 1.6

def hp_mooren(x):
    #x += np.pi*(2./3.)
    return 15.3*np.cos(x+ee)*np.cos(x+ee)-6.2*np.cos(x+ee) + 1.5

def hp_lee(x):
    #x += np.pi*(2./3.)
    return 18.1*np.cos(x+ee)*np.cos(x+ee)-4.8*np.cos(x+ee) + 1.5

fmts = ['o','s','*','d']
cols = ['blue','red','black','yellow']
lee_err = []
mooren_err = []
lankhorst_err = []

xx = np.arange(0,2*np.pi,0.01)
ff = np.pi/180.
plt.plot(xx,hp_mooren(xx+bb),c=cp[0],label="mooren")
plt.plot(xx,hp_lee(xx+bb),c=cp[1],label="lee")
plt.plot(xx,hp_lankhorst(xx+bb),c=cp[2],label="lankhorst")
plt.legend()
data = np.array([[float(x) for x in line.split()] for line in open("h3p.txt") if ("#" not in line)])
data[np.where(data[:,3]<0.0),3] += 360
plt.errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2])
plt.xlabel("Epsilon (rad)")
plt.ylabel("3J (Hz)")
plt.savefig("h3p.png")
plt.close()
mooren_err.extend([hp_mooren(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
lee_err.extend([hp_lee(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
lankhorst_err.extend([hp_lankhorst(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])


plt.plot(xx,hp_mooren(xx-bb),c=cp[0],label="mooren")
plt.plot(xx,hp_lee(xx-bb),c=cp[1],label="lee")
plt.plot(xx,hp_lankhorst(xx-bb),c=cp[2],label="lankhorst")
plt.legend()
data = np.array([[float(x) for x in line.split()] for line in open("h5pp.txt") if ("#" not in line)])
data[np.where(data[:,3]<0.0),3] += 360
plt.errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2])
plt.xlabel("Beta (rad)")
plt.ylabel("3J (Hz)")
plt.savefig("h5pp.png")
plt.close()
mooren_err.extend([hp_mooren(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
lee_err.extend([hp_lee(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
lankhorst_err.extend([hp_lankhorst(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])


plt.plot(xx,hp_mooren(xx+bb),c=cp[0],label="mooren")
plt.plot(xx,hp_lee(xx+bb),c=cp[1],label="lee")
plt.plot(xx,hp_lankhorst(xx+bb),c=cp[2],label="lankhorst")
plt.legend()
data = np.array([[float(x) for x in line.split()] for line in open("h5ps.txt") if ("#" not in line)])
data[np.where(data[:,3]<0.0),3] += 360
plt.errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2])
plt.xlabel("Beta (rad)")
plt.ylabel("3J (Hz)")
plt.savefig("h5sp.png")
plt.close()
mooren_err.extend([hp_mooren(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
lee_err.extend([hp_lee(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
lankhorst_err.extend([hp_lankhorst(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])





