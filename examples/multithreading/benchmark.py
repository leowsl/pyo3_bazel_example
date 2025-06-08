import math
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Tuple, List

def work(start: int, end: int) -> float:
    return sum(math.sin(math.sqrt(i)) for i in range(start, end))

def work_threaded(iterations: int, thread_count: int) -> Tuple[float, float]:
    chunk_size = iterations // thread_count
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(thread_count - 1)]
    chunks.append(((thread_count - 1) * chunk_size, iterations))
    
    start = time.time()
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        results = list(executor.map(lambda c: work(c[0], c[1]), chunks))
    return time.time() - start, sum(results)

def work_no_threading(iterations: int) -> Tuple[float, float]:
    start = time.time()
    result = work(0, iterations)
    return time.time() - start, result
