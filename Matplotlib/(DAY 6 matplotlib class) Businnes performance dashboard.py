import matplotlib.pyplot as plt 
weeks = [1, 2, 3, 4]
engagement = [120, 180, 260, 340]
plt.style.use("ggplot")
plt.plot(weeks,engagement,
         color="green",
         linewidth=2,
         alpha=0.8,
         marker="o")
plt.title("Campaign Engagement Growth""Campaign Engagement Growth")
plt.xlabel("Week")
plt.ylabel("Engagement Score")
plt.grid(True)
plt.tight_layout()
plt.show()