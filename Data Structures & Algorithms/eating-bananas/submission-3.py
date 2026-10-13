class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       #ok so my first thought is that we're looking for gcd so that the number of bananas divides by a value or we  

       #so the big idea here is to realize that minimum k or banana eating speed is 1, and the maximum k is the max number of bananas. This is because even if we increase our k to like 1000, the number of hours is still going to the be 4 for a set of 4 piles so increasing k is not going to make this mroe effecient
       #what we want to check is if the number of hours is less than h, we know that if we increase k, we will decrease h, and if we decrease k, we will increase h so we can use binary search
       #and we're looking for exactly h since that is the minimum k, if we increase k we will decrease h more


       maxk = max(piles)
       mink = 1
       mid = (maxk + mink)//2
       hours = 0
       closesthour=0

       
       while mink<=maxk:
           mid = (maxk+mink)//2
           for i in piles:
               hours=hours - (-i//mid)
           print(mid, hours)
           if hours<=h:
               closesthour=mid
               maxk=mid-1
           elif hours>h:
                mink = mid+1
           hours = 0

       return closesthour

       
           


            


       #so how to determine h
       #use mid and get the k/bananas 
       
       #print(-(-10//25))
      
       

       
