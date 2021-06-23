def stockBuySell(arr, n):
    		#code here
		minF=0
		maxF=0
		res=[]
		for i in range(1,n):
		    if arr[i]>=arr[i-1]:
		        maxF=i
		        
		    else:
		        if arr[maxF]-arr[minF]>=1:
		            res.append([minF,maxF])
		        minF=i
		        maxF=i
		if arr[maxF]>arr[minF]:
		    res.append([minF,maxF])
# 		print(res)      /
		return res

print(stockBuySell([100,180,260,355,40,560,655],7))