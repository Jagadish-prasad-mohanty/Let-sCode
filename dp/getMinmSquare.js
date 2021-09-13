const checkSquare= (n) =>{
    const nn=Math.floor(Math.sqrt(n))
    return nn*nn===n?true:false
}
const getMinmSq = (n) =>{
    if (n<=3 ){
        return n
    }
    if (checkSquare(n)){
        return 1
    }
    let minm=n;
    for (let i=1;i<=Math.floor(Math.sqrt(n));i++){
        const right=getMinmSq(n-(i*i))
        const sum=1+right;
        console.log(sum,minm,i);
        if (sum<minm){
            minm=sum
        }
    }
    return minm
}

console.log(getMinmSq(29));