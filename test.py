

geese = [1,3,0,9,8,7,10,2]
self = geese[2]
ahead = [goose for goose in geese if goose > self]
leadGoose = min(ahead)
lead_i = geese.index(leadGoose)
print(ahead)
print(leadGoose)
print(lead_i)