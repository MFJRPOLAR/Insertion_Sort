from insertion_sort import * 

def main():
    # set local vairble to store list and first 
    data = []
    first = 0 

    # prompt the user to input the list values 
    data = list(map(int,input("Enter 10 numbers seperated by a space: ").split()))

    # prompt the user for first 
    first = int(input("Enter the index at which the sort will begin: "))

    # display original unsorted list input by the user
    for i in data: 
        print(i, end=" ")

    # call sort method
    sort(data,first)

    print()

    # display sort method
    for i in data: 
        print(i, end=" ")

if __name__ == "__main__":
    main()