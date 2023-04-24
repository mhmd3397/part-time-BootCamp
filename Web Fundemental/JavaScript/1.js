
function greaterY(arr, Y) {
    //your code here 
    var count=0;
    for( var i =0;i<arr.length;i++){
        if (Y<arr[i]){
            count++;
        }
    }
    return count; 
}
var x = greaterY([-1],0);
console.log(x);
function maxMinAvg(arr) {
    //your code here 
    var max=0, min=0, sum=0, avg=0 ;
    var arrnew;
    for( var i =0;i<arr.length;i++){
        if(max<arr[i]){
        max=arr[i];
        }
    
    }
    for(i =0;i<arr.length;i++){
        if(min>arr[i]){
        min=arr[i] ;  
        }
    
    }
    for(i =0;i<arr.length;i++){
        sum+=arr[i];
        
    }
    avg+=sum/arr.length;
    arrnew.push(max);
    arrnew.push(min);
    arrnew.push(avg);
    return arrnew; 
}
var x=maxMinAvg([0,2,4]);
console.log(x);