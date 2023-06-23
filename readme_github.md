1. cd ~ => for home directory
2. cd (paste path) => for master branch
3. cd .. => for previous 1 slash
4. git log (get info) 

******* [add on github]

1. git config --global user.name "gaureechoughule"
2. git config --global user.email "gpc1194@gmail.com"
3. git config --list
4. create repo. on github
5. git init
6. git status (untracked files : red color)
7. git add --all / git add . / git add -a
8. git status (green color)
9. git commit -m "first commit"
10. git status (working tree clean)
11. git remote add origin https://github.com/gaureechoughule/myprac.git [copy code from => code https on github]
12. git status (working tree clean)
13. git push origin master (see master on github)

********* [made some changes in any file]

1. git status (modified : red color)
2. git add --all / git add . / git add -a
3. git status (modified : green color)
4. git commit -m "second commit"
5. git push origin master (see changes in file on github)

******** [branch => no interfere with master]

git branch [only master : in green color]
git branch github [github => my branch name]
git branch [my branch also visible]
git checkout github
git branch [github : in green color]
now do any changes [or add new files]
git status (modified : red color)
git add --all / git add . / git add -a
git status (modified : green color)
git commit -m "added readme_github.md"
git push origin github [github => my branch name]
now 2/ 3 branches visible on github
click on github [my branch name] & see the changes

********** [take branch changes on master => only when boss said]

1. git branch [both branches are visible]
2. git checkout master
3. git merge github
4. git push -u origin master