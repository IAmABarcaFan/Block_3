import matplotlib.pyplot as plt

def read_data(filename):
        """Read data from text file containing:
        school department, grade, nationality
        Args:
        filename (str): Name of the file to extract the data.
        Returns:
        tuple: (list(emat_grades), list(cs_grades), list(nationality_data))
        """
        with open(filename, 'r') as f:
                lines = f.readlines()
                emat_grades = [float(line.split()[2])
                        for line in lines if line.split()[0] == 'Engineering']
                cs_grades = [float(line.split()[2])
                        for line in lines if line.split()[0] == 'Computer']
                nationality_data = [line.split()[3] for line in lines]
        return emat_grades, cs_grades, nationality_data

emat_grades, cs_grades, nationality_data = read_data("grades.txt")

# Cleaning up nationality data
unique_dict_1 = dict.fromkeys(nationality_data)
for key in unique_dict_1:
    unique_dict_1.update({key: nationality_data.count(key)/len(nationality_data)*100})
keys = unique_dict_1.keys()
values = unique_dict_1.values()

# Histogram
plt.hist(emat_grades, label='Engineering Mathematics', alpha=0.5, color='blue', bins=20)
plt.hist(cs_grades, label='Computer Science', alpha=0.5, color='red', bins=20)
plt.legend(loc='upper left')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Grades Distribution')
plt.show()

# Pie Chart
plt.pie(values, labels=keys)
plt.title('Nationalities of Students')
plt.show()