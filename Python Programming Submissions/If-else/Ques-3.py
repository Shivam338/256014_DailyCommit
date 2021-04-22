# Write Python code that asks a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice.
# if user order even number of slices, price per slice is Rs 120.00.
# Print the total price depending on how many slices user orders.

slices= int(input("Enter number of slices required : "))
if slices%2==0 :
    Total_Price = 120*slices
else :
    Total_Price = 123*slices

print(Total_Price)