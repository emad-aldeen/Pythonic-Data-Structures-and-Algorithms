# Hashtables
one of the famous ways to encrypt data and save it in..

<br>
<hr>

## Challenge

* Implement a Hashtable with the following methods:

    1.  `add`: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

    2. `get`: takes in the key and returns the value from the table.

    3. `contains`: takes in the key and returns a boolean, indicating if the key exists in the table already.

    4. `hash`: takes in an arbitrary key and returns an index in the collection.

<br>


## Approach & Efficiency
well i learned about one of the greatest ways to encrypt data and save it in less 'Big(O)' complexity, cuse Big(O) for hash_table is:

* Time Complexity: ***O(1)***
* Space Complexity: ***O(n)***

<br>
<br>
<hr>

## APIs

* `.hash(key)` : it hashing any inputed key with hash method and returns it hashed in range the hash_table size

* `.add(key, value)` : it used to add your kay and value to the hash_table

* `.get(key)` : it used to get you the value of your inputed key if it exist in the hash table

* `.contains(key)` : your not sure if your key is exist on hash table? this fuction will check and return boolean