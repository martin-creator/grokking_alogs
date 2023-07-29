# Hash maps are data structures that store key-value pairs. 
# They are like arrays, but the keys are not ordered.
# They have a faster search time than lists, which is why they are used in search engines and databases.
# In Python, the Dictionary data types represent the implementation of hash tables.
# They use a hash function to calculate the index for a key and stores it in that index.
# A good hash map should have the following features: 
# 1. Fast lookup
# 2. Doesn't allow duplicate keys
# 3. Keys should be immutable
# 4. Keys should be hashable
# The most common hash function is the modulo operator.
# Other examples of hash functions are SHA, MD5, and HMAC.

# Example of a hash map
book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)

# To recap, hashes are good for
# • Modeling relationships from one thing to another thing
# • Filtering out duplicates
# • Caching/memorizing data instead of making your server do work


# A load factor is a measure of how full the hash table is allowed to get before its capacity is automatically increased.
# A higher load factor means that there are more keys per bucket, so there are more collisions,
# but it also means that the hash table is more likely to have unused buckets.
# This results in faster operations, especially when the hash table is mostly empty.
# A good rule of thumb is to keep the load factor below 0.7.
# This can be done by increasing the size of the hash table when the load factor exceeds some threshold.
# The choice of the threshold and the resizing method can have a large effect on the performance of the hash table,
# especially when there are many entries in it.
# The load factor is also sometimes known as the fill factor.
# The load factor and hash function determine how well the hash table works.

# Common uses cases for hash maps in real life are:
# • Indexing data is a common use case for hash maps. For example, we can store the index of a word in a document in a hash map.
# • In a web server, we can use a hash map to map the route to the corresponding handler.
# • Hash maps are used in caching. For example, we can cache the results of a search query in a hash map.
# • Hash maps are used in memoization. For example, we can store the results of a function in a hash map.
# • Hash maps are used in bidirectional mapping. For example, we can map the English word to the Spanish word and vice versa.
# • Hash maps are used in file systems for the index of a file.
# • Hash maps are used in routers for forwarding the packet to the correct outgoing link.
# • Hash maps are used in compilers for the symbol table in order to store the variables and their attributes.
# • Hash maps are used in caching in operating systems for the page table.
# • Hash maps are used in databases for indexing.
# • Hash maps are used in caching in CPUs for caching instructions and data.
# • Hash maps are used in routers, switches, and load balancers for storing the network connections.
# • Hash maps are used in cryptography for the one-way hash function.
# • Hash maps are used in Java, Python, and PHP programming languages.
# • Hash maps are used in JavaScript objects.
# • Hash maps are used in Perl programming language.
# • Hash maps are used in Ruby programming language.
# • Hash maps are used in Linux kernel.
# • Hash maps are used in NoSQL databases.
# • Hash maps are used in Redis database.
# • Hash maps are used in memcached database.
# • Hash maps are used in Cassandra database.
# • Hash maps are used in DynamoDB database.
# • Hash maps are used in memcached database.
# • Hash maps are used in Couchbase database.
# • Hash maps are used in Riak database.
# • Hash maps are used in Voldemort database.

# Hash maps are used in search engines for indexing.
# Hash maps are used in spell checkers for storing the dictionary.
# Hash maps are used in spam filters for storing the list of spammers.
# Hash maps are used in social networks for storing the list of friends.
# Hash maps are used in compilers for the symbol table.
# Hash maps are used in routers for forwarding the packet to the correct outgoing link.
# Hash maps are used in load balancers for storing the list of servers.


# The time complexity of hash maps is O(1) for insertion, deletion, and lookup.
# The space complexity of hash maps is O(n) where n is the number of elements in the hash map.
# The best case time complexity of hash maps is O(1) when there are no collisions.
# The worst case time complexity of hash maps is O(n) when all the keys are mapped to the same bucket.
# The average case time complexity of hash maps is O(1) when the keys are uniformly distributed across all the buckets.
# The amortized time complexity of hash maps is O(1) when the keys are uniformly distributed across all the buckets.
# The time complexity of hash maps is O(n) for traversal.
