#
#
#       BLOOM FILTER DATA STRUCTURE
#       AUTHOR: JIMWELAGUINALDO
#
#

import hashlib

class bloom_filter:

    def hash_md5(self, obj):
        return int(hashlib.md5(obj).hexdigest(), 16) % self.cont_size
    
    def hash_sha256(self, obj):
        return int(hashlib.sha256(obj).hexdigest(), 16) % self.cont_size
    
    def hash_sha384(self, obj):
        return int(hashlib.sha384(obj).hexdigest(), 16) % self.cont_size

    def hash_sha512(self, obj):
        return int(hashlib.sha512(obj).hexdigest(), 16) % self.cont_size

    def hash_sha1(self,obj):
        return int(hashlib.sha1(obj).hexdigest(), 16) % self.cont_size

    def __init__(self, cont_size, nb_hash):
        self.container = [0] * cont_size
        self.cont_size = cont_size
        self.nb_hash = nb_hash

    def add(self, obj):
        if(self.nb_hash == 3):
            self.container[self.hash_md5(obj)] = 1;
            self.container[self.hash_sha256(obj)] = 1;
            self.container[self.hash_sha384(obj)] = 1;

        elif(self.nb_hash == 5):
            self.container[self.hash_md5(obj)] = 1;
            self.container[self.hash_sha256(obj)] = 1;
            self.container[self.hash_sha384(obj)] = 1;
            self.container[self.hash_sha512(obj)] = 1;
            self.container[self.hash_sha1(obj)] = 1;
    
    def membership_test(self, obj): 
        if(self.nb_hash == 3):
            if(self.container[self.hash_md5(obj)] and
                    self.container[self.hash_sha256(obj)] and
                    self.container[self.hash_sha384(obj)]):
                return "maybe"
            else:
                return "no"

        elif(self.nb_hash == 5):
            if(self.container[self.hash_md5(obj)] and
                    self.container[self.hash_sha256(obj)] and
                    self.container[self.hash_sha384(obj)] and
                    self.container[self.hash_sha512(obj)] and
                    self.container[self.hash_sha1(obj)]):
                return "maybe"
            else:
                return "no"


