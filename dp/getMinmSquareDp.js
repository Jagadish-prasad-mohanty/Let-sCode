const checkSquare= (n) =>{
    const nn=Math.floor(Math.sqrt(n))
    return nn*nn===n?true:false
}
const getMinmSq = (n) =>{
    if (checkSquare(n)){
        return 1
    }
    const dp=new Array(n+1).fill(0);
    dp[0]=0
    dp[1]=1
    dp[2]=2

    dp[3]=3
    // console.log(dp);
    for (let j=4;j<=n;j++){
        if (checkSquare(j)){
            dp[j]=1;
            continue;
        }
        let minm=j;
        for (let i=1;i<=Math.floor(j/2);i++){
            const sum=dp[i]+dp[j-i];
            // console.log(sum,minm,i);
            if (sum<minm){
                minm=sum
            }
            // if (i===1 && j===5){
            //     console.log(i,j);
            //     console.log(sum);
            //     console.log(dp);
            // }
        }
        dp[j]=minm;
        // console.log(dp);
    }
    // console.log(dp);
    return dp[n]
}

console.log(getMinmSq(120));