filepath = 'story.txt'
vowels="AEIOUaeiou"
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if(line[0] in vowels):
            #print(line)
            print("Line {}: {}".format(cnt, line.strip()))
            cnt=cnt+1
        line = fp.readline() 
