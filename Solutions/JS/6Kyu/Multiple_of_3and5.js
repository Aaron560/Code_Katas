function solution(number){
    //sets sum to 0;
    let sum = 0;
    
    //for loops i if less than num. 
    for (let i = 0; i < number; i++) 
    {
        //if i divisible by 3/5 or both. Add sum + i to sum.
        if (i % 3 === 0 || i % 5 === 0 || (i % 3 === 0 && i % 5 ===0)) 
        {
            sum = sum += i;
        }
    }
    return sum;
  }