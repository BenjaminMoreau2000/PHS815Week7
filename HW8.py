import numpy as np

BestGuesses=[]
TrueProbabilities=[]


#Give 100 data points for each true probability value
for k in range(0,100):
    for i in range(0,100):
        Pc=100-i#Simulate a coin that has a 0 to 100 percent chance of heads
        N=100#Exps
        Success=0#me
        for i in range(N):

            a=np.random.randint(0,101)
            if(a>Pc):
                Success+=1
        BestGuess=Success/N
        BestGuesses.append(BestGuess)
        TrueProbabilities.append(Pc/100)


from matplotlib import pyplot as plt


ax = plt.axes()

ax.set(facecolor = "blue")



plt.scatter(TrueProbabilities,BestGuesses,color='orange',alpha=.1)
plt.xlabel("True p")
plt.ylabel("Guessed p")
plt.title("Guessed probabilities for a coin that has a face probability ranging from 0 to 1, 100 data points at each value")

plt.show()
