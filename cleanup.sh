#!/bin/bash
# Usage:
#  ./cleanup.sh /PREFIX-NAME

PREFIX=$1

if [ -z "$PREFIX" ]; then
  echo "Usage: $0 <branch-prefix>"
  exit 1
fi

echo "Deleting local branches starting with '$PREFIX'..."

for branch in $(git branch | grep "$PREFIX"); do
  branch_clean=$(echo "$branch" | sed 's/\*//g' | xargs)
  if [[ "$branch_clean" != "main" && "$branch_clean" != "master" ]]; then
    git branch -D "$branch_clean"
  fi
done

echo "Clearing all stashes..."
git stash clear

echo "Cleanup complete."
