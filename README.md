# Echo Guard

A lightweight, custom Python micro-function that acts as a smart "anti-spam" filter for data streams. It drops "echoes"—items that repeat too quickly within a sliding memory window.

## Features

* **Stream Filtering:** Works as a generator (`yield`), making it memory-efficient for large datasets or continuous streams.
* **Sliding Window:** Remembers the last N items to filter out rapid duplicates.
* **Custom Keys:** Supports a custom `key` function to evaluate complex objects or specific properties.

## Code

```python
def echo_guard(iterable, key=lambda x: x, window_size=3):
  """Filters a stream by dropping 'echoes' - items that appeared

  too recently within a sliding window of the last N steps.
  """
  seen_window = []
  for item in iterable:
    k = key(item)
    if k not in seen_window:
      yield item
      seen_window.append(k)
      if len(seen_window) > window_size:
        seen_window.pop(0)



[[[[[[[  [[[[[      [[[[[[[    [[[[[[[
[[       [[   [[    [[         [[
[[[[[[[  [[   [[    [[         [[
[[       [[[[[      [[[[[[[    [[[[[[[     to use (:
[[       [[   [     [[         [[
[[       [[     [   [[[[[[[    [[[[[[[
