# Identify memory hungry gems

Use [derailed](https://github.com/schneems/derailed_benchmark) in development to analyze memory and object allocations of gems.

`bundle exec derailed bundle:mem`

`bundle exec derailed bundle:objects`

If you identify gems that are a bit too hungry, check for updates that may address this, or consider alternatives.
