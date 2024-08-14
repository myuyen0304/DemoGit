#Add some comment
#Doi gia tri cho 2 bien
def doicho(m,n):
    return n,m
# Thuat toan quick sort
def quicksort(L, R):
    global a
    if L >= R:
        return
    i = L
    j = R
    x = a[(L + R)//2]
    while True:
        while a[i]<x:
            i = i+1
        while a[j] > x:
            j = j-1
        if i <= j:
            a[i], a[j] = doicho(a[i], a[j])
            i = i+1
            j = j-1
        else:
            break
    quicksort(L, j)
    quicksort(i, R)
# Chuong trinh chinh 
n = int(input("Nhap n ="))    
a = []
for i in range(0, n):
    x = int(input("Nhap phan tu %d:" % (i+1)))
    a.append(x)
quicksort(0, n-1)
print("Day so khi duoc sap xep lai: ",a)
