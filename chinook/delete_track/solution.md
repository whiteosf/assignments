# Solution Notes

Take special care NOT to use python's string interpolation when building your query strings. This is a surefire way to get wrecked by injection, as explained in the documentation and accompanying XKCD comic.

I've included the original corrupted database here as `corrupt.old`. It can still be opened/queried like any other sqlite database.
