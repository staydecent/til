# Query Optimizations

Prefix your query with `explain analyze` and copy the output to [explain.depesz](https://explain.depesz.com/).

## Seq Scan

If your seq scan is too slow, it's likely because your dataset is large and PG is scanning the whole set. Either filter your results or consider adding an index.

## External merge / Disk sort

This means your dataset didn't fit in memory, so PG had to use the disk to sort. Reduce dataset, or try increasing `work_mem`.
