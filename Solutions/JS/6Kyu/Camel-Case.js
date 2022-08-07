String.prototype.camelCase=function(){
    let str = this.split(' ');
    let newstr = []
    
    for (let word of str) 
    {
        if (word) 
        {
            let upper = ''
            upper += word[0].toUpperCase();
            
            for (let i = 1; i < word.length; i++) 
            {
                upper += word[i]
            }
            newstr.push(upper)
        }
    }
    
    return newstr.join('')
  }