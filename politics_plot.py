import matplotlib.pyplot as plt
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.govtrack.us/congress/bills/statistics"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
table = soup.findAll("div", attrs={'class': 'abs'})

text_values = [thing.text for thing in table]
float_values = []
for text_value in text_values:
	if "," not in list(text_value):
		float_values.append(float(text_value))
	else:
		text_value = text_value.replace(",", "")
		float_values.append(float(text_value))
enacted_laws = [float_values[i] for i in range(len(float_values)) if i%6==0]
enacted_laws = enacted_laws[::-1][:23]

total_legislation = [thing.text for thing in soup.findAll("th")][8:]
float_total_legislation = []
for total in total_legislation:
	float_total_legislation.append(float(total.replace(",", "")))
total_legislation = float_total_legislation[::-1][:23]

congresses = [i for i in range(93, 116)]
plt.plot(congresses, enacted_laws, '-b')
plt.ylim(0, 804)
plt.xlabel("Congress")
plt.ylabel("Enacted Laws")
plt.title("Fig. A: 93rd Through 115th Congress Legislature")
plt.savefig("enacted_laws.png")
plt.close()
plt.plot(congresses, total_legislation, '-r')
plt.ylim(0, 26222)
plt.xlabel("Congress")
plt.ylabel("Total Legislation")
plt.title("Fig. B: 93rd Through 115th Congress Legislature")
plt.savefig("total_legislation.png")
plt.close()