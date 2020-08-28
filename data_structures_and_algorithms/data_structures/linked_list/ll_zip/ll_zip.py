def zipLists(list1,list2):
    nodes_counter_li1 = 0
    nodes_counter_li2 = 0

    current = list1.head
    while current != None:
        current = current.next
        nodes_counter_li1 += 1

    current = list2.head
    while current != None:
        current = current.next
        nodes_counter_li2 = nodes_counter_li2 + 1 

    if nodes_counter_li1 > nodes_counter_li2:
        l1 = list1
        l2 = list2
    else:
        l1 = list2
        l2 = list1

    current = l1.head 
    l2_current = l2.head 
    while current != None and l2_current != None: 
        l1_next = current.next
        l2_next = l2_current.next
        l2_current.next = l1_next 
        current.next = l2_current 
        current = l1_next 
        l2_current = l2_next 
    l2.head = l2_current 
    return l1.toString()


    
    # @staticmethod
    # def merge(list1, list2):
    #     current = list1.head
    #     # les = current.next
    #     current2 = list2.head

    #     while True:

    #         if current.value < current2.value:
    #             list1.insertAfter(current.value, current2.value)
    #             try:
    #                 current2 = current2.next.value
    #                 current.next.value
    #             except:
    #                 break
    #             else:
    #                 o = current.next
    #                 current = o.next
    #                 current2 = current2.next

    #         elif current.value >= current2.value:
    #             list1.insertBefore(current.value, current2.value)
    #             try:
    #                 current2 = current2.next.value
    #                 current.next.value
    #             except:
    #                 break
    #             else:
    #                 current = current.next
    #                 current2 = current2.next
    #     return list1.toString()
