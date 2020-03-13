#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # loop through
    for i in tickets:
        #add to hash table
        hash_table_insert(hashtable, i.source, i.destination)

       
        # get NONE 
        start_stop = hash_table_retrieve(hashtable, "NONE")
        print(start_stop,"ss")

#loop through from 
    for i in range(length):
        route[i] = start_stop

        print(route[i],"r")
        start_stop = hash_table_retrieve(hashtable, start_stop)
        print(start_stop,"2s")
        
        #remove none
    route.pop()
    return route
    

    
