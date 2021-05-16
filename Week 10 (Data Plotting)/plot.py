import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_title("Production of Pointed Sticks")
ax.set_xlabel("Month")
ax.set_ylabel("Pointed Sticks")

ax.set_xlim(1,4)
ax.set_ylim(0,5.5)

xlabels = ['jan','feb','mar','apr']
ax.set_xticklabel(xlabels)


x = [1,2,3,4]
y = [1,2,5,3]

ax.plot(x,y, marker = S,)

ax.grid()
plt.show()
