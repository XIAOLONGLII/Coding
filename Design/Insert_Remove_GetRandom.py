''' Question
Design a class:
  1. inserting a value (no duplicates)
  2. removeing a value 
  3. GetRadonm a value that is already inserted (with euqal probability) 
'''

''' Clarifications:
1. is the value a integer? FLoat? a person?
2. is there a limitation constrains?
'''

''' Think loud:
1. What data structrue can do insert, remove and getRadom? 
   array(list), linkedList, HashMap, HashSet....
2. which data structure can be very efficient, let's say O(1) runtime?
   a. insert at the end of list
   b. remove at the end of list
   c. random number, then get that index.
3. how to insert at the end of list:
   a. is the list already have that element? 
      we can use a hashmap to check it, if yes then skip 
         if element in hashmap:
            return
   b.if no, we add add to the end of list, (append), then add to hashmap 
         ln = len(list)
         hashmap[element] = ln
         list.append(element)
 4. remove:
    a. is the element not in hashmap?
       if element not in hashmap:
          return
       else:
         index = hashmap[element]
         swap index with last index
         last_index = len(list) - 1
         temp = list[index]
         list[index] = list[last_index]
         list[last_index] = temp 
         
         list = list[:-1]
   
   5. getRandom
      random_index = Random.random(0, len(list))
      return list[random_index]
   6. Search
      return hashmap.get(element, None)
          
'''

####################################

####################################
