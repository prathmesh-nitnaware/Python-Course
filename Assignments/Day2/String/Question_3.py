#accept a string and display how many vowel characters are there inside it.

stg = str(input("Enter a string: "))
stg = stg.upper()
c =0
for i in range(len(stg)):
    if(stg[i]=='A' or stg[i]=='I' or stg[i]=='E' or stg[i]=='O' or stg[i]=='U'):
        c+=1

print(f"Total number of values in given string: {c}")
