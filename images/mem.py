import hashlib
from django.core.cache import cache

from memcached_stats import MemcachedStats
mem = MemcachedStats()
print(mem.keys())
