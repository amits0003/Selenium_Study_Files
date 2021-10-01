# Node Object


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # adding new node

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    # insert in between linekdlist
    def insert_after(self, prev_node, new_data):

        if prev_node is None :
            print("The previous node must be in linkedlist")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node


    # append at the end

    def append_at_end(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head  = new_node
            return

        last = self.head

        while(last.next):
            last = last.next

        last.next =  new_node

    def print_Link_List(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next





if __name__ == "__main__":
    link_List = LinkedList()

    # link_List.head = Node("Amit")
    #
    # second = Node("Sumit")
    #
    # third = Node("Dev")
    #
    # link_List.head.next = second
    #
    # second.next = third

    link_List.append_at_end(12)

    link_List.push(43)

    link_List.push(45)

    link_List.append_at_end(2324)

    link_List.insert_after(link_List.head.next, 323)

    print("The new Linked list : ", end=" ")

    link_List.print_Link_List()
