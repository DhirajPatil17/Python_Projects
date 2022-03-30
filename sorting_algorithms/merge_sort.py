def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left_list=list1[:mid]
        right_list=list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i=0
        j=0
        k=0
        while len(left_list)>i and len(right_list)>j:
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i=i+1
                k=k+1
            else:
                list1[k]=right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            list1[k]=left_list[i]
            i=i+1
            k=k+1
        while j<len(right_list):
            list1[k]=right_list[j]
            j=j+1
            k=k+1
# n=int(input("enter the number"))
# list1=[int(input()) for i in range(n)]
list1=[3,2,6,5,8,7,1,9]
merge_sort(list1)
print("sorted list",list1)


