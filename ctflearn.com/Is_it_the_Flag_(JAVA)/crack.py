print("Cracking the JAVA hash code...")
print()

t1 = 1472541258
t2 = 1471587914

count = 0

def get_hash(string):
    hashcode = 0
    for i in range(len(string)):
        hashcode += ord(string[i])*pow(31,len(string)-(i+1))
    return hashcode

def crack(target):
    initial = target%31
    initial = 31+initial
    results = []
    for i in range(initial,127,31):
        if i<=target:
            results.append(i)
    return results

def loop(target_1,target_2,str_1="",str_2=""):

    target_1_results = crack(target_1)
    target_2_results = crack(target_2)

    conclusions_1 = []
    conclusions_2 = []
    for i in target_1_results:
        for j in target_2_results:
            if chr(i).lower() == chr(j).lower() and chr(i).isprintable():
                conclusions_1.append( chr(i) )
                conclusions_2.append( chr(j) )
    

    for c in range(len(conclusions_1)):
        cstr_1 = str_1
        cstr_2 = str_2
        cstr_1 += conclusions_1[c]
        cstr_2 += conclusions_2[c]
        ctarget_1 = int((target_1-ord(conclusions_1[c]))/31)
        ctarget_2 = int((target_2-ord(conclusions_2[c]))/31)
        if (not ctarget_1 and not ctarget_2) and (get_hash(cstr_2[::-1]) == t2) and (get_hash(cstr_1[::-1]) == t1):
            global count
            count+=1
            print("Cracked string:",cstr_2[::-1],f"[{count}]")
        else:
            loop(ctarget_1,ctarget_2,str_1=cstr_1,str_2=cstr_2)

loop(t1,t2)
print()
print(f"A total of {count} combinations where discovered!")
