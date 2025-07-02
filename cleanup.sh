#!/bin/bash
# Usage:
#  ./cleanup.sh PREFIX-NAME

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

# Ask the user if they want to clear the stash
read -p "Do you want to clear the git stash? (y/n): " clear_stash

# If the user confirms, clear the stash
if [[ "$clear_stash" =~ ^[Yy]$ ]]; then
  echo "Clearing all stashes..."
  git stash clear
  echo "Git stash cleared."
else
  echo "Git stash not cleared."
fi

echo "Cleanup complete."
