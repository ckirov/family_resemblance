# family_resemblance
Language genealogy tools

# Requirements

Family trees are stored in:

```
family_trees.dat
```

# Usage

API is exposed in (see **__main** for examples)

```
family_tree_distance.py: 
```

There are two main functions:

```
#compute the distance between two languages (input as iso693 codes)
distance(source,target,bibles_only=True)

#find the most similar language to the given iso code
nearest(source,bibles_only=True)
```

The 'bibles_only' parameter determines whether you only want to consider languages for which there is a bible. If it is set to False, all the languages in ethnologue are considered.
