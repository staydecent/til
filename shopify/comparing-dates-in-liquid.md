# Comparing dates in Liquid templates

The dates should be converted to unix timestamp to do numerical comparison, as comparing raw date classes does not seem to work. Best guess is liquid is doing string comparisons.

```
{%- assign now = 'now' | date -%}
{%- assign start = '2020-11-26 15:00' | date -%}
{%- assign end = '2020-12-01 00:00' | date -%}
```

```
{%- assign now = 'now' | date: "%s" -%}
{%- assign start = '2020-11-26 15:00' | date: "%s" -%}
{%- assign end = '2020-12-01 00:00' | date: "%s" -%}
```

Only the later will work as expected in the following:

```
{%- if now >= start and now < end -%}
```
