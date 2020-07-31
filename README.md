# small_real_estate_calculator
small real estate calculator by core python

### Throughout the day we need to calculate how much revenue we have generated by matching our users with their dream properties and passing them onto an agent,
We match a variety of people looking for very different properties, here are the types of 'leads' we currently use and the price for each one:

```
LeadCode Name Price
B Buy £10
R Rent £5
ST Short Term £2.5
```

### Sometimes agents have special promotions for providing them with certain combinations of leads, for example the promotions may be:

`providing more than 5 buy leads gives us a £10 bonus`

`providing more than 8 rent leads we get a 10% bonus on total base price.`

### Technical Tasks:

We need you to provide us with a piece of code to help us calculate the total price of our
leads. An example of calling this code is below:


```python
calculator = Calculator(pricing_rules)
calculator.add(LeadCode)
calculator.add(LeadCode)
calculator.add(LeadCode)
total = calculator.total()
```


You should be able to implement the Calculator class above such that it will calculate the
total price for every lead added to it.
Use the pricing rules stated above and the test data specified below.
You do not need to worry about when or how it will be run, only that it must be instantiated
with a set of pricing rules, leads of various types can be added to it and a ‘total’ method
provided.
Provide us with a piece of ​ Python​ code via a zipped folder, or through a github repo.


Test Data:
6 x B, 2 x R, 1 x ST

£82.5

1 x B, 10 x R

£65

### how to run [command prompt]

`python calculator.py`

and then just give the input as it is asking
