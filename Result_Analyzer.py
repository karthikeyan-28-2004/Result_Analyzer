import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 📂 Step 1: Student Data
# ==============================
data = {
    'Name': ['Karthi', 'Anu', 'Vikram', 'Priya', 'Raj'],
    'Maths': [78, 45, 89, 67, 92],
    'Science': [85, 56, 91, 72, 88],
    'English': [74, 68, 80, 65, 70]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# ==============================
# 📊 Step 2: Process Data
# ==============================
# Calculate Total and Average
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Maths', 'Science', 'English']].mean(axis=1)

# Assign Grades
def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 75:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 40:
        return 'C'
    else:
        return 'Fail'

df['Grade'] = df['Average'].apply(assign_grade)

# ==============================
# 📋 Step 3: Display Results
# ==============================
print("=== Student Result Analyzer ===")
print(df)

print("\nClass Average:", round(df['Average'].mean(), 2))
print("Topper:", df.loc[df['Total'].idxmax(), 'Name'])

# ==============================
# 📈 Step 4: Visualization
# ==============================
df.set_index('Name')[['Maths', 'Science', 'English']].plot(kind='bar')
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
