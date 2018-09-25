# Part1. Remove Sensitive Data from github
## All done by kp2393
1. Create test.csv
```
  a, b, c
  Hallo, World, !
```
- Tried to make csv with python.
![making_csv](./img/make_csv.png)
- This is How it looks like.
![frame_csv](./img/csv_frame.png)
- Oh.. I made 1 more csv file named test1.csv because I misunderstood the way to make csv file, just in case.
![commits_csv](./img/commits.png)
type bash command to remove history
```
$git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch HW3_kp2393/test.csv HW3_kp2393/test2.csv' --prune-empty --tag-name-filter cat -- --all
$git push origin --force --all
```
- The next figure is result.
![result](./img/results.png)
