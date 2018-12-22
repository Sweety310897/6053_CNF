def main():
    temp = load_file("data.csv")
    print(temp)
def load_file(filename):
    dic = {}
    list1 = []
    with open(filename, 'r') as filename:
        for line in filename:
            temp1 = line.split(",")
            #temp1 = temp.split(",")
            #print(temp1)
            dic[temp1[0]] = temp1[1] + temp1[2]
            #dic[line] = 0
            # list1.append(line)
            # print(list1)
    return dic
if __name__ == "__main__":
    main()