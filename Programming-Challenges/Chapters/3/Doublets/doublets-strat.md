# Doublets Strat

## Naming

start = Starting word

end = End word

diff = The number of different letters between start and end

inc = The number of times diff is increased along the path

len = Number of steps between start and end

---

## Formulas

len = 2*inc + diff

---

## Idea

Instead of plain BFS (too many possible paths), we can use DFS with optimizations.

### Example:

booster -> roasted

diff = 3 (0, 2, 6)

That means min path has len >=3

Now we search for any path, prioritizing the ones which lower diff.

booster -> rooster -> roaster -> roasted

If we find a path which always lowers diff, it will ALWAYS have minimal length

If we get to a point where all possible options increase diff, we BFS them, looking for the first option which decreases diff again

When found, we DFS that path, and repeat the process

When doing BFS, we keep how many times diff was increased (this will be the way we compare multiple options) (let's call this variable 'inc')

This is needed because a possible scenario is the following:


- We DFS, don't find any path with inc=0
- Then BFS, find a decreasing option at inc=1
- We DFS that path, but again, we get stuck
- Then BFS again, finding another at inc=3
- This path ends at inc=3

But actually, in the first BFS, there is a decreasing option at inc=2, which actually reaches the end.

So, it turned out that the path with inc=2 (that would be, len=2*inc+diff=7) is better than the one at inc=3 (len=9)

This means that, if we reach BFS for the first time, we have to compare all possible options, just in case this happens.

But at least we can cut out some branches, as soon as we have any path (thus the importance of finding one soon).

For instance:

Let's think of a situation where we have a path (len=3), and we are looking for other possible paths.

If our current diff is 1, we know that the only way to improve our original path, is to have a path which ends in a single more step. (Any increasing option will bump our min len up to 3 (2*1+1)).

So, if *end* isn't a doublet of our current word, that entire branch can be cut out.

Similar to this, if we were at diff=2, and no decreasing option was found, we can cut out the branch as well (same reason as before).