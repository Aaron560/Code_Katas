def filter_list(l)
  # return a new list with the strings filtered out
  l.reject { |i| i.is_a? String }
end
