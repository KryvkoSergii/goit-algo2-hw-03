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
    <h2>Actual Flow of Goods</h2>
    <table>
        <thead>
            <tr>
                <th>Terminal</th>
                <th>Shop</th>
                <th>Actual Flow (units)</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Термінал 1</td><td>Магазин 1</td><td>15</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 2</td><td>10</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 3</td><td>20</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 4</td><td>15</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 5</td><td>10</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 6</td><td>20</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 7</td><td>15</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 8</td><td>15</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 9</td><td>10</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 10</td><td>0</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 11</td><td>0</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 12</td><td>0</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 13</td><td>0</td></tr>
            <tr><td>Термінал 1</td><td>Магазин 14</td><td>0</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 1</td><td>0</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 2</td><td>0</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 3</td><td>0</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 4</td><td>10</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 5</td><td>10</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 6</td><td>10</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 7</td><td>15</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 8</td><td>15</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 9</td><td>10</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 10</td><td>20</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 11</td><td>10</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 12</td><td>15</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 13</td><td>5</td></tr>
            <tr><td>Термінал 2</td><td>Магазин 14</td><td>10</td></tr>
        </tbody>
    </table>