class HashMap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def __contains__(self, key):                                        ## Checking if key, value exists in hashmap. Tc--> Avg:O(1) Worst: O(n)
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return True 
        return False

    def __len__(self):                                                  ## Getting the length TC------> O(1)
        return self.size

    def put (self, key, value):                                         ## Adding a key, value of hashmap. Tc--> Avg:O(1) Worst: O(n)
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    
    def get (self, key):                                                ## Getting the value for a key . Tc--> Avg:O(1) Worst: O(n)
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k,v in bucket:
            if k == key:
                return v
        
        raise KeyError ("Key not found! ")

    def remove(self, key):                                              ## Removing a key, value form hashmap Tc--> Avg:O(1) Worst: O(n)
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError ("Key Not Found !")

    def keys(self):                                                     ## getting all keys from hashmao TC--> O(n)
        return (list(k for bucket in self.buckets for k, _ in bucket))

    def values(self):                                                   ## getting all values from hashmao TC--> O(n)
        return (list(v for bucket in self.buckets for _, v in bucket))

    def items(self):                                                    ## getting all key, value pairs from hashmao TC--> O(n)
        return (list((k, v) for bucket in self.buckets for k, v in bucket))

    def _hash_function(self,key):                                       ## Private function 
        key_string = str(key)
        hash_result = 0

        for i in key_string:
            hash_result = (hash_result*31 + ord(i))% self.capacity

        return hash_result


if __name__ == "__main__":
    hm = HashMap(32)

    hm.put('name', "ABC")
    hm.put("Age", 21)
    hm.put("Gamer", False)

    print(hm.items())

    print(hm.get("name"))
    print(hm.keys())

    hm.remove("Gamer")
    print(hm.items())