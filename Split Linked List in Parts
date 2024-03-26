class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        noofele=0
        temp=head
        while temp:
            noofele+=1
            temp=temp.next
        appnoofele=noofele//k
        extraele=0
        if (k>noofele):
            appnoofele=1
        else:
            extraele=noofele-appnoofele * k
        iteratedcount=0
        temp=head
        resultList=[]
        while temp:
            if k==1:
                resultList.append(head)
                k-=1
                break
            iteratedcount+=1
            if iteratedcount == appnoofele:
                if (extraele > 0):
                    temp=temp.next
                    extraele-=1
                if temp:
                    temp2=temp.next
                    temp.next = None
                    resultList.append(head)
                    temp=temp2
                    head=temp2
                    iteratedcount=0
                    k-=1
            else:
                temp=temp.next
        while k>0:
            k-=1
            resultList.append(ListNode(""))
        return resultList
