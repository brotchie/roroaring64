# distutils: language = c++

from libc.stdint cimport uint32_t, uint64_t, int64_t
from libc.stdlib cimport malloc, free
from libcpp cimport bool

cdef extern from "roaring64map.hh" namespace "roaring":
  cdef cppclass Roaring64Map:
    uint64_t cardinality()
    void toUint64Array(uint64_t *ans)
    @staticmethod
    Roaring64Map readSafe(const char *buf, size_t maxbytes) except +


def deserialize(bytes serialized) -> set[int]:
  """Deserialize a portably serialized Roaring64Map.

  Params:
    serialized: Portable binary serialization of a Roaring64Map,
        compatible with C++, Go, and Java implementations.

  Returns:
    A Python set of the bitmap contents.

  Raises:
    MemoryError: Raised when temporary memory allocated to export
        map contents couldn't be allocated.
    RuntimeError: Raised when C++ code raises an exception, typically
        due to invalid input data.
  """
  map = Roaring64Map.readSafe(serialized, len(serialized))
  cdef uint64_t cardinality = map.cardinality()

  cdef uint64_t *contents = <uint64_t *>malloc(cardinality * sizeof(uint64_t))
  if not contents:
    raise MemoryError("Could not allocated memory to store Roaring64Map contents.")

  result = set()
  try:
    map.toUint64Array(contents)
    for i in range(cardinality):
      result.add(contents[i])
  finally:
    free(contents)

  return result