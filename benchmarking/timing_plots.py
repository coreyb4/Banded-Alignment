import matplotlib.pyplot as plt
import json

with open("times.json") as json_file:
    D = json.load(json_file)

lengths = [25, 50, 100, 250, 500, 750, 1000, 2000, 3000, 4000, 5000]
bandwidths = [1, 3, 5, 10, 20]


nw_times = []
banded_1_times = []
banded_3_times = []
banded_5_times = []
banded_10_times = []
banded_20_times = []

for l in lengths:
    nw_times.append(D[str(l)]["NW"])
    banded_1_times.append(D[str(l)]["1"])
    banded_3_times.append(D[str(l)]["3"])
    banded_5_times.append(D[str(l)]["5"])
    banded_10_times.append(D[str(l)]["10"])
    banded_20_times.append(D[str(l)]["20"])

print(nw_times)


plt.plot(lengths, nw_times, label="Needleman Wunsch", color="blue")
plt.plot(lengths, banded_1_times, label="Banded (k = 1)", color="green")
plt.plot(lengths, banded_3_times, label="Banded (k = 3)", color="orange")
plt.plot(lengths, banded_5_times, label="Banded (k = 5)", color="purple")
plt.plot(lengths, banded_10_times, label="Banded (k = 10)", color="brown")
plt.plot(lengths, banded_20_times, label="Banded (k = 20)", color="#6495ED")


plt.xlabel("Length")
plt.ylabel("Time of Execution (s)")
plt.title("Average Execution Time of Alignment Algorithms")

# Add a legend
plt.legend()

# Display the plot
plt.show()
