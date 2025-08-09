import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import matplotlib.cm as cm

def gecis():
    gecis = 4  # 1 dakikada geçen ortlama araba sayısı
    x = np.arange(0, 16)  # olabilecek araç geçiş sayısı
    pois_olasılıkları =poisson.pmf(x, mu=gecis)
    pois_olasılıkları *=100
    newpois = np.round(pois_olasılıkları,1)
    plt.figure(figsize=(10, 7))
    colors = cm.magma(np.linspace(0,1,len(x)))  # x'in her elemanı için bir renk oluştur

    plt.bar(x, newpois,color=colors,edgecolor="black")
    plt.plot(x,newpois, color="k", linestyle="-", marker="o", markersize=6)
    font1 = {"family":"serif","color":"darkred","size": 13}
    font2 = {"family":"serif","color":"darkblue","size": 18}
    plt.title("Poisson Distribution",fontdict=font2)
    plt.xlabel("Number of Cars Per Minute",fontdict=font1)
    plt.yticks(newpois,[f"{x}%" for x in newpois])
    plt.ylim(0.2,20)
    plt.ylabel("Probability(%)",fontdict=font1)

    for i, v in enumerate(newpois):   #her barın üstüne olasılığını yazdık
        plt.text(x[i],v + 0.5,f"{v}%",ha='center',fontsize=10)

    plt.grid(axis='y',linestyle="--",alpha=0.6)
    plt.savefig("poisson_cars_per_minute.png",bbox_inches='tight')
    plt.show()

def main():
    gecis()

if __name__ == "__main__":
    main()