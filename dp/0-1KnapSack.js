const createDp= (n,W)=>{
    const dp=new Array(n+1);
    for (let i=0;i<=n;i++) {
        const temp=[]
        for (let j=0;j<=W;j++){
            temp.push(-1)
        }
        dp[i]=temp
    }
    
    return dp
}
const knapSack = (W,n, wt, val, )=>
    { 
       // code here
        const dp=createDp(n,W);
        console.log(dp)
        for (let i=0;i<=n;i++) {
            for (let j=0;j<=W;j++){
                if (i===0 || j===0){
                    // console.log(i,j)
                    dp[i][j]=0
                
                }
            }
        }
        console.log(dp)
        for (let i=1;i<=n;i++){
            for (let j=1;j<=W;j++){
                if (wt[i-1]<=j){
                    dp[i][j]=Math.max(dp[i-1][j],
                        val[i-1]+dp[i-1][j-wt[i-1]])
                }else{
                    dp[i][j]=dp[i-1][j]
                }
            }
        }
        console.log(dp)
        return dp[n][W]
        
    }

console.log(knapSack(4,3,[4,5,1],[1,2,3]));