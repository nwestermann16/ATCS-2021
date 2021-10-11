dictionary_mountains = {}
dictionary_mountains['Kangchenjunga'] ='8586'
dictionary_mountains['Everest'] ='8848'
dictionary_mountains['Cho Oyu'] ='8188'
dictionary_mountains['Dhaulagiri'] ='8167'
dictionary_mountains['Makalu'] ='8485'

print("\nNames:")
for word, meaning in dictionary_mountains.items():
    print("Mountain: %s" % word)

print("\nELevation:")
for word, meaning in dictionary_mountains.items():
    print("Elevation: %s" % meaning)

print("\nDescription:")
for word, meaning in dictionary_mountains.items():
    print("%s" % word + " is %s" % meaning + " meters tall.")
