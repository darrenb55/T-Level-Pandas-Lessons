print("step 1")
print("import the libraries you will need")
from pydoc import describe
import pandas as pd

print("step 2")
print("get the dataset")
print("step 3")
print("save it to a sensible variable name")
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', 
                      sep='|', index_col='user_id')

print("step 4")
print("look at the first 25 entries")

#Your code goes here:
print(df.iloc[:25])
print("#"*10)
input()

print("step 5")
print("look at the last 10 entries")
print(df.tail(10))
#Your code goes here:

print("#"*10)
input()

print("step 6")
print("find out the number of rows in the dataset")
print(len(df))
#Your code go1s here:

print("#"*10)
input()

print("step 7")
print("found out the number of columns in the dataset")
print(df.shape[1])
#Your code goes here:

print("#"*10)
input()

print("step 8")
print("print the names of all the columns")
print(list(df.columns))
#Your code goes here:

print("#"*10)
input()

print("step 9")
print("find out how the data is indexed (what are the labels)")
print(df.index)

#Your code goes here:

print("#"*10)
input()

print("step 10")
print("what are the data types of each column")
print(df.dtypes)
#Your code goes here:

print("#"*10)
input()

print("step 11")
print("print only the 'occupation' column")
print(df['occupation'])
#Your code goes here:

print("#"*10)
input()

print("step 12")
print("find out how many different occupations are in this dataset")

#Your code goes here:
print(df['occupation'].nunique())
print("#"*10)
input()

print("step 13")
print("what is the most frequent occupation")
print(df["occupation"].mode()[0])
#Your code goes here:

print("#"*10)
input()

print("step 14")
print("summarize the dataFrame")
print(df.describe())
#Your code goes here:

print("#"*10)
input()

print("step 15")
print("summarize every column in the dataFrame")
print(df.describe(include="All"))
#Your code goes here:

print("#"*10)
input()

print("step 16")
print("summarize only the occupation column")
print(df['occupation'].describe())
#Your code goes here:

print("#"*10)
input()

print("step 17")
print("what is the mean age of all the users")
print(df['Age'].mean())
#Your code goes here:

print("#"*10)
input()

print("step 18")
print("what is the least frequent occupation")
print(df['Occupation'].value_count().idxmin())
#Your code goes here:

print("#"*10)
input()

