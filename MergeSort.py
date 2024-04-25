
from Apartment import Apartment

def merge_sort(apartment_list):
    if len(apartment_list)>1:
        mid = len(apartment_list)//2
        lefthalf = apartment_list[:mid]
        righthalf = apartment_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or not righthalf[j] < lefthalf[i]:
                apartment_list[k]=lefthalf[i]
                i=i+1
            else:
                apartment_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            apartment_list[k]=lefthalf[i]
            i = i+1
            k= k+1

        while j < len(righthalf):
            apartment_list[k]=righthalf[j]
            j = j+1
            k = k+1

def ensure_sorted_ascending(apartment_list):
    for a in range(len(apartment_list))[1:]:
        if apartment_list[a - 1] > apartment_list[a]:
            return False
    return True

    
def get_best_apartment(apartment_list):
    merge_sort(apartment_list)
    return apartment_list[0].get_apartment_details()

def get_worst_apartment(apartment_list):
    merge_sort(apartment_list)
    return apartment_list[-1].get_apartment_details()

def get_affordable_apartments(apartment_list, budget):
    merge_sort(apartment_list)
    string = ''
    for a in apartment_list:
         if a.get_rent() <= budget:
             string += a.get_apartment_details() + '\n'
    index = len(string)
    while index > 0 and string[index - 1] == '\n':
        index -= 1
    return string[:index]
