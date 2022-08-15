function saleHotdogs(n){
    const saleHotdogs = n => n * (n<5 ? 100: (n>=5 && n<10 ? 95: 90))
    return saleHotdogs(n)
  }