# Gradient Descent

## Observations

Score: **DECENT** - `learning_rate = 0.05` & `steps_number = 1000`

Baseline model yielded 89.6 - 89.7% accuracy.

Score: **BETTER** - `steps_number = 10000`

The model improved to 92.1% accuracy when `steps_number` was increased tenfold.

Score: **MEH** - `learning_rate = 0.01`

The model suffered slightly to 90.93% when `learning_rate` was decreased five-fold, while keeping the `steps_number` at `10000`.

Score: **GOOD** - `learning_rate = 0.1`

The model fit improved back to 92.22% when `learning_rate` was increased to twice the baseline.

...

After several iterations...

...

Score: **GOOD** - `learning_rate = 0.05` & `steps_number = 50000, 100000`

The model continued to only produce between 92.51% - 92.61% even with many more iterations at the conventional `learning_rate` of 0.05.

## Conclusions

The output range of 89% - 92% means our model will erroneously label roughly 1 in 10 digits.

Several batches within each run seemed to yield higher accuracy, but ultimately landed on a model that yielded higher losses. Experiments worth pursuing for better results:

- A more cautious `learning_rate` - more incremental approach to find the global minimum.
- A more experimental `learning_rate` - bolder exploration to find global minima more quickly, but could wander far off and mistake a local minimum for the global.
- Different type of cost function
- Different type of optimizer algorithm (ML technique)

<hr>

## Raw Values

### Initial Runs #1-2

Configs
- `learning_rate = 0.05`
- `steps_number = 1000`

#### Run #1
```
STEP 0, training batch accuracy 22 %
STEP 100, training batch accuracy 80 %
STEP 200, training batch accuracy 90 %
STEP 300, training batch accuracy 88 %
STEP 400, training batch accuracy 92 %
STEP 500, training batch accuracy 85 %
STEP 600, training batch accuracy 90 %
STEP 700, training batch accuracy 89 %
STEP 800, training batch accuracy 86 %
STEP 900, training batch accuracy 86 %
Test accuracy: 89.61 %
```

#### Run #2
```
STEP 0, training batch accuracy 11 %
STEP 100, training batch accuracy 84 %
STEP 200, training batch accuracy 80 %
STEP 300, training batch accuracy 83 %
STEP 400, training batch accuracy 85 %
STEP 500, training batch accuracy 82 %
STEP 600, training batch accuracy 90 %
STEP 700, training batch accuracy 91 %
STEP 800, training batch accuracy 88 %
STEP 900, training batch accuracy 84 %
Test accuracy: 89.74 %
```

### Run #3

Configs
- `learning_rate = 0.05`
- ***`steps_number = 10000`***

```
STEP 0, training batch accuracy 17 %
STEP 100, training batch accuracy 81 %
STEP 200, training batch accuracy 82 %
STEP 300, training batch accuracy 85 %
STEP 400, training batch accuracy 88 %
STEP 500, training batch accuracy 90 %
STEP 600, training batch accuracy 86 %
STEP 700, training batch accuracy 89 %
STEP 800, training batch accuracy 85 %
STEP 900, training batch accuracy 87 %
STEP 1000, training batch accuracy 90 %
STEP 2000, training batch accuracy 94 %
STEP 3000, training batch accuracy 94 %
STEP 4000, training batch accuracy 91 %
STEP 5000, training batch accuracy 88 %
STEP 6000, training batch accuracy 93 %
STEP 7000, training batch accuracy 91 %
STEP 8000, training batch accuracy 92 %
STEP 9000, training batch accuracy 93 %
Test accuracy: 92.1 %
```

### Run #4

Configs
- ***`learning_rate = 0.01`***
- `steps_number = 10000`

```
STEP 0, training batch accuracy 6 %
STEP 100, training batch accuracy 56 %
STEP 200, training batch accuracy 80 %
STEP 300, training batch accuracy 66 %
STEP 400, training batch accuracy 81 %
STEP 500, training batch accuracy 80 %
STEP 600, training batch accuracy 86 %
STEP 700, training batch accuracy 85 %
STEP 800, training batch accuracy 86 %
STEP 900, training batch accuracy 84 %
STEP 1000, training batch accuracy 77 %
STEP 2000, training batch accuracy 88 %
STEP 3000, training batch accuracy 90 %
STEP 4000, training batch accuracy 82 %
STEP 5000, training batch accuracy 88 %
STEP 6000, training batch accuracy 92 %
STEP 7000, training batch accuracy 94 %
STEP 8000, training batch accuracy 90 %
STEP 9000, training batch accuracy 87 %
Test accuracy: 90.93 %
```

### Run #5

Configs
- ***`learning_rate = 0.1`***
- `steps_number = 10000`

```
STEP 0, training batch accuracy 21 %
STEP 100, training batch accuracy 82 %
STEP 200, training batch accuracy 87 %
STEP 300, training batch accuracy 90 %
STEP 400, training batch accuracy 88 %
STEP 500, training batch accuracy 92 %
STEP 600, training batch accuracy 90 %
STEP 700, training batch accuracy 89 %
STEP 800, training batch accuracy 92 %
STEP 900, training batch accuracy 83 %
STEP 1000, training batch accuracy 86 %
STEP 2000, training batch accuracy 84 %
STEP 3000, training batch accuracy 90 %
STEP 4000, training batch accuracy 94 %
STEP 5000, training batch accuracy 97 %
STEP 6000, training batch accuracy 91 %
STEP 7000, training batch accuracy 91 %
STEP 8000, training batch accuracy 97 %
STEP 9000, training batch accuracy 94 %
Test accuracy: 92.22 %
```

### Run #6

Configs
- **`learning_rate = 0.05`**
- **`steps_number = 50000`**

```
STEP 0, training batch accuracy 21 %
STEP 10000, training batch accuracy 95 %
STEP 20000, training batch accuracy 89 %
STEP 30000, training batch accuracy 91 %
STEP 40000, training batch accuracy 94 %
Test accuracy: 92.51 %
```

### Run #7

Configs
- `learning_rate = 0.05`
- **`steps_number = 100000`**

```
STEP 0, training batch accuracy 11 %
STEP 10000, training batch accuracy 92 %
STEP 20000, training batch accuracy 95 %
STEP 30000, training batch accuracy 95 %
STEP 40000, training batch accuracy 92.5 %
STEP 50000, training batch accuracy 91 %
STEP 60000, training batch accuracy 95 %
STEP 70000, training batch accuracy 95.5 %
STEP 80000, training batch accuracy 95 %
STEP 90000, training batch accuracy 94.5 %
Test accuracy: 92.61 %
```

