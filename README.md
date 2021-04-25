Deserialize 64 bit [roaring bitmaps](https://roaringbitmap.org/) into a Python set of integers. `roroaring64` is a lightweight Python binding on top of the [CRoaring](https://github.com/RoaringBitmap/CRoaring) library.

**Note:** `roroaring64` has only been testing on Linux, so OSX and Windows users, your mileage may vary.

# Motivation

[brotchie@](https://github.com/brotchie) built this library to deserialized the 64 bit roaring bitmaps [turbo-geth](https://github.com/ledgerwatch/turbo-geth) uses in its database model.

# API

The `roroaring64` module exposes a single method:

```python
def deserialize(serialized: bytes) -> Set[int]:
    ...
```

`deserialize` takes the byte representation of a 64 bit roaring bitmap serialized from the Go, Java, or C++ reference roaring bitmap implementations. It returns a Python set of all 64 bit integers contained within the input bitmap.

# Example Usage

```python
>>> import roroaring64
>>> hex_bitmap = "0100000000000000000000003a300000010000004700040010000000e64ee84ee94eea4eeb4e"
>>> values = roroaring64.deserialize(bytes.fromhex(hex_bitmap))
>>> print(values)
{4673254, 4673256, 4673257, 4673258, 4673259}
```

# Installation

```sh
$ pip install roroaring64
```

# Tests

```sh
$ python test.py
```

# Manual Compilation

```sh
$ python setup.py build_ext -i
```

# Credits

Thanks to the [authors](https://github.com/RoaringBitmap/CRoaring/blob/master/AUTHORS) of [CRoaring](https://github.com/RoaringBitmap/CRoaring) and to [ezibenroc@](https://github.com/Ezibenroc), the author of [PyRoaringBitmap](https://github.com/Ezibenroc/PyRoaringBitMap), whose project I looked at to work out Cython packaging.

# License

MIT License
