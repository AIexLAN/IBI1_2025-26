seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
import re
pattern= r'AUG(?:.{3})*?(?:UAA|UGA|UAG)'
orf = re.findall(pattern, seq)
print(orf)
longest_orf = max(orf, key=len)
print(longest_orf)