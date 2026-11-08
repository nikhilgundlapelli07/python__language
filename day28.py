import matplotlib.pyplot as plt

# # SECTION 1: LINE PLOT

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.show()







# # SECTION 2: ADDING A TITLE AND AXIS LABELS

# days = [1, 2, 3, 4, 5]
# temperatures = [28, 30, 29, 33, 31]

# plt.plot(days, temperatures)
# plt.title("Temperature During the Week")
# plt.xlabel("Day")
# plt.ylabel("Temperature (Celsius)")
# plt.show()







# # SECTION 3: CUSTOMIZING A LINE PLOT

# x = [1, 2, 3, 4]
# y = [10, 30, 20, 25]

# plt.plot(
#     x, y,
#     color="green",
#     linewidth=2,
#     marker="o",
#     linestyle=":"
# )
# plt.title("Customized Line Graph")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.grid(True)
# plt.show()





# # SECTION 4: BAR GRAPH

# subjects = ["Math", "Science", "English", "History"]
# marks = [85, 90, 78, 88]

# plt.bar(subjects, marks, color="skyblue")
# plt.title("Student Marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()





# # SECTION 5: PIE CHART

# labels = ["Math", "Science", "English", "History"]
# marks = [85, 90, 78, 88]

# plt.pie(
#     marks,
#     labels=labels,
#     autopct="%1.1f%%",
#     startangle=90      
# )
# plt.title("Marks by Subject")
# plt.axis("equal")
# plt.show()




# # SECTION 6: HISTOGRAM

# marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90]

# plt.hist(marks, bins=7, edgecolor="black")  #default bins=10
# plt.title("Distribution of Marks")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.show()

# # SECTION 7: SCATTER PLOT

# hours = [1, 2, 3, 4, 5, 6]
# marks = [40, 50, 55, 70, 80, 90]

# plt.scatter(hours, marks, color="red")
# plt.title("Study Hours vs Marks")
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")
# plt.show()

# # SECTION 8: BOX PLOT

# marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90]

# plt.boxplot(marks)
# plt.title("Distribution of Marks")
# plt.ylabel("Marks")
# plt.show()

# # SECTION 9: HEATMAP USING imshow()
# # Marks scored by students in different subjects
# data = [
#     [85, 90, 78],  # Rakesh
#     [70, 65, 88],  # Adhithya
#     [95, 80, 92],  # Ram
#     [50, 90, 70]   #Shyam
# ]

# plt.imshow(data, cmap="Blues", aspect="auto")
# plt.colorbar(label="Marks")
# # Label the axes
# marks = ['Maths', 'Physics', 'Chemistry']
# students = ["Rakesh", "Adhithya", "Ram", 'Shyam']
# plt.xticks(range(len(data[0])), marks )
# plt.yticks(range(len(data)), students )

# plt.title("Student Performance Heatmap")
# plt.xlabel("Subjects")
# plt.ylabel("Students")
# plt.show()



# SECTION 11: SUBPLOTS
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]
          

plt.subplot(1, 2, 1)                     
plt.plot(x, y1, marker="o")
plt.title("Increasing")
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(1, 2, 2)                    
plt.plot(x, y2, marker="o", color="orange")
plt.title("Decreasing")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()                      
plt.show()                               



#Modern way
fig, axes = plt.subplots(2, 2, figsize=(10, 8))  

axes[0, 0].plot([1, 2, 3])                      
axes[0, 0].set_title("Line Plot")

axes[0, 1].bar([1, 2, 3], [4, 5, 6])           
axes[0, 1].set_title("Bar Chart")

axes[1, 0].scatter([1, 2, 3], [3, 2, 5])       
axes[1, 0].set_title("Scatter Plot")

axes[1, 1].hist([1, 1, 2, 3, 3, 3])            
axes[1, 1].set_title("Histogram")
                             
plt.show()