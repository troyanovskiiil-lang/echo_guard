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
