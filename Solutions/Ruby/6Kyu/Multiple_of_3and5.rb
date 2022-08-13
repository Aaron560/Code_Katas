def solution(number)
  sum = 0
  for i in 3...number
    if i % 3 == 0 || i % 5 == 0
      sum += i
    end
  end
  return sum
end
