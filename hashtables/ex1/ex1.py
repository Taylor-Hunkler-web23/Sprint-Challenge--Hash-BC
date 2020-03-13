#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    #[2,4,6]  10

#loop through weights
    for i in range(0, len(weights)):
        
        w= weights[i]


        num = hash_table_retrieve(ht, limit-w)

#if it matches
        if num is not None:
            first_num = max(i, num)
            sec_num = min(i, num)
            print("num", num)
            print("first", first_num)
            print("sec", sec_num)

            return (first_num, sec_num)
        else:
            hash_table_insert(ht, w, i)
        # if weights[i] in ht:
        #     return (ht[weights[i]], weights[i])
        #     print(ht[weights[i]], weights[i])
        # else:
        #     ht[limit - weights[i]] = weights[i]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
