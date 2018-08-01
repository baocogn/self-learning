elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}
elements['lithium'] = 3
print('mithril' in elements)
print(elements)
n = elements.get("dilithium")
print(n is None)
print(n is not None)

#dictionaries: mutable + store mappings of unique keys to values
#identity_operators: - in: check whether a value is in a dictionary
#                    - get: looks up values in a dictionary, returns "None" if the key isn't found or a value of your choice

#identity_operators: - is: evaluates if both sides have the same identity
#                    - is not:            //            the different indentities
