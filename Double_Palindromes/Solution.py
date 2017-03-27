#https://leetcode.com/problems/palindrome-pairs/#/description
#todo: testing

''' My solution '''

class Solution:
    def add_to_dict(self, thelist):
        res = []
        d = {}
        for i, w in enumerate(thelist):
			if w[::-1] in thelist:
			    d[w] = i
			    
	for k,v in d.items():
		for k2,v2 in d.items():
		    if k[::-1] == k2:
		        res.append([v,v2])
        return res


''' Optimal solution '''

class Solution:
  def add_to_dict(self, thelist):
     res = []
     d = {}
     for i, w in enumerate(thelist):
         if w[::-1] in thelist:
             d[w] = [i, thelist.index(w[::-1])]
     return d.values()
