# Ekumen Training Program - Testing

### This repository contains the following two projects:

## 1.Basics

Intended to be provide practical examples of the basic concepts of testing.

See also this guide https://docs.google.com/presentation/d/1kWtkZ5LRkFt7t4ruX5-JJXBgzyKMRPwzXXymMuwTvv0/edit?usp=sharing 


for running tests, use `make` and then
```
cd Basics
pytest 01_discovery/ -v
pytest 02_hooks/test_hooks.py  -s
pytest 02_hooks/test_hooks_class.py  -s
```

Play with it! modify things and experiment!




## 2.Checkout

A finished example project, for a TDD practice for implementing requirements defined in test_cases.txt

- can create an instance of the Checkout class
- can add an item price
- can add an item
- can calculate the current total
- can add multiple items and get correct total
- can add discount rules
- can apply discount rules to the total
- exception is thrown for Item Added without a price
