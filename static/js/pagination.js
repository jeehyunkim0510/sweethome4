const pagination = document.getElementById('pageList');
const articles = {{ articles | safe }};
const itemsPerPage = 5;

unction displayArticles(currentPage) {
        const startIndex = (currentPage - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        const visibleArticles = articles.slice(startIndex, endIndex);

        const col = document.querySelector('.col-lg-8');
        col.innerHTML = '';

        for (const article of visibleArticles) {
            const card = document.createElement('div');
            card.className = 'card mb-4';

            const cardLink = document.createElement('a');
            cardLink.href = '#';

            const cardImg = document.createElement('img');
            cardImg.className = 'card-img-top';
            cardImg.src = article.image.url;
            cardImg.alt = 'Article Image';
            cardImg.style.maxHeight = '300px';

            cardLink.appendChild(cardImg);

            const cardBody = document.createElement('div');
            cardBody.className = 'card-body';

            const smallText = document.createElement('div');
            smallText.className = 'small text-muted';
            smallText.textContent = article.created_at;

            const cardText = document.createElement('p');
            cardText.className = 'card-text';
            cardText.textContent = article.content;

            const readMoreBtn = document.createElement('a');
            readMoreBtn.className = 'btn btn-primary';
            readMoreBtn.href = '#';
            readMoreBtn.textContent = 'Read more →';

            cardBody.appendChild(smallText);
            cardBody.appendChild(cardText);
            cardBody.appendChild(readMoreBtn);

            card.appendChild(cardLink);
            card.appendChild(cardBody);

            col.appendChild(card);
        }
    }
 function createPagination() {
        const totalPages = Math.ceil(articles.length / itemsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const li = document.createElement('li');
            li.className = 'page-item';
            const a = document.createElement('a');
            a.className = 'page-link';
            a.href = '#';
            a.textContent = i;

            a.addEventListener('click', function() {
                displayArticles(i);
            });

            li.appendChild(a);
            pagination.appendChild(li);
        }
    }
displayArticles(1);
createPagination();