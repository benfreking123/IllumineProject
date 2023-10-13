- [[#New|New]]
- [[#Levels|Levels]]
- [[#Rarity|Rarity]]
	- [[#Rarity#Open|Open]]
	- [[#Rarity#Common|Common]]
	- [[#Rarity#Uncommon|Uncommon]]
	- [[#Rarity#Rare|Rare]]
	- [[#Rarity#Mythical|Mythical]]
	- [[#Rarity#Sacred|Sacred]]
	- [[#Rarity#Cursed|Cursed]]
- [[#Authors|Authors]]
- [[#Tags|Tags]]
	- [[#Tags#<u>Items</u>|Items]]
				- [[#Tool|Tool]]
				- [[#Servitor|Servitor]]
				- [[#Talisman|Talisman]]
	- [[#Tags#<u>Spirit</u>|Spirit]]
				- [[#Abilities|Abilities]]
			- [[#Classes|Classes]]
	- [[#Tags#<u>Realms</u>|Realms]]
				- [[#Classes#Lucid|Lucid]]
				- [[#Classes#Astral|Astral]]

- - - 

## New
```start-multi-column
ID: ID_gdpn
Number of Columns: 2
Largest Column: standard
```
### Created
```dataview
LIST
FROM "New" and -"New/-Actions" and -"New/Potential"
SORT file.ctime DESC

Limit 
16
```

--- column-end ---

### Modified
```dataview
LIST
FROM "New" and -"New/-Actions" and -"New/Potential"
SORT file.mtime DESC

Limit 
16
```

--- end-multi-column
- - -
## Levels

```start-multi-column
ID: ID_levels
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 0
```dataview
LIST
FROM #Level0
SORT file.name ASC
```

--- column-end ---

### Level 1
```dataview
LIST
FROM #Level1
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_1
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 2
```dataview
LIST
FROM #Level2
SORT file.name ASC
```

--- column-end ---

### Level 3
```dataview
LIST
FROM #Level3
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_2
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 4
```dataview
LIST
FROM #Level4
SORT file.name ASC
```

--- column-end ---

### Level 5
```dataview
LIST
FROM #Level5
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_3
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 6
```dataview
LIST
FROM #Level6
SORT file.name ASC
```

--- column-end ---

### Level 7
```dataview
LIST
FROM #Level7
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_4
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 8
```dataview
LIST
FROM #Level8 
SORT file.name ASC
```

--- column-end ---

### Level 9
```dataview
LIST
FROM #Level9
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_5
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 10
```dataview
LIST
FROM #Level10
SORT file.name ASC
```

--- column-end ---

### Level 11
```dataview
LIST
FROM #Level11
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_6
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 12
```dataview
LIST
FROM #Level12 
SORT file.name ASC
```

--- column-end ---

### Level 13
```dataview
LIST
FROM #Level13
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_7
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 14
```dataview
LIST
FROM #Level14
SORT file.name ASC
```

--- column-end ---

### Level 15
```dataview
LIST
FROM #Level15
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_8
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 16
```dataview
LIST
FROM #Level16
SORT file.name ASC
```

--- column-end ---

### Level 17
```dataview
LIST
FROM #Level17
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_9
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 18
```dataview
LIST
FROM #Level18
SORT file.name ASC
```

--- column-end ---

### Level 19
```dataview
LIST
FROM #Level19
SORT file.name ASC
```

--- end-multi-column

```start-multi-column
ID: ID_levels_10
Number of Columns: 2
Largest Column: standard
Border: [on]
```

### Level 20
```dataview
LIST
FROM #Level20
SORT file.name ASC
```

--- column-end ---

### Level -
```dataview
LIST
FROM #Level-
SORT file.name ASC
```

--- end-multi-column

- - -


## Rarity


```start-multi-column
ID: ID_Rarity
Number of Columns: 1
Column Size: Full
Border: [on]
```


### Open
```dataview
Table 
file.tags AS Tag

FROM #Open 

SORT 
file.mtime 
DESC

LIMIT
12
```


### Common
```dataview
Table 
file.tags AS Tag

FROM #Common

SORT 
file.mtime 
DESC
```

### Uncommon
```dataview
Table 
file.tags AS Tag

FROM #Uncommon

SORT 
file.mtime 
DESC

LIMIT
12
```

### Rare
```dataview
Table 
file.tags AS Tag

FROM #Rare

SORT 
file.mtime 
DESC

LIMIT
12
```

### Mythical
```dataview
Table 
file.tags AS Tag

FROM #Mythical

SORT 
file.mtime 
DESC

LIMIT
12
```

### Sacred
```dataview
Table 
file.tags AS Tag

FROM #Sacred

SORT 
file.mtime 
DESC

LIMIT
12
```

### Cursed
```dataview
Table 
file.tags AS Tag

FROM #Cursed

SORT 
file.mtime 
DESC

LIMIT
12
```

--- end-multi-column

- - -
## Authors
```dataview
TABLE 
file.name as "Title",
file.inlinks as "Works"

from "- Individuals/Authors"

SORT 
file.ctime 
DESC

LIMIT
12
```

- - -  

## Tags

```start-multi-column
ID: ID_5avy
Number of Columns: 2
Largest Column: standard
```
### <u>Items</u>
###### Tool
```dataview
LIST
FROM #Tool
SORT file.mtime DESC
```

###### Talisman
```dataview
LIST
FROM #Talisman 
SORT file.mtime DESC
```

###### Servitor
```dataview
LIST
FROM #Servitor 
SORT file.mtime DESC
```

###### Concept
```dataview
LIST
FROM #Concept 
SORT file.mtime DESC
```


###### Individual
```dataview
LIST
FROM #Individual 
SORT file.mtime DESC
```

--- column-end ---

### <u>Spirit</u>
###### Abilities
```dataview
LIST
FROM #Ability  
SORT file.mtime DESC
```
###### Classes
```dataview
LIST
FROM #Class
SORT file.mtime DESC
```
### <u>Realms</u>
###### Lucid
```dataview
LIST
FROM #Lucid 
SORT file.mtime DESC
```
###### Astral
```dataview
LIST
FROM #Astral
SORT file.mtime DESC
```

--- end-multi-column

