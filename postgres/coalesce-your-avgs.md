# coalesce your avg's

If computing an avg on a column that can have NULL values, you may wish to `coalesce(some_column, 0)` to get the avg of all rows, not just those with a non-NULL value.
