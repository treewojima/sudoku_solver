#!/bin/sh

BACKUP_DIR="../.solver.bak"

for d in $(find -type d); do
	#if 
	mkdir -p $BACKUP_DIR/$d
done

for f in $(find -type f -iname "*.py" -or -type f -iname "*.txt"); do
	ln -f $f $BACKUP_DIR/$f.hardlink	
done

cp -r .git $BACKUP_DIR
