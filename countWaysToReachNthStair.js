const countStair= (n,m) =>{
    if (n===0 || n===1){
        return n;
    }
    const obj=new Array(n+1)
    for (let i=0;i<=n;i++){
        obj[i]=0
    }
    obj[0]=1;
    obj[1]=1;
        // code here
      for (let i=2;i<=n;i++){
          let j=1
          while(j<=i && j<=m){
            obj[i]+=obj[i-j]
            console.log(i,obj[i]);
            j++;
          }
      }
    //   console.log((Math.pow(10,9)+7))
      console.log(obj)
      return obj[n]%(Math.pow(10,9)+7);


}
const obj=new Object({})
console.log(countStair(84,2));