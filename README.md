# 1. Find Prime Factors by range

Finding prime factors in between a range by python.

Simple programs using for loops.

The results is sent as standard output.It's showed up as lists.

最大数と最低数を指定して、素因数を出力するコード。

for文を使用したシンプルなコードです。

結果は、標準出力されます。

## Usage

1. git clone
2. just run like this! ($ python3 combination_primefactors.py "mini_num" "max_num")

#### output

```
The range is between 0 to 10.
[2, 3, 5, 7]
```

# 2. Get combinations that can be got by adding prime numbers

Finding prime factors in between a range by python3.

Using priduct method, *itertools*, iterator, you can get combinations that you want to know.

from the rage you set, First get prime numbers, Second print all combinations of points that can compose a given max number.

※ this code suitable for small numbners.

最大数と最低数を指定して、素因数を取得します。

イテレーター、pythonのitertoolsのproductmethodを使用して、あなたが知りたい組み合わせを求めます。

あなたが指定した範囲から、まず素因数を取得します。次に、足し算をして、あなたが指定した範囲の最高値までの組み合わせを標準出力します。

このコードは小さい数字に向いている。

## Usage

1. git clone
2. just run like this! ($ python3 get_allcombinations_by_primenumbers.py "mini_num" "max_num")

#### output

```
The range is between 0 to 10.
Prime Numbers are:  [2, 3, 5, 7]
All combinations are:
[(2, 2, 3, 3),
 (2, 3, 2, 3),
 (2, 3, 3, 2),
 (3, 2, 2, 3),
 (3, 2, 3, 2),
 (3, 3, 2, 2),
 (2, 3, 5),
 (2, 5, 3),
 (3, 2, 5),
 (3, 5, 2),
 (5, 2, 3),
 (5, 3, 2),
 (3, 7),
 (5, 5),
 (7, 3)]
```
