# Topic 3. Graphs and Trees
## Task 1. Application of the maximum flow algorithm for goods logistics

Develop a program to model the flow network for goods logistics from warehouses to stores using the maximum flow algorithm. Analyze the results and compare them with theoretical knowledge.

![Graph](doc/Figure_1.svg)

### Prerequisites 
```bash
poetry install
poetry shell
```

### To draw graph
```bash
poetry run python .\app\logistic_draw.py
```

### To run alg
```bash
poetry run python .\app\logistic.py -matrix
```
where 
-matrix - print capacity matrix. Optional

### Results:
#### Actual Flow of Goods

| Terminal  | Shop  | Actual Flow (units) |
|-----------|---------|--------------------------|
| Термінал 1 | Магазин 1  | 15  |
| Термінал 1 | Магазин 2  | 10  |
| Термінал 1 | Магазин 3  | 20  |
| Термінал 1 | Магазин 4  | 15  |
| Термінал 1 | Магазин 5  | 10  |
| Термінал 1 | Магазин 6  | 20  |
| Термінал 1 | Магазин 7  | 15  |
| Термінал 1 | Магазин 8  | 15  |
| Термінал 1 | Магазин 9  | 10  |
| Термінал 1 | Магазин 10 | 0   |
| Термінал 1 | Магазин 11 | 0   |
| Термінал 1 | Магазин 12 | 0   |
| Термінал 1 | Магазин 13 | 0   |
| Термінал 1 | Магазин 14 | 0   |
| Термінал 2 | Магазин 1  | 0   |
| Термінал 2 | Магазин 2  | 0   |
| Термінал 2 | Магазин 3  | 0   |
| Термінал 2 | Магазин 4  | 10  |
| Термінал 2 | Магазин 5  | 10  |
| Термінал 2 | Магазин 6  | 10  |
| Термінал 2 | Магазин 7  | 15  |
| Термінал 2 | Магазин 8  | 15  |
| Термінал 2 | Магазин 9  | 10  |
| Термінал 2 | Магазин 10 | 20  |
| Термінал 2 | Магазин 11 | 10  |
| Термінал 2 | Магазин 12 | 15  |
| Термінал 2 | Магазин 13 | 5   |
| Термінал 2 | Магазин 14 | 10  |

#### Result analysis

**1. Which terminals provide the highest flow of goods to stores?**
**Answer:** 'Термінал 1' provides a flow of 60 units.

**2. Which routes have the lowest capacity, and how does this impact the overall flow?**
**Answer:** Overall, the routes from 'Термінал' to 'Склад' have low capacity.
- 'Термінал 1' should have a capacity of 130 units instead of 60 units.
- 'Термінал 2' should have a capacity of 130 units instead of 55 units.
- The entire network is inefficient due to the low capacity of 'Термінал'.

**3. Which stores received the least goods, and can their supply be increased by improving the capacity of certain routes?**
**Answer:**
- The capacity from 'Термінал 2' to 'Склад 4' is 30 units, but 'Склад 4' can supply (15+10+20+5+10=60).
- Therefore, 'Магазин 10' to 'Магазин 14' receive the least amount of goods.

**4. Are there bottlenecks that can be eliminated to improve the efficiency of the logistics network?**
**Answer:** Yes.
- 'Склад 1' can supply (15+10+20=45), but 'Термінал 1' can only supply 25. The capacity from 'Термінал 1' to 'Склад 1' should be increased to 45 units.
- 'Склад 2' can supply (15+10+25=50), but 'Термінал 1' and 'Термінал 2' together supply only 20+10=30 units. The route capacity should be increased:
  - 'Термінал 1' to 'Склад 2' to 30 units.
  - 'Термінал 2' to 'Склад 2' to 20 units.
- 'Склад 3' can supply (15+10+20=45), but 'Термінал 1' and 'Термінал 2' together supply only 15+15=30 units. The route capacity should be increased:
  - 'Термінал 1' to 'Склад 3' to 30 units.
- 'Склад 4' can supply (15+10+20+5+10=60), but 'Термінал 2' supplies only 30 units. The route capacity should be increased:
  - 'Термінал 1' to 'Склад 4' to 60 units.


## Task 2. Comparing the performance of OOBTree and dictionary for segmented queries

Develop a program to store a large set of product data in two data structures — OOBTree and dict — and introduce a comparative analysis of their performance for executing work queries.

```bash
poetry run python .\app\tree_comparison.py
```

### Results
```
Total range_query time for Dict: 1.00726 seconds.
Total range_query time for OOBTree: 0.00180 seconds.
```