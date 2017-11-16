import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cp = sns.color_palette(n_colors=9)
sns.set_style("white")
sns.set_context("paper")

# sugar
def sugar_hasnoot_h1h2(x):
    v = [6.96462,-0.91,1.02629,1.27009,0]
    cos = np.cos(x+v[4])
    sin = np.sin(x+v[4])
    return v[0]*cos*cos + v[1]*cos + v[2] + v[3]*cos*sin

def sugar_hasnoot_h2h3(x):
    v = [8.28926,-0.91, 0.66772, 0.00193297,0]
    cos = np.cos(x+v[4])
    sin = np.sin(x+v[4])
    return v[0]*cos*cos + v[1]*cos + v[2] + v[3]*cos*sin

def sugar_hasnoot_h3h4(x):
    v = [7.96446,-0.91, 0.77241, -0.262475,0]
    cos = np.cos(x+v[4])
    sin = np.sin(x+v[4])
    return v[0]*cos*cos + v[1]*cos + v[2] + v[3]*cos*sin

def hasnoot_h4h5p(x):
    v = [8.313,-0.99,1.373,0.27,0]
    cos = np.cos(x+v[4])
    sin = np.sin(x+v[4])
    return v[0]*cos*cos + v[1]*cos + v[2] + v[3]*cos*sin

def hasnoot_h4h5s(x):
    v = [8.313,-0.99,1.373,-4.752,0]
    cos = np.cos(x+v[4])
    sin = np.sin(x+v[4])
    return v[0]*cos*cos + v[1]*cos + v[2] + v[3]*cos*sin
    
def sugar_davies(x):
    return 10.2*np.cos(x)*np.cos(x)-0.8*np.cos(x)

def sugar_condon(x):
    return 9.67*np.cos(x)*np.cos(x)-2.03*np.cos(x)

def cp_mooren(x):
    return 8*np.cos(x)*np.cos(x)-3.4*np.cos(x) + 0.5

def cp_marino(x):
    return 6.9*np.cos(x)*np.cos(x)-3.4*np.cos(x) + 0.7

def hp_lankhorst(x):
    #x += 
    return 15.3*np.cos(x)*np.cos(x)-6.1*np.cos(x) + 1.6

def hp_mooren(x):
    return 15.3*np.cos(x)*np.cos(x)-6.2*np.cos(x) + 1.5

def hp_lee(x):
    return 18.1*np.cos(x)*np.cos(x)-4.8*np.cos(x) + 1.5
   
def ippel_c86(x):
    return 4.5*np.cos(x)*np.cos(x)-0.6*np.cos(x) + 0.1

def ippel_c42(x):
    return 4.7*np.cos(x)*np.cos(x)+2.3*np.cos(x) + 0.1

def hh_davies(x):
    return 9.7*np.cos(x)*np.cos(x)-1.8*np.cos(x)


xx = np.arange(0,2*np.pi,0.01)
ff = np.pi/180.
errors = []
labels = []
fig,ax = plt.subplots(5,3,figsize=(8.3,8),sharex=True)

# H1H2
ax[0,0].plot(xx,sugar_hasnoot_h1h2(xx),c=cp[0],label="Hasnoot",lw=1)
ax[0,0].plot(xx,sugar_davies(xx),c=cp[1],label="Davies",lw=1)
ax[0,0].plot(xx,sugar_condon(xx),c=cp[2],label="Condon",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h1h2.txt")])
errors.append([sugar_hasnoot_h1h2(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H1H2","HASNOOT"])
errors.append([sugar_davies(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H1H2","DAVIES"])
errors.append([sugar_condon(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H1H2","CONDON"])

data[np.where(data[:,3]<0.0),3] += 360
ax[0,0].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[0,0].set_xlabel("H1'H3'")
ax[0,0].set_ylabel("3J (Hz)")
ax[1,0].set_ylabel("3J (Hz)")
ax[2,0].set_ylabel("3J (Hz)")
ax[3,0].set_ylabel("3J (Hz)")
ax[4,0].set_ylabel("3J (Hz)")
ax[0,0].legend()
ax[0,0].set_xlim(0,2*np.pi)


# H2H3
ax[0,1].plot(xx,sugar_hasnoot_h2h3(xx),c=cp[0],label="Hasnoot",lw=1)
ax[0,1].plot(xx,sugar_davies(xx),c=cp[1],label="Davies",lw=1)
ax[0,1].plot(xx,sugar_condon(xx),c=cp[2],label="Condon",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h2h3.txt")])
errors.append([sugar_hasnoot_h2h3(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H2H3","HASNOOT"])
errors.append([sugar_davies(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H2H3","DAVIES"])
errors.append([sugar_condon(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H2H3","CONDON"])

data[np.where(data[:,3]<0.0),3] += 360
ax[0,1].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[0,1].set_xlabel("H2'H3'")
ax[0,1].set_xlim(0,2*np.pi)

# H3H4
ax[0,2].plot(xx,sugar_hasnoot_h3h4(xx),c=cp[0],label="Hasnoot",lw=1)
ax[0,2].plot(xx,sugar_davies(xx),c=cp[1],label="Davies",lw=1)
ax[0,2].plot(xx,sugar_condon(xx),c=cp[2],label="Condon",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h3h4.txt")])
errors.append([sugar_hasnoot_h3h4(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H3H4","HASNOOT"])
errors.append([sugar_davies(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H3H4","DAVIES"])
errors.append([sugar_condon(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H3H4","CONDON"])

data[np.where(data[:,3]<0.0),3] += 360
ax[0,2].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[0,2].set_xlabel("H3'H4'")
ax[0,2].set_xlim(0,2*np.pi)

# CP
ax[1,0].plot(xx,cp_mooren(xx),c=cp[3],label="Mooren",lw=1)
ax[1,0].plot(xx,cp_marino(xx),c=cp[4],label="Marino",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("c4p5.txt") if("#" not in line)])
errors.append([cp_mooren(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["C4P5","MOOREN"])
errors.append([cp_marino(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["C4P5","MARINO"])

data[np.where(data[:,3]<0.0),3] += 360
ax[1,0].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[1,0].set_xlabel(r"$\beta$ (C4P(i+1))")
ax[1,0].set_xlim(0,2*np.pi)
#################
ax[1,1].plot(xx,cp_mooren(xx),c=cp[3],label="Mooren",lw=1)
ax[1,1].plot(xx,cp_marino(xx),c=cp[4],label="Marino",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("c4p3.txt")])
errors.append([cp_mooren(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["C4P3","MOOREN"])
errors.append([cp_marino(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["C4P3","MARINO"])
ax[1,0].legend()
data[np.where(data[:,3]<0.0),3] += 360
ax[1,1].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[1,1].set_xlabel(r"$\epsilon$ (C4P3)")
ax[1,1].set_xlim(0,2*np.pi)

ax[1,2].axis('off')

#########  HP  ####################
bb=np.pi*(2./3.)

ax[2,0].plot(xx,hp_mooren(xx-bb),c=cp[3],label="Mooren",lw=1)
ax[2,0].plot(xx,hp_lankhorst(xx-bb),c=cp[5],label="Lankhorst",lw=1)
ax[2,0].plot(xx,hp_lee(xx-bb),c=cp[6],label="Lee",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h5pp.txt") if("#" not in line)])
errors.append([hp_mooren(data[ii,3]*ff-bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["PH5'","MOOREN"])
errors.append([hp_lankhorst(data[ii,3]*ff-bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["PH5'","LANKHORST"])
errors.append([hp_lee(data[ii,3]*ff-bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["PH5'","LEE"])

data[np.where(data[:,3]<0.0),3] += 360
ax[2,0].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[2,0].set_xlabel(r"$\beta$ (PH5')")
ax[2,0].set_xlim(0,2*np.pi)
ax[2,0].legend()

ax[2,1].plot(xx,hp_mooren(xx+bb),c=cp[3],label="Mooren",lw=1)
ax[2,1].plot(xx,hp_lankhorst(xx+bb),c=cp[5],label="Lankhorst",lw=1)
ax[2,1].plot(xx,hp_lee(xx+bb),c=cp[6],label="Lee",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h5ps.txt") if("#" not in line)])
errors.append([hp_mooren(data[ii,3]*ff+bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["PH5''","MOOREN"])
errors.append([hp_lankhorst(data[ii,3]*ff+bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["PH5''","LANKHORST"])
errors.append([hp_lee(data[ii,3]*ff+bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["PH5''","LEE"])

data[np.where(data[:,3]<0.0),3] += 360
ax[2,1].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[2,1].set_xlabel(r"$\beta$ (PH5'')")
ax[2,1].set_xlim(0,2*np.pi)


ax[2,2].plot(xx,hp_mooren(xx+bb),c=cp[3],label="Mooren",lw=1)
ax[2,2].plot(xx,hp_lankhorst(xx+bb),c=cp[5],label="Lankhorst",lw=1)
ax[2,2].plot(xx,hp_lee(xx+bb),c=cp[6],label="Lee",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h3p.txt") if("#" not in line)])
errors.append([hp_mooren(data[ii,3]*ff+bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H3P","MOOREN"])
errors.append([hp_lankhorst(data[ii,3]*ff+bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H3P","LANKHORST"])
errors.append([hp_lee(data[ii,3]*ff+bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H3P","LEE"])

data[np.where(data[:,3]<0.0),3] += 360
ax[2,2].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[2,2].set_xlabel(r"$\epsilon$ (H3P)")
ax[2,2].set_xlim(0,2*np.pi)

#########  HP  ####################

ax[3,0].plot(xx,hasnoot_h4h5p(xx-bb),c=cp[0],label="Hasnoot",lw=1)
ax[3,0].plot(xx,hh_davies(xx-bb),c=cp[7],label="Davies",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h4h5p.txt") if("#" not in line)])
errors.append([hasnoot_h4h5p(data[ii,3]*ff-bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H4H5'","HASNOOT"])
errors.append([hh_davies(data[ii,3]*ff-bb)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H4H5'","DAVIES"])
data[np.where(data[:,3]<0.0),3] += 360
ax[3,0].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[3,0].set_xlabel(r"$\gamma$ (H4H5')")
ax[3,0].set_xlim(0,2*np.pi)
ax[3,0].legend()

ax[3,1].plot(xx,hasnoot_h4h5p(xx),c=cp[0],label="Hasnoot",lw=1)
ax[3,1].plot(xx,hh_davies(xx),c=cp[7],label="Davies",lw=1)
data = np.array([[float(x) for x in line.split()] for line in open("h4h5s.txt") if("#" not in line)])
errors.append([hasnoot_h4h5p(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H4H5''","HASNOOT"])
errors.append([hh_davies(data[ii,3]*ff)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["H4H5''","DAVIES"])
data[np.where(data[:,3]<0.0),3] += 360
ax[3,1].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[3,1].set_xlabel(r"$\gamma$ (H4H5'')")
ax[3,1].set_xlim(0,2*np.pi)
ax[3,2].axis('off')

##########################
ax[4,0].plot(xx,ippel_c86(xx-bb/2.),c=cp[8],label="Ippel",lw=1)
ax[4,0].legend()

#data = np.array([[float(x) for x in line.split()] for line in open("h1c86.txt") if("#" not in line)])
#errors.append([ippel(data[ii,3]*ff-bb/2)-data[ii,1] for ii in range(data.shape[0])])
labels.append(["h1c86","IPPEL"])
#data[np.where(data[:,3]<0.0),3] += 360
#ax[4,0].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[4,0].set_xlabel(r"$\chi$ (H1C8/6)")
ax[4,0].set_xlim(0,2*np.pi)

ax[4,1].plot(xx,ippel_c42(xx-bb/2.),c=cp[8],label="Ippel",lw=1)
#data = np.array([[float(x) for x in line.split()] for line in open("h1c42.txt") if("#" not in line)])
#errors.append([ippel(data[ii,3]*ff-bb/2)-data[ii,1] for ii in range(data.shape[0])])
#labels.append(["h1c42","IPPEL"])
#data[np.where(data[:,3]<0.0),3] += 360
#ax[4,0].errorbar(data[:,3]*ff,data[:,1],fmt ='o',xerr=data[:,4]*ff,yerr=data[:,2],ms=2.5,c='0.5',zorder=10,elinewidth=0.75)
ax[4,1].set_xlabel(r"$\chi$ (H1C4/2)")
ax[4,1].set_xlim(0,2*np.pi)
ax[4,2].axis('off')

##################################

fig.savefig("karplus.png",dpi=400)
#fig.close()
plt.close()


# now errors
fig,ax = plt.subplots(4,1,figsize=(8.3,8))

# SUGAR
results_sugar = []
for j in range(9):
    mae = np.array(errors[j])**2
    results_sugar.append([np.sqrt(np.average(mae)),0.5*np.std(mae)/np.sqrt(np.average(mae))])

hasnoot = errors[0] + errors[3] + errors[6]
hasnoot = np.array(hasnoot)**2
results_sugar.append([np.sqrt(np.average(hasnoot)),0.5*np.std(hasnoot)/np.sqrt(np.average(hasnoot))])

davies = errors[1] + errors[4] + errors[7]
davies = np.array(davies)**2
results_sugar.append([np.sqrt(np.average(davies)),0.5*np.std(davies)/np.sqrt(np.average(davies))])

condon = errors[2] + errors[5] + errors[8]
condon = np.array(condon)**2
results_sugar.append([np.sqrt(np.average(condon)),0.5*np.std(condon)/np.sqrt(np.average(condon))])
    
results_sugar = np.array(results_sugar)
ax[0].bar([1,2,3,5,6,7,9,10,11,13,14,15],\
          results_sugar[:,0],yerr=results_sugar[:,1],\
          color=[cp[0],cp[1],cp[2],cp[0],cp[1],cp[2],cp[0],cp[1],cp[2],cp[0],cp[1],cp[2]],width=0.7)
ax[0].set_xticks([2,6,10,13,14,15])
ax[0].set_xticklabels(["H1'H2'","H2'H3'","H3'H4'","HASNOOT","DAVIES","CONDON"],rotation=15)
ax[0].set_ylabel("RMSE (Hz)")
ax[0].set_ylim(0,5)
ax[0].set_xlim(0.5,15.5)
ax[1].set_ylim(0,5)
ax[1].set_xlim(0.5,15.5)
ax[2].set_ylim(0,5)
ax[2].set_xlim(0.5,15.5)
ax[3].set_ylim(0,5)
ax[3].set_xlim(0.5,15.5)
print results_sugar[:,0]
########################
results_sugar = []
for j in range(9,13):
    mae = np.array(errors[j])**2
    results_sugar.append([np.sqrt(np.average(mae)),0.5*np.std(mae)/np.sqrt(np.average(mae))])

hasnoot = errors[9] + errors[11] 
hasnoot = np.array(hasnoot)**2
results_sugar.append([np.sqrt(np.average(hasnoot)),0.5*np.std(hasnoot)/np.sqrt(np.average(hasnoot))])

davies = errors[10] + errors[12] 
davies = np.array(davies)**2
results_sugar.append([np.sqrt(np.average(davies)),0.5*np.std(davies)/np.sqrt(np.average(davies))])

    
results_sugar = np.array(results_sugar)
ax[1].bar([1,2,5,6,13,14],\
          results_sugar[:,0],yerr=results_sugar[:,1],\
          color=[cp[3],cp[4],cp[3],cp[4],cp[3],cp[4]],width=0.7)
ax[1].set_xticks([1.5,5.5,13,14])
ax[1].set_xticklabels(["C4P(i+1)","C4P3","MOOREN","MARINO"],rotation=15)
ax[1].set_ylabel("RMSE (Hz)")
#####################################
print results_sugar[:,0]

results_sugar = []
for j in range(13,22):
    mae = np.array(errors[j])**2
    results_sugar.append([np.sqrt(np.average(mae)),0.5*np.std(mae)/np.sqrt(np.average(mae))])

hasnoot = errors[13] + errors[16] + errors[19]
hasnoot = np.array(hasnoot)**2
results_sugar.append([np.sqrt(np.average(hasnoot)),0.5*np.std(hasnoot)/np.sqrt(np.average(hasnoot))])

davies = errors[14] + errors[17] + errors[20]
davies = np.array(davies)**2
results_sugar.append([np.sqrt(np.average(davies)),0.5*np.std(davies)/np.sqrt(np.average(davies))])

condon = errors[15] + errors[18] + errors[21]
condon = np.array(condon)**2
results_sugar.append([np.sqrt(np.average(condon)),0.5*np.std(condon)/np.sqrt(np.average(condon))])
    
results_sugar = np.array(results_sugar)
ax[2].bar([1,2,3,5,6,7,9,10,11,13,14,15],\
          results_sugar[:,0],yerr=results_sugar[:,1],\
          color=[cp[3],cp[5],cp[6],cp[3],cp[5],cp[6],cp[3],cp[5],cp[6],cp[3],cp[5],cp[6]],width=0.7)
ax[2].set_xticks([2,6,10,13,14,15])
ax[2].set_xticklabels(["PH5'","PH5''","H3P","MOOREN","LANKHORST","LEE"],rotation=15)
ax[2].set_ylabel("RMSE (Hz)")
print results_sugar[:,0]

results_sugar = []
for j in range(22,26):
    mae = np.array(errors[j])**2
    results_sugar.append([np.sqrt(np.average(mae)),0.5*np.std(mae)/np.sqrt(np.average(mae))])

hasnoot = errors[22] + errors[24] 
hasnoot = np.array(hasnoot)**2
results_sugar.append([np.sqrt(np.average(hasnoot)),0.5*np.std(hasnoot)/np.sqrt(np.average(hasnoot))])

davies = errors[23] + errors[25] 
davies = np.array(davies)**2
results_sugar.append([np.sqrt(np.average(davies)),0.5*np.std(davies)/np.sqrt(np.average(davies))])

    
results_sugar = np.array(results_sugar)
ax[3].bar([1,2,5,6,13,14],\
          results_sugar[:,0],yerr=results_sugar[:,1],\
          color=[cp[0],cp[7],cp[0],cp[7],cp[0],cp[7]],width=0.7)
ax[3].set_xticks([1.5,5.5,13,14])
ax[3].set_xticklabels(["H4H5'","H4H5''","HASNOOT","DAVIES"],rotation=15)
ax[3].set_ylabel("RMSE (Hz)")
ax[3].axhline(1.0,lw=0.5,c='0.2',zorder=0)
ax[3].axhline(2.0,lw=0.5,c='0.2',zorder=0)
ax[0].axhline(1.0,lw=0.5,c='0.2',zorder=0)
ax[0].axhline(2.0,lw=0.5,c='0.2',zorder=0)
ax[1].axhline(1.0,lw=0.5,c='0.2',zorder=0)
ax[1].axhline(2.0,lw=0.5,c='0.2',zorder=0)
ax[2].axhline(1.0,lw=0.5,c='0.2',zorder=0)
ax[2].axhline(2.0,lw=0.5,c='0.2',zorder=0)
plt.subplots_adjust(left=None, bottom=0.1, right=None, top=0.95,
                    wspace=None, hspace=0.25)
#ax[0].grid(True, which='x')
print results_sugar[:,0]
fig.savefig("karplus_error.png",dpi=400)
