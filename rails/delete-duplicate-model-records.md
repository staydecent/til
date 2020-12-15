# Delete duplicate model records 

You may want to do this via Rails, rather than directly in SQL, if you have something like `paper_trail` tracking model changes and deletions. 

In Rails Console:

```
dupe_ids = MyModel.group(:external_id, :created_at).having("count(*) > 1").pluck(Arel.sql('MIN(id) as id')); true
dupes = MyModel.where(id: dupe_ids); true
dupes.each{|d| d.destroy}; true

```
