
use BooksDB;
SELECT title,COUNT(authors) as numberofauthors
FROM BooksDB.dbo.books
GROUP BY title
HAVING COUNT(authors) > 1;

SELECT title, authors
FROM booksDB.dbo.books;

SELECT 
    title,
    authors,
    LEN(authors) - LEN(REPLACE(authors, ',', '')) +1 AS author_count
FROM books
WHERE LEN(authors) - LEN(REPLACE(authors, ',', '')) > 1;


select forename,surname from drivers
where driverId IN (
    select DISTINCT driverId
    from results where position = '1'
)

select title from books 
where id IN(
    select Distinct tag_id 
    from tags t where t.tag_name = 'Meditation'
)

select title from books b 
inner join tags t on  b.id  = t.tag_id where t.tag_name ='Meditation';

select * from tags where tag_name = 'Meditation';


SELECT title
FROM books
WHERE id IN (
    SELECT goodreads_book_id
    FROM book_tags
    WHERE tag_id IN (
        SELECT id 
        FROM tags
        WHERE tag_name = 'Meditation'
    )
);

select * from book_tags;

select * from book_tags;

WITH meditation_books AS (
    SELECT bt.goodreads_book_id
    FROM book_tags bt
    JOIN tags t
        ON t.tag_id = bt.tag_id
    WHERE t.tag_name = 'Meditation'
)
SELECT b.title
FROM books b
WHERE b.id IN (SELECT goodreads_book_id FROM meditation_books);

select title from books;


SELECT 
title 
FROM BooksDB.dbo.books 
WHERE best_book_id IN (
    SELECT goodreads_book_id
    FROM BooksDB.dbo.book_tags
    WHERE tag_id = (
        SELECT tag_id 
        FROM tags 
        WHERE tag_name = 'meditation'
    )
);