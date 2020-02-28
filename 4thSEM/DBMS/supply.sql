use supply;
select suppliers.sid 
from suppliers,parts,catalog 
where suppliers.sid=catalog.sid and parts.pid=catalog.pid and parts.color="red";
select suppliers.sid 
from suppliers,parts,catalog 
where suppliers.sid=catalog.sid and parts.pid=catalog.pid  and (parts.color="red" or suppliers.city="Bangalore");
select c1.sid,c2.sid
from catalog c1,catalog c2
where c1.sid>c2.sid and  c1.pid=c2.pid
